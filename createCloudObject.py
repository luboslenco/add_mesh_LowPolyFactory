import bpy
import bmesh
from mathutils import Matrix
from mathutils import Euler
from math import radians
from random import seed, uniform
from add_mesh_LowPolyFactory.utils import *
from add_mesh_LowPolyFactory.materials import *


def draw_cloud(bm, prefs, translation=(0, 0, 0)):
    mat = Matrix()
    mat.translation = translation
    smin = prefs.lp_Cloud_Scale_Min
    smax = prefs.lp_Cloud_Scale_Max
    sx = uniform(smin[0], smax[0])
    sy = uniform(smin[1], smax[1])
    sz = uniform(smin[2], smax[2])
    scale = (sx, sy, sz)
    mat[0][0], mat[1][1], mat[2][2] = scale[0], scale[1], scale[2]
    e = Euler((uniform(0, 3.14), uniform(0, 3.14), uniform(0, 3.14)), 'XYZ')
    mat = mat * e.to_matrix().to_4x4()
    bmesh.ops.create_icosphere(bm, subdivisions=prefs.lp_Cloud_Subdivisions,
                               diameter=1.0, matrix=mat)
    return scale


def get_cloud_mesh(context, prefs):
    me = context.blend_data.meshes.new('temp_mesh')
    bm = bmesh.new()
    bm.from_mesh(me)

    spheres_min = prefs.lp_Cloud_Spheres_Min
    spheres_max = prefs.lp_Cloud_Spheres_Max
    num_spheres = get_random(spheres_min, spheres_max)

    trans = (0, 0, 0)
    for i in range(0, num_spheres):
        scale = draw_cloud(bm, prefs, translation=trans)
        r = get_random(0, 3)
        if r == 0:
            sdir = (1, 0, 0)
        elif r == 1:
            sdir = (-1, 0, 0)
        elif r == 2:
            sdir = (0, 1, 0)
        elif r == 3:
            sdir = (0, -1, 0)
        rand_z = uniform(-scale[2], scale[2]) / 2
        tx = trans[0] + scale[0] * 1.1 * sdir[0]
        ty = trans[1] + scale[1] * 1.1 * sdir[1]
        tz = trans[2] + scale[2] * 1.1 * sdir[2] + rand_z
        trans = (tx, ty, tz)

    bm.to_mesh(me)

    return me


def get_cloud_material(context):
    colors_from, colors_to = get_cloud_colors()
    return get_material(context, 'CloudMaterial', colors_from, colors_to), \
        colors_from, colors_to


def create_cloud(context, prefs):
    me = get_cloud_mesh(context, prefs)
    mat, colors_from, colors_to = get_cloud_material(context)
    bobject = create_object(context, 'Cloud', me, mat)

    make_vertex_colors(me, colors_from, colors_to, prefs)

    return bobject


def create_cloud_object(self, context, prefs):
    bpy.ops.object.select_all(action='DESELECT')

    location = context.scene.cursor_location.copy()
    cloud = create_cloud(context, prefs)

    if prefs.lp_Cloud_Keep_Modifiers:
        cloud.location = location
    else:
        context.scene.update()
        me_orig = cloud.data
        cloud.data = cloud.to_mesh(context.scene, True, 'PREVIEW')
        context.blend_data.meshes.remove(me_orig)
        cloud.location = location

    cloud.data.name = cloud.name
    cloud.select = True

    return cloud
