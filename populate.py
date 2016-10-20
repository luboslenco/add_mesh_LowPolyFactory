import bpy
import bmesh
from random import seed, uniform
import math
import mathutils
from mathutils import *
from add_mesh_LowPolyFactory import LowPolyFactory
from add_mesh_LowPolyFactory.createRockObject import *
from add_mesh_LowPolyFactory.createTreeObject import *
from add_mesh_LowPolyFactory.createBushObject import *
from add_mesh_LowPolyFactory.createGrassObject import *
from add_mesh_LowPolyFactory.createCloudObject import *
from add_mesh_LowPolyFactory.createTerrainObject import *
from add_mesh_LowPolyFactory.createWaterObject import *
from add_mesh_LowPolyFactory.drop import *


def populate(self, context, ground=None, spherical=False,
             merge=False, num_oaks=0, num_pines=0, num_palms=0,
             num_rocks=0, num_bushes=0, num_grass=0):

    # ground = create_terrain_object(
    #    self,
    #    context, 90, 90, size,
    #    strength=(40,40), scale=(20,20),
    #    weight1=(1,1), weight2=(2,2), weight3=(1,1))

    if ground is None:
        if len(bpy.context.selected_objects) > 0:
            ground = bpy.context.selected_objects[0]
        else:
            return

    obs = []

    # Trees
    tree_options = LowPolyFactory.add_mesh_tree.get_options(context)
    tree_type = tree_options.lp_Tree_Type

    tree_options.lp_Tree_Type = 'lp_Tree_Oak'

    for i in range(0, num_oaks):
        o = create_tree_object(self, context, tree_options)
        obs.append(o)

    tree_options.lp_Tree_Type = 'lp_Tree_Pine'

    for i in range(0, num_pines):
        o = create_tree_object(self, context, tree_options)
        obs.append(o)

    tree_options.lp_Tree_Type = 'lp_Tree_Palm'

    for i in range(0, num_palms):
        o = create_tree_object(self, context, tree_options)
        o.rotation_euler = (0, 0, uniform(0, math.pi * 2))
        obs.append(o)

    tree_options.lp_Tree_Type = tree_type

    # Rocks
    rock_options = LowPolyFactory.add_mesh_rock.get_options(context)

    for i in range(0, num_rocks):
        o = create_rock_object(self, context, rock_options)
        obs.append(o)

    # Bushes
    bushes_options = LowPolyFactory.add_mesh_bush.get_options(context)

    for i in range(0, num_bushes):
        o = create_bush_object(self, context, bushes_options)
        obs.append(o)

    # Grass
    grass_options = LowPolyFactory.add_mesh_grass.get_options(context)

    for i in range(0, num_grass):
        o = create_grass_object(self, context, grass_options)
        o.rotation_euler = (0, 0, uniform(0, math.pi * 2))
        obs.append(o)

    drop_objects(self, context, ground, obs, spherical)

    if merge:
        bpy.ops.object.select_all(action='DESELECT')
        for o in obs:
            o.select = True
        bpy.context.scene.objects.active = obs[0]
        obs[0].name = 'Population'
        obs[0].data.name = 'Population'
        bpy.ops.object.join()
