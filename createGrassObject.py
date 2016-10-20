import bpy
import bmesh
from mathutils import Matrix
from math import radians
from random import seed, uniform
from add_mesh_LowPolyFactory.utils import *
from add_mesh_LowPolyFactory.materials import *


def get_grass_mesh(context, prefs):
    me = context.blend_data.meshes.new('temp_mesh')
    bm = bmesh.new()
    bm.from_mesh(me)
    mat = Matrix()

    sx = uniform(prefs.lp_Grass_Scale_Min[0], prefs.lp_Grass_Scale_Max[0])
    sy = uniform(prefs.lp_Grass_Scale_Min[1], prefs.lp_Grass_Scale_Max[1])
    sz = uniform(prefs.lp_Grass_Scale_Min[2], prefs.lp_Grass_Scale_Max[2])
    blade_scale = (sx, sy, sz)
    mat[0][0], mat[1][1], mat[2][2] = (
        blade_scale[0], blade_scale[1], blade_scale[2])
    bmesh.ops.create_cube(bm, size=1, matrix=mat)
    faces = bm.faces[:]
    sc = uniform(prefs.lp_Grass_Grow_Scale_Min, prefs.lp_Grass_Grow_Scale_Max)
    scale_vec = (sc, sc, sc)
    dirx = uniform(prefs.lp_Grass_Dir_Min[0], prefs.lp_Grass_Dir_Max[0])
    diry = uniform(prefs.lp_Grass_Dir_Min[1], prefs.lp_Grass_Dir_Max[1])
    dirz = uniform(prefs.lp_Grass_Dir_Min[2], prefs.lp_Grass_Dir_Max[2])
    grow_direction = (dirx, diry, dirz)

    for face in faces:
        nor = face.normal  # Asume normalized normal
        dir = (grow_direction[0], grow_direction[1], grow_direction[2])
        if nor.z == 1:
            lenmin = prefs.lp_Grass_Length_Min
            lenmax = prefs.lp_Grass_Length_Max
            grass_length = get_random(lenmin, lenmax)
            bmesh.ops.scale(bm, vec=scale_vec, verts=face.verts)
            for i in range(0, grass_length):
                r = bmesh.ops.extrude_discrete_faces(bm, faces=[face])
                face = r['faces'][0]
                bmesh.ops.translate(bm, vec=dir, verts=face.verts)
                bmesh.ops.scale(bm, vec=scale_vec, verts=face.verts)
                dir = (dir[0] + grow_direction[0], dir[1], dir[2])

    bm.to_mesh(me)
    return me


def get_grass_material(context):
    colors_from, colors_to = get_grass_colors()
    return get_material(context, 'GrassMaterial', colors_from, colors_to), \
        colors_from, colors_to


def create_grass(context, prefs):
    me = get_grass_mesh(context, prefs)
    mat, colors_from, colors_to = get_grass_material(context)
    bobject = create_object(context, 'Grass', me, mat)

    make_vertex_colors(me, colors_from, colors_to, prefs)

    return bobject


def create_grass_object(self, context, prefs):
    bpy.ops.object.select_all(action='DESELECT')

    location = context.scene.cursor_location.copy()
    grass = create_grass(context, prefs)

    if prefs.lp_Grass_Keep_Modifiers:
        grass.location = location
    else:
        context.scene.update()
        me_orig = grass.data
        grass.data = grass.to_mesh(context.scene, True, 'PREVIEW')
        context.blend_data.meshes.remove(me_orig)
        grass.location = location

    grass.data.name = grass.name
    grass.select = True

    return grass
