import bpy
import bmesh
from mathutils import Matrix
from mathutils import Euler
from math import radians
from random import seed, uniform
from add_mesh_LowPolyFactory.utils import *
from add_mesh_LowPolyFactory.materials import *


def get_coconuts_mesh(context, prefs):
    me = context.blend_data.meshes.new('temp_mesh')
    bm = bmesh.new()
    bm.from_mesh(me)
    mat = Matrix()

    trunk_length = prefs.palm_stage_length * prefs.palm_stages

    coconutX = (0.29, -0.29, 0,     0)
    coconutY = (0,     0,    0.29, -0.29)
    coconutZ = trunk_length - 0.2

    coconuts = get_random(prefs.lp_Tree_Palm_Top_Coconuts_Min,
                          prefs.lp_Tree_Palm_Top_Coconuts_Max)

    for i in range(0, coconuts):
        mat.translation = (coconutX[i], coconutY[i], coconutZ)
        bmesh.ops.create_icosphere(
            bm,
            subdivisions=1,
            diameter=0.15,
            matrix=mat)

    bm.to_mesh(me)

    return me


def get_coconuts_material(context):
    colors_from, colors_to = get_tree_coconut_colors()
    return get_material(context, 'TreeCoconutMaterial',
                        colors_from, colors_to), \
        colors_from, colors_to


def create_coconuts(context, prefs):
    me = get_coconuts_mesh(context, prefs)
    mat, colors_from, colors_to = get_coconuts_material(context)
    make_vertex_colors(me, colors_from, colors_to, prefs)
    return create_object(context, 'TreeCoconuts', me, mat)


def get_trunk_mesh(context, prefs):
    me = context.blend_data.meshes.new('temp_mesh')
    bm = bmesh.new()
    bm.from_mesh(me)
    mat = Matrix()
    tt = prefs.lp_Tree_Type

    if tt == 'lp_Tree_Oak' or tt == 'lp_Tree_Pine':
        segments = get_random(prefs.lp_Tree_Trunk_Segments_Min,
                              prefs.lp_Tree_Trunk_Segments_Max)
        trunklen = uniform(prefs.lp_Tree_Trunk_Length_Min,
                           prefs.lp_Tree_Trunk_Length_Max)
        prefs.trunk_depth = 2.0 * trunklen
        mat.translation = (0, 0, prefs.trunk_depth / 2)
        trunk_diameter1 = 0.15 * uniform(prefs.lp_Tree_Trunk_Diameter1_Min,
                                         prefs.lp_Tree_Trunk_Diameter1_Max)
        trunk_diameter2 = 0.15 * uniform(prefs.lp_Tree_Trunk_Diameter2_Min,
                                         prefs.lp_Tree_Trunk_Diameter2_Max)
        bmesh.ops.create_cone(
            bm,
            cap_ends=False,
            cap_tris=True,
            segments=segments,
            diameter1=trunk_diameter1,
            diameter2=trunk_diameter2,
            depth=prefs.trunk_depth,
            matrix=mat)
    elif tt == 'lp_Tree_Palm':
        prefs.palm_stages = get_random(
            prefs.lp_Tree_Palm_Trunk_Stages_Min,
            prefs.lp_Tree_Palm_Trunk_Stages_Max)
        segments = get_random(
            prefs.lp_Tree_Palm_Trunk_Segments_Min,
            prefs.lp_Tree_Palm_Trunk_Segments_Max)
        prefs.palm_stage_length = uniform(
            prefs.lp_Tree_Palm_Trunk_Stage_Length_Min,
            prefs.lp_Tree_Palm_Trunk_Stage_Length_Max)
        stage_length = prefs.palm_stage_length
        diameter1 = uniform(
            prefs.lp_Tree_Palm_Trunk_Diameter1_Min,
            prefs.lp_Tree_Palm_Trunk_Diameter1_Max)
        diameter2 = uniform(
            prefs.lp_Tree_Palm_Trunk_Diameter2_Min,
            prefs.lp_Tree_Palm_Trunk_Diameter1_Max)
        for i in range(0, prefs.palm_stages):
            scale = 1
            mat[0][0], mat[1][1], mat[2][2] = (scale, scale, scale)
            # e = Euler((0, uniform(0, 0.2), 0), 'XYZ')
            # mat = mat * e.to_matrix().to_4x4()
            mat.translation = (0, 0, (stage_length / 2 + i * stage_length))
            bmesh.ops.create_cone(
                bm, cap_ends=True,
                cap_tris=True,
                segments=segments,
                diameter1=diameter1,
                diameter2=diameter2,
                depth=stage_length,
                matrix=mat)
            # mat = Matrix()

    bm.to_mesh(me)
    return me


def get_trunk_material(context, prefs):
    if prefs.lp_Tree_Type == 'lp_Tree_Palm':
        material_name = 'TreeTrunkPalmMaterial'
        colors_from, colors_to = get_tree_trunk_palm_colors()
    else:
        material_name = 'TreeTrunkMaterial'
        colors_from, colors_to = get_tree_trunk_colors()

    return get_material(context, material_name, colors_from, colors_to), \
        colors_from, colors_to


def create_trunk(context, prefs):
    me = get_trunk_mesh(context, prefs)
    mat, colors_from, colors_to = get_trunk_material(context, prefs)
    make_vertex_colors(me, colors_from, colors_to, prefs)
    return create_object(context, 'TreeTrunk', me, mat)


def get_top_mesh(context, prefs):
    me = context.blend_data.meshes.new('temp_mesh')
    bm = bmesh.new()
    bm.from_mesh(me)
    mat = Matrix()
    tt = prefs.lp_Tree_Type

    if tt == 'lp_Tree_Oak':
        mat.translation = (0, 0, prefs.trunk_depth)
        tsmin = prefs.lp_Tree_Top_Scale_Min
        tsmax = prefs.lp_Tree_Top_Scale_Max
        mat[0][0], mat[1][1], mat[2][2] = (
            uniform(tsmin[0], tsmax[0]),
            uniform(tsmin[1], tsmax[1]),
            uniform(tsmin[2], tsmax[2]))
        bmesh.ops.create_icosphere(
            bm,
            subdivisions=prefs.lp_Tree_Top_Subdivisions,
            diameter=1.0,
            matrix=mat)
    elif tt == 'lp_Tree_Pine':
        segments = get_random(
            prefs.lp_Tree_Top_Stage_Segments_Min,
            prefs.lp_Tree_Top_Stage_Segments_Max)
        stages = get_random(
            prefs.lp_Tree_Top_Stages_Min,
            prefs.lp_Tree_Top_Stages_Max)
        td = prefs.trunk_depth - 0.7
        sstep = uniform(
            prefs.lp_Tree_Top_Stage_Step_Min,
            prefs.lp_Tree_Top_Stage_Step_Max)
        ssmin = prefs.lp_Tree_Top_Stage_Size_Min
        ssmax = prefs.lp_Tree_Top_Stage_Size_Max
        ssize = (
            uniform(ssmin[0], ssmax[0]),
            uniform(ssmin[1], ssmax[1]),
            uniform(ssmin[2], ssmax[2]))
        for i in range(0, stages):
            mult = prefs.lp_Tree_Top_Stage_Shrink_Multiplier * (i / 4)
            sc = (1 - i * prefs.lp_Tree_Top_Stage_Shrink * mult) * 0.9
            if sc < 0.01:
                sc = 0.01
            mat[0][0], mat[1][1], mat[2][2] = (
                sc * ssize[0], sc * ssize[1], sc * ssize[2])
            mat.translation = (
                0, 0, (td + ((ssize[2] - 1) / 2) + i * sstep) * 0.85)
            if prefs.lp_Tree_Top_Rotate_Stages:
                e = Euler((0, 0, uniform(0, 3.14)), 'XYZ')
                mat = mat * e.to_matrix().to_4x4()
            bmesh.ops.create_cone(
                bm,
                cap_ends=True,
                cap_tris=True,
                segments=segments,
                diameter1=(prefs.lp_Tree_Top_Stage_Diameter),
                diameter2=0,
                depth=(0.85),
                matrix=mat)
            mat = Matrix()
    elif tt == 'lp_Tree_Palm':
        trunk_length = prefs.palm_stage_length * prefs.palm_stages
        leaf_length = get_random(
            prefs.lp_Tree_Palm_Top_Leaf_Length_Min,
            prefs.lp_Tree_Palm_Top_Leaf_Length_Max)
        leaf_size = uniform(
            prefs.lp_Tree_Palm_Top_Leaf_Size_Min,
            prefs.lp_Tree_Palm_Top_Leaf_Size_Max)

        mat.translation = (0, 0, trunk_length)
        leaves = get_random(
            prefs.lp_Tree_Palm_Top_Leaves_Min,
            prefs.lp_Tree_Palm_Top_Leaves_Max)
        bmesh.ops.create_cone(
            bm,
            cap_ends=True,
            cap_tris=True,
            segments=leaves,
            diameter1=leaf_size,
            diameter2=leaf_size,
            depth=0.1,
            matrix=mat)
        faces = bm.faces[:]
        for face in faces:
            nor = face.normal  # Asume normalized normal
            dir = (nor.x * 0.3, nor.y * 0.3, -0.12)
            if nor.z == 0:
                for i in range(0, leaf_length):
                    r = bmesh.ops.extrude_discrete_faces(bm, faces=[face])
                    bmesh.ops.translate(
                        bm, vec=dir, verts=r['faces'][0].verts)
                    face = r['faces'][0]
                    dir = (dir[0], dir[1], dir[2] - 0.08)
                # Align last face verts
                mid = [0, 0, 0]
                for v in face.verts:
                    mid[0] += v.co.x
                    mid[1] += v.co.y
                    mid[2] += v.co.z
                mid[0] /= len(face.verts)
                mid[1] /= len(face.verts)
                mid[2] /= len(face.verts)
                for v in face.verts:
                    v.co.x, v.co.y, v.co.z = mid[0], mid[1], mid[2]

    bm.to_mesh(me)
    return me


def get_top_material(context, prefs):
    tt = prefs.lp_Tree_Type
    if tt == 'lp_Tree_Oak':
        material_name = 'TreeTopOakMaterial'
        colors_from, colors_to = get_tree_top_oak_colors()
    elif tt == 'lp_Tree_Pine':
        material_name = 'TreeTopPineMaterial'
        colors_from, colors_to = get_tree_top_pine_colors()
    elif tt == 'lp_Tree_Palm':
        material_name = 'TreeTopPalmMaterial'
        colors_from, colors_to = get_tree_top_palm_colors()

    return get_material(context, material_name, colors_from, colors_to), \
        colors_from, colors_to


def create_top(context, prefs):
    me = get_top_mesh(context, prefs)
    mat, colors_from, colors_to = get_top_material(context, prefs)
    bobject = create_object(context, 'TreeTop', me, mat)

    make_vertex_colors(me, colors_from, colors_to, prefs)

    if prefs.lp_Tree_Type == 'lp_Tree_Oak':
        noise_origin = apply_displacement(
            context,
            bobject,
            strength=(prefs.lp_Tree_Top_Strength_Min,
                      prefs.lp_Tree_Top_Strength_Max),
            scale=(prefs.lp_Tree_Top_NScale_Min,
                   prefs.lp_Tree_Top_NScale_Max),
            weight1=(prefs.lp_Tree_Top_Weight1, prefs.lp_Tree_Top_Weight1),
            weight2=(prefs.lp_Tree_Top_Weight2, prefs.lp_Tree_Top_Weight2),
            weight3=(prefs.lp_Tree_Top_Weight3, prefs.lp_Tree_Top_Weight3))
    else:
        noise_origin = None

    return bobject, noise_origin


def create_tree_object(self, context, prefs):
    bpy.ops.object.select_all(action='DESELECT')

    location = context.scene.cursor_location.copy()

    tree_trunk = create_trunk(context, prefs)
    tree_top, noise_origin = create_top(context, prefs)

    if prefs.lp_Tree_Type == 'lp_Tree_Palm':
        tree_extra = create_coconuts(context, prefs)
    else:
        tree_extra = None

    if prefs.lp_Tree_Keep_Modifiers:
        tree_top.location = location
        tree_trunk.location = location
        if noise_origin is not None:
            noise_origin.location += location
        tree_trunk.data.name = tree_trunk.name
        tree_top.data.name = tree_top.name
        tree_top.select = True
        if tree_extra is not None:
            tree_extra.location = location
            tree_extra.data.name = tree_extra.name
    else:
        context.scene.update()
        me_orig = tree_top.data
        if noise_origin is not None:  # Displacement was performed
            tex = tree_top.modifiers['displace'].texture
        else:
            tex = None
        tree_top.data = tree_top.to_mesh(context.scene, True, 'PREVIEW')
        context.blend_data.meshes.remove(me_orig)
        tree_top.modifiers.clear()
        tree_top.location = location
        tree_trunk.location = location
        if tree_extra is not None:
            tree_extra.location = location
        if noise_origin is not None:
            context.scene.objects.unlink(noise_origin)
            context.blend_data.objects.remove(noise_origin)
        if tex is not None:
            context.blend_data.textures.remove(tex)

        # Join objects
        tree_top.select = True
        tree_trunk.select = True
        if tree_extra is not None:
            tree_extra.select = True
        bpy.context.scene.objects.active = tree_top
        bpy.ops.object.join()

        # ext = ''
        # if pos > 0:
        #    ext = ".{:03d}".format(pos)

        tree_top.name = 'Tree'
        tree_top.data.name = tree_top.name
        tree_top.select = True

    return tree_top
