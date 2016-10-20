import bpy
import mathutils
from bpy.types import Operator
from bpy.props import *
from add_mesh_LowPolyFactory.createRockObject import *
from add_mesh_LowPolyFactory.createTreeObject import *
from add_mesh_LowPolyFactory.createBushObject import *
from add_mesh_LowPolyFactory.createGrassObject import *
from add_mesh_LowPolyFactory.createCloudObject import *
from add_mesh_LowPolyFactory.createTerrainObject import *
from add_mesh_LowPolyFactory.createWaterObject import *


def get_prefs(context):
    return context.user_preferences.addons[__package__].preferences


class Options():
    pass


class add_mesh_rock(Operator):
    """"""
    bl_idname = "mesh.rock_add"
    bl_label = "Add Rock"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}
    bl_description = "adds low poly rocks"

    def draw(self, context):
        prefs = get_prefs(context)
        layout = self.layout
        layout.prop(prefs, 'lp_Rock_Subdivisions')
        layout.label("Scale Min")
        layout.prop(prefs, 'lp_Rock_Scale_Min')
        layout.label("Scale Max")
        layout.prop(prefs, 'lp_Rock_Scale_Max')

        layout.label("Dispalce Strength")
        layout.prop(prefs, 'lp_Rock_Strength_Min')
        layout.prop(prefs, 'lp_Rock_Strength_Max')

        layout.label("Dispalce Scale")
        layout.prop(prefs, 'lp_Rock_NScale_Min')
        layout.prop(prefs, 'lp_Rock_NScale_Max')

        layout.label("Dispalce Weights")
        layout.prop(prefs, 'lp_Rock_Weight1')
        layout.prop(prefs, 'lp_Rock_Weight2')
        layout.prop(prefs, 'lp_Rock_Weight3')
        layout.prop(prefs, 'lp_Rock_Keep_Modifiers')

    @classmethod
    def poll(cls, context):
        return (context.scene is not None)

    def get_options(context):
        return get_prefs(context)

    def execute(self, context):
        create_rock_object(
            self,
            context,
            add_mesh_rock.get_options(context))
        return {'FINISHED'}

    def invoke(self, context, event):
        self.execute(context)
        return {'FINISHED'}


class add_mesh_tree(Operator):
    """"""
    bl_idname = "mesh.tree_add"
    bl_label = "Add Tree"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}
    bl_description = "adds low poly tree"

    def draw(self, context):
        prefs = get_prefs(context)
        layout = self.layout
        layout.prop(prefs, 'lp_Tree_Type')
        layout.prop(prefs, 'lp_Tree_Setting')
        if prefs.lp_Tree_Setting == 'lp_Tree_Trunk':
            box = layout.box()
            if prefs.lp_Tree_Type == 'lp_Tree_Palm':
                box.label("Segments")
                box.prop(prefs, 'lp_Tree_Palm_Trunk_Segments_Min')
                box.prop(prefs, 'lp_Tree_Palm_Trunk_Segments_Max')
                box.label("Stages")
                box.prop(prefs, 'lp_Tree_Palm_Trunk_Stages_Min')
                box.prop(prefs, 'lp_Tree_Palm_Trunk_Stages_Max')
                box.label("Stage Length")
                box.prop(prefs, 'lp_Tree_Palm_Trunk_Stage_Length_Min')
                box.prop(prefs, 'lp_Tree_Palm_Trunk_Stage_Length_Max')
                box.label("Stage Diameter")
                box.prop(prefs, 'lp_Tree_Palm_Trunk_Diameter1_Min')
                box.prop(prefs, 'lp_Tree_Palm_Trunk_Diameter1_Max')
                box.prop(prefs, 'lp_Tree_Palm_Trunk_Diameter2_Min')
                box.prop(prefs, 'lp_Tree_Palm_Trunk_Diameter2_Max')
            else:
                box.label("Segments")
                box.prop(prefs, 'lp_Tree_Trunk_Segments_Min')
                box.prop(prefs, 'lp_Tree_Trunk_Segments_Max')
                box.label("Length")
                box.prop(prefs, 'lp_Tree_Trunk_Length_Min')
                box.prop(prefs, 'lp_Tree_Trunk_Length_Max')
                box.label("Diameter")
                box.prop(prefs, 'lp_Tree_Trunk_Diameter1_Min')
                box.prop(prefs, 'lp_Tree_Trunk_Diameter1_Max')
                box.prop(prefs, 'lp_Tree_Trunk_Diameter2_Min')
                box.prop(prefs, 'lp_Tree_Trunk_Diameter2_Max')

        if prefs.lp_Tree_Setting == 'lp_Tree_Top':
            box = layout.box()
            if prefs.lp_Tree_Type == 'lp_Tree_Oak':
                box.prop(prefs, 'lp_Tree_Top_Subdivisions')
                box.label("Scale Min")
                box.prop(prefs, 'lp_Tree_Top_Scale_Min')
                box.label("Scale Max")
                box.prop(prefs, 'lp_Tree_Top_Scale_Max')

                box.label("Dispalce Strength")
                box.prop(prefs, 'lp_Tree_Top_Strength_Min')
                box.prop(prefs, 'lp_Tree_Top_Strength_Max')

                box.label("Dispalce Scale")
                box.prop(prefs, 'lp_Tree_Top_NScale_Min')
                box.prop(prefs, 'lp_Tree_Top_NScale_Max')

                box.label("Dispalce Weights")
                box.prop(prefs, 'lp_Tree_Top_Weight1')
                box.prop(prefs, 'lp_Tree_Top_Weight2')
                box.prop(prefs, 'lp_Tree_Top_Weight3')
            elif prefs.lp_Tree_Type == 'lp_Tree_Pine':
                box.label("Stages")
                box.prop(prefs, 'lp_Tree_Top_Stages_Min')
                box.prop(prefs, 'lp_Tree_Top_Stages_Max')
                box.label("Stage Size Min")
                box.prop(prefs, 'lp_Tree_Top_Stage_Size_Min')
                box.label("Stage Size Max")
                box.prop(prefs, 'lp_Tree_Top_Stage_Size_Max')
                # box.prop(prefs, 'lp_Tree_Top_Stage_Diameter')
                box.prop(prefs, 'lp_Tree_Top_Stage_Shrink')
                box.prop(prefs, 'lp_Tree_Top_Stage_Shrink_Multiplier')
                box.label("Stage Step")
                box.prop(prefs, 'lp_Tree_Top_Stage_Step_Min')
                box.prop(prefs, 'lp_Tree_Top_Stage_Step_Max')
                box.label("Stage Segments")
                box.prop(prefs, 'lp_Tree_Top_Stage_Segments_Min')
                box.prop(prefs, 'lp_Tree_Top_Stage_Segments_Max')
                box.prop(prefs, 'lp_Tree_Top_Rotate_Stages')
            elif prefs.lp_Tree_Type == 'lp_Tree_Palm':
                box.label("Leaves")
                box.prop(prefs, 'lp_Tree_Palm_Top_Leaves_Min')
                box.prop(prefs, 'lp_Tree_Palm_Top_Leaves_Max')
                box.label("Leaf Length")
                box.prop(prefs, 'lp_Tree_Palm_Top_Leaf_Length_Min')
                box.prop(prefs, 'lp_Tree_Palm_Top_Leaf_Length_Max')
                box.label("Leaf Size")
                box.prop(prefs, 'lp_Tree_Palm_Top_Leaf_Size_Min')
                box.prop(prefs, 'lp_Tree_Palm_Top_Leaf_Size_Max')
                box.label("Coconuts")
                box.prop(prefs, 'lp_Tree_Palm_Top_Coconuts_Min')
                box.prop(prefs, 'lp_Tree_Palm_Top_Coconuts_Max')

        layout.label("")
        layout.prop(prefs, 'lp_Tree_Keep_Modifiers')

    @classmethod
    def poll(cls, context):
        return (context.scene is not None)

    def get_options(context):
        return get_prefs(context)

    def execute(self, context):
        create_tree_object(self, context, add_mesh_tree.get_options(context))
        return {'FINISHED'}

    def invoke(self, context, event):
        self.execute(context)
        return {'FINISHED'}


class add_mesh_bush(Operator):
    """"""
    bl_idname = "mesh.bush_add"
    bl_label = "Add Bush"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}
    bl_description = "adds low poly bush"

    def draw(self, context):
        prefs = get_prefs(context)
        layout = self.layout
        layout.prop(prefs, 'lp_Bush_Subdivisions')
        layout.label("Scale Min")
        layout.prop(prefs, 'lp_Bush_Scale_Min')
        layout.label("Scale Max")
        layout.prop(prefs, 'lp_Bush_Scale_Max')

        layout.label("Dispalce Strength")
        layout.prop(prefs, 'lp_Bush_Strength_Min')
        layout.prop(prefs, 'lp_Bush_Strength_Max')

        layout.label("Dispalce Scale")
        layout.prop(prefs, 'lp_Bush_NScale_Min')
        layout.prop(prefs, 'lp_Bush_NScale_Max')

        layout.label("Dispalce Weights")
        layout.prop(prefs, 'lp_Bush_Weight1')
        layout.prop(prefs, 'lp_Bush_Weight2')
        layout.prop(prefs, 'lp_Bush_Weight3')
        layout.prop(prefs, 'lp_Bush_Keep_Modifiers')

    @classmethod
    def poll(cls, context):
        return (context.scene is not None)

    def get_options(context):
        return get_prefs(context)

    def execute(self, context):
        create_bush_object(self, context, add_mesh_bush.get_options(context))
        return {'FINISHED'}

    def invoke(self, context, event):
        self.execute(context)
        return {'FINISHED'}


class add_mesh_grass(Operator):
    """"""
    bl_idname = "mesh.grass_add"
    bl_label = "Add Grass"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}
    bl_description = "adds low poly grass"

    def draw(self, context):
        prefs = get_prefs(context)
        layout = self.layout
        layout.label("Length")
        layout.prop(prefs, 'lp_Grass_Length_Min')
        layout.prop(prefs, 'lp_Grass_Length_Max')
        layout.label("Grow scale")
        layout.prop(prefs, 'lp_Grass_Grow_Scale_Min')
        layout.prop(prefs, 'lp_Grass_Grow_Scale_Max')
        layout.label("Grow Direction Min")
        layout.prop(prefs, 'lp_Grass_Dir_Min')
        layout.label("Grow Direction Max")
        layout.prop(prefs, 'lp_Grass_Dir_Max')
        layout.label("Scale Min")
        layout.prop(prefs, 'lp_Grass_Scale_Min')
        layout.label("Scale Max")
        layout.prop(prefs, 'lp_Grass_Scale_Max')
        # layout.prop(prefs, 'lp_Grass_Keep_Modifiers')

    @classmethod
    def poll(cls, context):
        return (context.scene is not None)

    def get_options(context):
        return get_prefs(context)

    def execute(self, context):
        create_grass_object(self, context, add_mesh_grass.get_options(context))
        return {'FINISHED'}

    def invoke(self, context, event):
        self.execute(context)
        return {'FINISHED'}


class add_mesh_cloud(Operator):
    """"""
    bl_idname = "mesh.cloud_add"
    bl_label = "Add Cloud"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}
    bl_description = "adds low poly cloud"

    def draw(self, context):
        prefs = get_prefs(context)
        layout = self.layout
        layout.prop(prefs, 'lp_Cloud_Subdivisions')
        layout.label("Spheres")
        layout.prop(prefs, 'lp_Cloud_Spheres_Min')
        layout.prop(prefs, 'lp_Cloud_Spheres_Max')
        layout.label("Scale Min")
        layout.prop(prefs, 'lp_Cloud_Scale_Min')
        layout.label("Scale Max")
        layout.prop(prefs, 'lp_Cloud_Scale_Max')
        # layout.prop(prefs, 'lp_Cloud_Keep_Modifiers')

    @classmethod
    def poll(cls, context):
        return (context.scene is not None)

    def get_options(context):
        return get_prefs(context)

    def execute(self, context):
        create_cloud_object(
            self, context, add_mesh_cloud.get_options(context))
        return {'FINISHED'}

    def invoke(self, context, event):
        self.execute(context)
        return {'FINISHED'}


class add_mesh_terrain(Operator):
    """"""
    bl_idname = "mesh.terrain_add"
    bl_label = "Add Terrain"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}
    bl_description = "adds low poly terrain"

    def draw(self, context):
        prefs = get_prefs(context)
        layout = self.layout
        layout.prop(prefs, 'lp_Terrain_Type')

        layout.prop(prefs, 'lp_Terrain_Size')

        if prefs.lp_Terrain_Type == 'lp_Terrain_Plane':
            layout.label("Segments")
            layout.prop(prefs, 'lp_Terrain_X_Segments')
            layout.prop(prefs, 'lp_Terrain_Y_Segments')
        elif prefs.lp_Terrain_Type == 'lp_Terrain_Sphere':
            layout.prop(prefs, 'lp_Terrain_Subdivisions')

        layout.prop(prefs, 'lp_Terrain_Displace_Type')

        layout.label("Dispalce Strength")
        layout.prop(prefs, 'lp_Terrain_Strength_Min')
        layout.prop(prefs, 'lp_Terrain_Strength_Max')

        layout.label("Dispalce Scale")
        layout.prop(prefs, 'lp_Terrain_Scale_Min')
        layout.prop(prefs, 'lp_Terrain_Scale_Max')

        if prefs.lp_Terrain_Displace_Type == 'lp_Terrain_Displace_Voronoi':
            layout.label("Dispalce Weights")
            layout.prop(prefs, 'lp_Terrain_Weight1')
            layout.prop(prefs, 'lp_Terrain_Weight2')
            layout.prop(prefs, 'lp_Terrain_Weight3')

        layout.label("")
        layout.prop(prefs, 'lp_Terrain_Keep_Modifiers')

    @classmethod
    def poll(cls, context):
        return (context.scene is not None)

    def get_options(context):
        return get_prefs(context)

    def execute(self, context):
        create_terrain_object(
            self, context, add_mesh_terrain.get_options(context))
        return {'FINISHED'}

    def invoke(self, context, event):
        self.execute(context)
        return {'FINISHED'}


class add_mesh_water(Operator):
    """"""
    bl_idname = "mesh.water_add"
    bl_label = "Add Water"
    bl_options = {'REGISTER', 'UNDO', 'PRESET'}
    bl_description = "adds low poly water"

    def draw(self, context):
        prefs = get_prefs(context)
        layout = self.layout
        layout.prop(prefs, 'lp_Water_Type')
        layout.prop(prefs, 'lp_Water_Size')

        if prefs.lp_Water_Type == 'lp_Water_Plane':
            layout.label("Segments")
            layout.prop(prefs, 'lp_Water_X_Segments')
            layout.prop(prefs, 'lp_Water_Y_Segments')
        elif prefs.lp_Water_Type == 'lp_Water_Sphere':
            layout.prop(prefs, 'lp_Water_Subdivisions')

        layout.label("")
        layout.prop(prefs, 'lp_Water_Displace')

        if prefs.lp_Water_Displace:
            layout.label("Dispalce Strength")
            layout.prop(prefs, 'lp_Water_Strength_Min')
            layout.prop(prefs, 'lp_Water_Strength_Max')

            layout.label("Dispalce Scale")
            layout.prop(prefs, 'lp_Water_Scale_Min')
            layout.prop(prefs, 'lp_Water_Scale_Max')

        layout.prop(prefs, 'lp_Water_Keep_Modifiers')

    @classmethod
    def poll(cls, context):
        return (context.scene is not None)

    def get_options(context):
        return get_prefs(context)

    def execute(self, context):
        create_water_object(
            self, context, add_mesh_water.get_options(context))
        return {'FINISHED'}

    def invoke(self, context, event):
        self.execute(context)
        return {'FINISHED'}
