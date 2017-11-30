# Modified version of
# http://wiki.blender.org/index.php/Extensions:2.6/Py/Scripts/Object/Drop_to_ground
import bpy
import bmesh
from random import seed, uniform
import math
import mathutils
from mathutils import *


def transform_ground_to_world(sc, ground):
    tmpMesh = ground.to_mesh(sc, True, 'PREVIEW')
    tmpMesh.transform(ground.matrix_world)
    tmp_ground = bpy.data.objects.new('tmpGround', tmpMesh)
    sc.objects.link(tmp_ground)
    sc.update()
    return tmp_ground


def get_lowest_world_co_from_mesh(ob, mat_parent=None):
    bme = bmesh.new()
    bme.from_mesh(ob.data)
    mat_to_world = ob.matrix_world.copy()
    if mat_parent:
        mat_to_world = mat_parent * mat_to_world
    lowest = None
    # bme.verts.index_update()
    for v in bme.verts:
        if not lowest:
            lowest = v
        if (mat_to_world * v.co).z < (mat_to_world * lowest.co).z:
            lowest = v
    lowest_co = mat_to_world * lowest.co
    bme.free()
    return lowest_co


def drop_objects(self, context, ground, obs, spherical=False, use_origin=True):
    halfX = ground.dimensions.x / 2
    halfY = ground.dimensions.y / 2

    for ob in obs:
        if spherical is True:
            ob.matrix_world = Matrix.Translation((0, 0, 100))
        else:
            ob.location = (
                ground.location.x + uniform(-halfX, halfX),
                ground.location.y + uniform(-halfY, halfY),
                ground.location.z + 100)

    if spherical is True:
        ground.matrix_world.translation = ((0, 0, 0))
    tmp_ground = transform_ground_to_world(context.scene, ground)
    down = Vector((0, 0, -10000))
    mat_original = ground.matrix_world.copy()

    for ob in obs:
        if use_origin:
            lowest_world_co = ob.location
        else:
            lowest_world_co = get_lowest_world_co_from_mesh(ob)

        if not lowest_world_co:
            continue

        if spherical is True:
            e = Euler(
                (uniform(0, math.pi * 2),
                 uniform(0, math.pi * 2),
                 uniform(0, math.pi * 2)),
                'XYZ')
            mat_rot = e.to_matrix().to_4x4()
            ground.matrix_world = mat_rot * mat_original

        if bpy.app.version < (2, 76, 5):  # ray_cast api changed
            hit_location, hit_normal, hit_index = \
                tmp_ground.ray_cast(lowest_world_co, lowest_world_co + down)
        else:
        	was_hit, hit_location, hit_normal, hit_index = \
                tmp_ground.ray_cast(lowest_world_co, lowest_world_co + down)

        if hit_index is -1:
            continue

        to_ground_vec = hit_location - lowest_world_co
        ob.matrix_world *= Matrix.Translation(to_ground_vec)

        if spherical is True:
            ob.matrix_world = mat_rot * ob.matrix_world

    ground.matrix_world = mat_original

    bpy.ops.object.select_all(action='DESELECT')
    tmp_ground.select = True
    bpy.ops.object.delete('EXEC_DEFAULT')
    for ob in obs:
        ob.select = True
    ground.select = True
    bpy.context.scene.objects.active = ground
