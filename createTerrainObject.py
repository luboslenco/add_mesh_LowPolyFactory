import bpy
import bmesh
from mathutils import Matrix
from math import radians
from random import seed, uniform
from add_mesh_LowPolyFactory.utils import *
from add_mesh_LowPolyFactory.materials import *


def get_terrain_mesh(context, prefs):
    me = context.blend_data.meshes.new('temp_mesh')
    bm = bmesh.new()
    bm.from_mesh(me)
    mat = Matrix()

    if prefs.lp_Terrain_Type == 'lp_Terrain_Plane':
        bmesh.ops.create_grid(
            bm,
            x_segments=prefs.lp_Terrain_X_Segments,
            y_segments=prefs.lp_Terrain_Y_Segments,
            size=prefs.lp_Terrain_Size,
            matrix=mat)
        bmesh.ops.triangulate(bm, faces=bm.faces)
    elif prefs.lp_Terrain_Type == 'lp_Terrain_Sphere':
        bmesh.ops.create_icosphere(
            bm,
            subdivisions=prefs.lp_Terrain_Subdivisions,
            diameter=prefs.lp_Terrain_Size,
            matrix=mat)

    bm.to_mesh(me)
    return me


def get_terrain_material(context):
    colors_from, colors_to = get_terrain_colors()
    return get_material(context, 'TerrainMaterial', colors_from, colors_to), \
        colors_from, colors_to


def create_terrain(context, prefs):
    me = get_terrain_mesh(context, prefs)
    mat, colors_from, colors_to = get_terrain_material(context)
    bobject = create_object(context, 'Terrain', me, mat)

    make_vertex_colors(me, colors_from, colors_to, prefs)

    noise_origin = apply_displacement(
        context,
        bobject,
        disptype=prefs.lp_Terrain_Displace_Type,
        strength=(prefs.lp_Terrain_Strength_Min,
                  prefs.lp_Terrain_Strength_Max),
        scale=(prefs.lp_Terrain_Scale_Min, prefs.lp_Terrain_Scale_Max),
        weight1=(prefs.lp_Terrain_Weight1, prefs.lp_Terrain_Weight1),
        weight2=(prefs.lp_Terrain_Weight2, prefs.lp_Terrain_Weight2),
        weight3=(prefs.lp_Terrain_Weight3, prefs.lp_Terrain_Weight3))

    return bobject, noise_origin


def create_terrain_object(self, context, prefs):
    bpy.ops.object.select_all(action='DESELECT')

    location = context.scene.cursor_location.copy()
    terrain, noise_origin = create_terrain(context, prefs)

    if prefs.lp_Terrain_Keep_Modifiers:
        terrain.location = location
        noise_origin.location += location
    else:
        context.scene.update()
        me_orig = terrain.data
        tex = terrain.modifiers['displace'].texture
        terrain.data = terrain.to_mesh(context.scene, True, 'PREVIEW')
        context.blend_data.meshes.remove(me_orig)
        terrain.modifiers.clear()
        terrain.location = location
        context.scene.objects.unlink(noise_origin)
        context.blend_data.objects.remove(noise_origin)
        context.blend_data.textures.remove(tex)

    terrain.data.name = terrain.name
    terrain.select = True

    return terrain
