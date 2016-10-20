import bpy
from bpy.props import *
from add_mesh_LowPolyFactory.materials import *
from add_mesh_LowPolyFactory.populate import *


def get_prefs(context):
    return context.user_preferences.addons[__package__].preferences


class LPF_Panel(bpy.types.Panel):
    bl_label = "LowPoly Factory"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "render"

    def draw(self, context):
        prefs = get_prefs(context)
        layout = self.layout

        layout.prop(prefs, 'lp_Populate_VCols')

        row = layout.row()
        # split = row.split(percentage=0.7)
        # split.prop(prefs, 'lp_Theme_Type')
        # split.operator("lpf.update_materials")
        # row = layout.row()
        # split = row.split(percentage=0.7)
        row.prop(prefs, 'lp_Light_Type')
        row.operator("lpf.update_lighting")

        layout.label("Populating")
        # layout.prop(prefs, 'lp_Distribution_Type')
        layout.prop(prefs, 'lp_Populate_Oaks')
        layout.prop(prefs, 'lp_Populate_Pines')
        layout.prop(prefs, 'lp_Populate_Palms')
        layout.prop(prefs, 'lp_Populate_Rocks')
        layout.prop(prefs, 'lp_Populate_Bushes')
        layout.prop(prefs, 'lp_Populate_Grass')
        row = layout.row()
        split = row.split(percentage=0.35)
        split.prop(prefs, 'lp_Populate_Spherical')
        split = split.split(percentage=0.5)
        split.prop(prefs, 'lp_Populate_Merge')
        split.operator("lpf.populate")

    def execute(self, context):
        return {'FINISHED'}


class LPF_UpdateMaterialsButton(bpy.types.Operator):
    bl_idname = "lpf.update_materials"
    bl_label = "Set Theme"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        prefs = get_prefs(context)
        theme = prefs.lp_Theme_Type

        for mat in bpy.data.materials:
            colors_from = None
            colors_to = None

            if mat.name == 'TerrainMaterial':
                colors_from, colors_to = get_terrain_colors(theme)

            elif mat.name == 'BushMaterial':
                colors_from, colors_to = get_bush_colors(theme)

            elif mat.name == 'CloudMaterial':
                colors_from, colors_to = get_cloud_colors(theme)

            elif mat.name == 'RockMaterial':
                colors_from, colors_to = get_rock_colors(theme)

            elif mat.name == 'TreeTrunkMaterial':
                colors_from, colors_to = get_tree_trunk_colors(theme)
            elif mat.name == 'TreeTrunkPalmMaterial':
                colors_from, colors_to = get_tree_trunk_palm_colors(theme)

            elif mat.name == 'TreeTopOakMaterial':
                colors_from, colors_to = get_tree_top_oak_colors(theme)
            elif mat.name == 'TreeTopPineMaterial':
                colors_from, colors_to = get_tree_top_pine_colors(theme)
            elif mat.name == 'TreeTopPalmMaterial':
                colors_from, colors_to = get_tree_top_palm_colors(theme)
            elif mat.name == 'TreeCoconutMaterial':
                colors_from, colors_to = get_tree_coconut_colors(theme)

            elif mat.name == 'WaterMaterial':
                colors_from, colors_to = get_water_colors(theme)

            if colors_from is not None:
                nodes = mat.node_tree.nodes
                cr_node = nodes['ColorRamp']
                cr_node.color_ramp.elements[0].color = colors_from
                cr_node.color_ramp.elements[1].color = colors_to

        return {'FINISHED'}


class LPF_UpdateLightingButton(bpy.types.Operator):
    bl_idname = "lpf.update_lighting"
    bl_label = "Set Lights"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        context.scene.render.engine = 'CYCLES'

        prefs = get_prefs(context)
        c = bpy.context

        # Remove existing lighting
        for o in bpy.data.objects:
            if o.type == 'LAMP':
                c.scene.objects.unlink(o)
                c.blend_data.objects.remove(o)

        # Create new lamp
        lamp_data = bpy.data.lamps.new(name="Lamp", type='SUN')
        lamp_object = bpy.data.objects.new(
            name="Lamp",
            object_data=lamp_data)
        c.scene.objects.link(lamp_object)
        # Place lamp to a specified location
        e = Euler((radians(37), radians(3), radians(107)), 'XYZ')
        lamp_object.matrix_world *= e.to_matrix().to_4x4()
        lamp_object.matrix_world.translation = (4.0, 1.0, 6.0)
        lamp_data.use_nodes = True
        bpy.data.worlds[0].use_nodes = True
        lamp_nodes = lamp_data.node_tree.nodes
        world_nodes = bpy.data.worlds[0].node_tree.nodes
        world_inp0 = world_nodes['Background'].inputs[0]
        world_inp1 = world_nodes['Background'].inputs[1]

        if prefs.lp_Light_Type == 'lp_Light_Midday':
            lamp_nodes['Emission'].inputs[1].default_value = 2.2
            world_inp0.default_value = [1, 1, 1, 1]
            world_inp1.default_value = 1.0
        elif prefs.lp_Light_Type == 'lp_Light_Night':
            lamp_nodes['Emission'].inputs[1].default_value = 0.2
            world_inp0.default_value = [0, 0.073, 0.147, 1]
            world_inp1.default_value = 3.0
        elif prefs.lp_Light_Type == 'lp_Light_Dusk':
            lamp_nodes['Emission'].inputs[1].default_value = 0.5
            world_inp0.default_value = [0.334, 0.274, 0.402, 1]
            world_inp1.default_value = 2.0
        elif prefs.lp_Light_Type == 'lp_Light_Dawn':
            lamp_nodes['Emission'].inputs[1].default_value = 1.0
            world_inp0.default_value = [0.869, 0.570, 0.371, 1]
            world_inp1.default_value = 2.0

        lamp_object.select = True
        c.scene.objects.active = lamp_object

        return {'FINISHED'}


class LPF_PopulateButton(bpy.types.Operator):
    bl_idname = "lpf.populate"
    bl_label = "Populate"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        prefs = get_prefs(context)

        populate(
            self, context,
            spherical=prefs.lp_Populate_Spherical,
            merge=prefs.lp_Populate_Merge,
            num_oaks=prefs.lp_Populate_Oaks,
            num_pines=prefs.lp_Populate_Pines,
            num_palms=prefs.lp_Populate_Palms,
            num_rocks=prefs.lp_Populate_Rocks,
            num_bushes=prefs.lp_Populate_Bushes,
            num_grass=prefs.lp_Populate_Grass)

        return {'FINISHED'}
