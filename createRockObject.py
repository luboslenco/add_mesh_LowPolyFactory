import bpy
import bmesh
from mathutils import Matrix
from math import radians
from random import seed, uniform
from add_mesh_LowPolyFactory.utils import *
from add_mesh_LowPolyFactory.materials import *


def get_rock_mesh(context, prefs):
    me = context.blend_data.meshes.new('temp_mesh')
    bm = bmesh.new()
    bm.from_mesh(me)
    mat = Matrix()
    smin = prefs.lp_Rock_Scale_Min
    smax = prefs.lp_Rock_Scale_Max
    matx = uniform(smin[0], smax[0])
    maty = uniform(smin[1], smax[1])
    matz = uniform(smin[2], smax[2])
    mat[0][0], mat[1][1], mat[2][2] = (matx, maty, matz)
    bmesh.ops.create_icosphere(bm, subdivisions=prefs.lp_Rock_Subdivisions,
                               diameter=1.0, matrix=mat)
    bm.to_mesh(me)

    return me


def get_rock_material(context):
    colors_from, colors_to = get_rock_colors()
    return get_material(context, 'RockMaterial', colors_from, colors_to), \
        colors_from, colors_to


def create_rock(context, prefs):
    me = get_rock_mesh(context, prefs)
    mat, colors_from, colors_to = get_rock_material(context)
    bobject = create_object(context, 'Rock', me, mat)

    make_vertex_colors(me, colors_from, colors_to, prefs)

    noise_origin = apply_displacement(
        context, bobject,
        strength=(prefs.lp_Rock_Strength_Min, prefs.lp_Rock_Strength_Max),
        scale=(prefs.lp_Rock_NScale_Min, prefs.lp_Rock_NScale_Max),
        weight1=(prefs.lp_Rock_Weight1, prefs.lp_Rock_Weight1),
        weight2=(prefs.lp_Rock_Weight2, prefs.lp_Rock_Weight2),
        weight3=(prefs.lp_Rock_Weight3, prefs.lp_Rock_Weight3))

    return bobject, noise_origin


def create_rock_object(self, context, prefs):
    bpy.ops.object.select_all(action='DESELECT')

    location = context.scene.cursor_location.copy()

    rock, noise_origin = create_rock(context, prefs)

    if prefs.lp_Rock_Keep_Modifiers:
        rock.location = location
        noise_origin.location += location
    else:
        context.scene.update()
        me_orig = rock.data
        tex = rock.modifiers['displace'].texture
        rock.data = rock.to_mesh(context.scene, True, 'PREVIEW')
        context.blend_data.meshes.remove(me_orig)
        rock.modifiers.clear()
        rock.location = location
        context.scene.objects.unlink(noise_origin)
        context.blend_data.objects.remove(noise_origin)
        context.blend_data.textures.remove(tex)

    rock.data.name = rock.name
    rock.select = True

    return rock
