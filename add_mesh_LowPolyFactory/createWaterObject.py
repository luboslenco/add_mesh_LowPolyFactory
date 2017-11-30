import bpy
import bmesh
from mathutils import Matrix
from math import radians
from random import seed, uniform
from add_mesh_LowPolyFactory.utils import *
from add_mesh_LowPolyFactory.materials import *


def get_water_mesh(context, prefs):
    me = context.blend_data.meshes.new('temp_mesh')
    bm = bmesh.new()
    bm.from_mesh(me)
    mat = Matrix()

    if prefs.lp_Water_Type == 'lp_Water_Plane':
        bmesh.ops.create_grid(
            bm,
            x_segments=prefs.lp_Water_X_Segments,
            y_segments=prefs.lp_Water_Y_Segments,
            size=prefs.lp_Water_Size, matrix=mat)
        bmesh.ops.triangulate(bm, faces=bm.faces)
    elif prefs.lp_Water_Type == 'lp_Water_Sphere':
        bmesh.ops.create_icosphere(
            bm,
            subdivisions=prefs.lp_Water_Subdivisions,
            diameter=prefs.lp_Water_Size,
            matrix=mat)

    bm.to_mesh(me)
    return me


def get_water_material(context):
    colors_from, colors_to = get_water_colors()
    return get_material_water(context, 'WaterMaterial',
                              colors_from, colors_to), \
        colors_from, colors_to


def create_water(context, prefs):
    me = get_water_mesh(context, prefs)
    mat, colors_from, colors_to = get_water_material(context)
    bobject = create_object(context, 'Water', me, mat)

    make_vertex_colors(me, colors_from, colors_to, prefs)

    noise_origin = None
    if prefs.lp_Water_Displace is True:
        noise_origin = apply_displacement(
            context,
            bobject,
            strength=(prefs.lp_Water_Strength_Min,
                      prefs.lp_Water_Strength_Max),
            scale=(prefs.lp_Water_Scale_Min, prefs.lp_Water_Scale_Max))

    return bobject, noise_origin


def create_water_object(self, context, prefs):
    bpy.ops.object.select_all(action='DESELECT')

    location = context.scene.cursor_location.copy()
    water, noise_origin = create_water(context, prefs)

    if prefs.lp_Water_Keep_Modifiers:
        water.location = location
        if noise_origin is not None:
            noise_origin.location += location
    else:
        context.scene.update()
        me_orig = water.data
        if noise_origin is not None:
            tex = water.modifiers['displace'].texture
        water.data = water.to_mesh(context.scene, True, 'PREVIEW')
        context.blend_data.meshes.remove(me_orig)
        water.modifiers.clear()
        water.location = location
        if noise_origin is not None:
            context.scene.objects.unlink(noise_origin)
            context.blend_data.objects.remove(noise_origin)
            context.blend_data.textures.remove(tex)

    water.data.name = water.name
    water.select = True

    return water
