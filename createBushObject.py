import bpy
import bmesh
from mathutils import Matrix
from math import radians
from random import seed, uniform
from add_mesh_LowPolyFactory.utils import *
from add_mesh_LowPolyFactory.materials import *


def get_bush_mesh(context, prefs):
    me = context.blend_data.meshes.new('temp_mesh')
    bm = bmesh.new()
    bm.from_mesh(me)
    mat = Matrix()
    smin = prefs.lp_Rock_Scale_Min
    smax = prefs.lp_Rock_Scale_Max
    sx = uniform(smin[0], smax[0])
    sy = uniform(smin[1], smax[1])
    sz = uniform(smin[2], smax[2])
    scale = (sx, sy, sz)
    mat[0][0], mat[1][1], mat[2][2] = (scale[0], scale[1], scale[2])
    diameter = uniform(0.45, 0.55)
    mat.translation = (0, 0, diameter * scale[2])
    bmesh.ops.create_icosphere(bm, subdivisions=prefs.lp_Bush_Subdivisions,
                               diameter=diameter, matrix=mat)
    bm.to_mesh(me)

    return me


def get_bush_material(context):
    colors_from, colors_to = get_bush_colors()
    return get_material(context, 'BushMaterial', colors_from, colors_to), \
        colors_from, colors_to


def create_bush(context, prefs):
    me = get_bush_mesh(context, prefs)
    mat, colors_from, colors_to = get_bush_material(context)
    bobject = create_object(context, 'Bush', me, mat)

    make_vertex_colors(me, colors_from, colors_to, prefs)

    noise_origin = apply_displacement(
        context, bobject,
        strength=(prefs.lp_Bush_Strength_Min, prefs.lp_Bush_Strength_Max),
        scale=(prefs.lp_Bush_NScale_Min, prefs.lp_Bush_NScale_Max),
        weight1=(prefs.lp_Bush_Weight1, prefs.lp_Bush_Weight1),
        weight2=(prefs.lp_Bush_Weight2, prefs.lp_Bush_Weight2),
        weight3=(prefs.lp_Bush_Weight3, prefs.lp_Bush_Weight3))

    return bobject, noise_origin


def create_bush_object(self, context, prefs):
    bpy.ops.object.select_all(action='DESELECT')

    location = context.scene.cursor_location.copy()
    bush, noise_origin = create_bush(context, prefs)

    if prefs.lp_Bush_Keep_Modifiers:
        bush.location = location
        noise_origin.location += location
    else:
        context.scene.update()
        me_orig = bush.data
        tex = bush.modifiers['displace'].texture
        bush.data = bush.to_mesh(context.scene, True, 'PREVIEW')
        context.blend_data.meshes.remove(me_orig)
        bush.modifiers.clear()
        bush.location = location
        context.scene.objects.unlink(noise_origin)
        context.blend_data.objects.remove(noise_origin)
        context.blend_data.textures.remove(tex)

    bush.data.name = bush.name
    bush.select = True

    return bush
