from bpy.types import Operator, AddonPreferences
from bpy.props import *


class LPFAddonPreferences(AddonPreferences):
    bl_idname = __package__

    # Editor
    lp_Populate_VCols = BoolProperty(
        attr='lp_Populate_VCols',
        name='Bake Vertex Colors',
        description='Bake material colors to vertex colors',
        default=True)

    Theme_Type_List = [
        ('lp_Theme_Autumn', 'Autumn', 'Autumn Theme'),
        ('lp_Theme_Summer', 'Summer', 'Summer Theme'),
        ('lp_Theme_Spring', 'Spring', 'Spring Theme'),
        ('lp_Theme_Winter', 'Winter', 'Winter Theme'),
        ('lp_Theme_Tropic', 'Tropic', 'Tropic Theme')]
    lp_Theme_Type = EnumProperty(
        attr='lp_Theme_Type',
        name='Theme',
        description='Choose theme',
        items=Theme_Type_List, default='lp_Theme_Autumn')

    Light_Type_List = [
        ('lp_Light_Midday', 'Midday', 'Midday Light'),
        ('lp_Light_Night', 'Night', 'Night Light'),
        ('lp_Light_Dusk', 'Dusk', 'Dusk Light'),
        ('lp_Light_Dawn', 'Dawn', 'Dawn Light')]
    lp_Light_Type = EnumProperty(
        attr='lp_Light_Type',
        name='Light',
        description='Choose light',
        items=Light_Type_List, default='lp_Light_Midday')

    Distribution_Type_List = [
        ('lp_Distribution_Random', 'Random', 'Random Distribution')]
    lp_Distribution_Type = EnumProperty(
        attr='lp_Distribution_Type',
        name='Distribution',
        description='Choose distribution',
        items=Distribution_Type_List, default='lp_Distribution_Random')

    lp_Populate_Oaks = IntProperty(
        attr='lp_Populate_Oaks',
        name='Oaks',
        description='How many oaks to spawn',
        default=20, min=0)

    lp_Populate_Pines = IntProperty(
        attr='lp_Populate_Pines',
        name='Pines',
        description='How many pines to spawn',
        default=15, min=0)

    lp_Populate_Palms = IntProperty(
        attr='lp_Populate_Palms',
        name='Palms',
        description='How many palms to spawn',
        default=0, min=0)

    lp_Populate_Rocks = IntProperty(
        attr='lp_Populate_Rocks',
        name='Rocks',
        description='How many rocks to spawn',
        default=5, min=0)

    lp_Populate_Bushes = IntProperty(
        attr='lp_Populate_Bushes',
        name='Bushes',
        description='How many bushes to spawn',
        default=5, min=0)

    lp_Populate_Grass = IntProperty(
        attr='lp_Populate_Grass',
        name='Grass',
        description='How many grass blades to spawn',
        default=0, min=0)

    lp_Populate_Spherical = BoolProperty(
        attr='lp_Populate_Spherical',
        name='Spherical',
        description='Use to populate spherical terrains',
        default=False)

    lp_Populate_Merge = BoolProperty(
        attr='lp_Populate_Merge',
        name='Merge',
        description='Merge created objects into single one',
        default=False)

    # Rock
    lp_Rock_Subdivisions = IntProperty(
        attr='lp_Rock_Subdivisions',
        name='Subdivisions',
        description='Rock Subdivisions',
        default=1, min=1)

    lp_Rock_Scale_Min = FloatVectorProperty(
        attr='lp_Rock_Scale_Min',
        name='',
        description='Minimum Scale',
        default=[0.4, 0.4, 0.4], size=3, min=0)

    lp_Rock_Scale_Max = FloatVectorProperty(
        attr='lp_Rock_Scale_Max',
        name='',
        description='Maximum Scale',
        default=[1.3, 1.3, 1.1], size=3, min=0)

    # Rock Noise
    lp_Rock_Strength_Min = FloatProperty(
        attr='lp_Rock_Strength_Min',
        name='Min',
        description='Rock Strength',
        default=-1.8)

    lp_Rock_Strength_Max = FloatProperty(
        attr='lp_Rock_Strength_Max',
        name='Max',
        description='Rock Strength',
        default=-1.2)

    lp_Rock_NScale_Min = FloatProperty(
        attr='lp_Rock_NScale_Min',
        name='Min',
        description='Rock Noise Scale',
        default=0.25, min=0.0001)

    lp_Rock_NScale_Max = FloatProperty(
        attr='lp_Rock_NScale_Max',
        name='Max',
        description='Rock Noise Scale',
        default=0.25, min=0.0001)

    lp_Rock_Weight1 = FloatProperty(
        attr='lp_Rock_Weight1',
        name='1',
        description='Rock Weight 1',
        default=1, min=-2, max=2)

    lp_Rock_Weight2 = FloatProperty(
        attr='lp_Rock_Weight2',
        name='2',
        description='Rock Weight 2',
        default=0, min=-2, max=2)

    lp_Rock_Weight3 = FloatProperty(
        attr='lp_Rock_Weight3',
        name='3',
        description='Rock Weight 3',
        default=0, min=-2, max=2)

    lp_Rock_Keep_Modifiers = BoolProperty(
        attr='lp_Rock_Keep_Modifiers',
        name='Keep Modifiers',
        description='Whether to apply modifiers or not',
        default=False)

    # Tree
    Tree_Setting_List = [
        ('lp_Tree_Trunk', 'Trunk', 'Trunk Settings'),
        ('lp_Tree_Top', 'Top', 'Top Settings')]
    lp_Tree_Setting = EnumProperty(
        attr='lp_Tree_Setting',
        name='Settings',
        description='Choose settings to display',
        items=Tree_Setting_List, default='lp_Tree_Trunk')

    Tree_Type_List = [
        ('lp_Tree_Oak', 'Oak', 'Oak Tree'),
        ('lp_Tree_Pine', 'Pine', 'Pine Tree'),
        ('lp_Tree_Palm', 'Palm', 'Palm Tree')]
    lp_Tree_Type = EnumProperty(
        attr='lp_Tree_Type',
        name='Type',
        description='Choose the tree type',
        items=Tree_Type_List, default='lp_Tree_Oak')

    lp_Tree_Trunk_Segments_Min = IntProperty(
        attr='lp_Tree_Trunk_Segments_Min',
        name='Min',
        description='Minimum Trunk Segments',
        default=4, min=3)

    lp_Tree_Trunk_Segments_Max = IntProperty(
        attr='lp_Tree_Trunk_Segments_Max',
        name='Max',
        description='Maximum Trunk Segments',
        default=4, min=3)

    lp_Tree_Palm_Trunk_Segments_Min = IntProperty(
        attr='lp_Tree_Palm_Trunk_Segments_Min',
        name='Min',
        description='Minimum Trunk Segments',
        default=6, min=3)

    lp_Tree_Palm_Trunk_Segments_Max = IntProperty(
        attr='lp_Tree_Palm_Trunk_Segments_Max',
        name='Max',
        description='Maximum Trunk Segments',
        default=8, min=3)

    lp_Tree_Trunk_Length_Min = FloatProperty(
        attr='lp_Tree_Trunk_Length_Min',
        name='Min',
        description='Minimum Trunk Length Ratio',
        default=0.9, min=0)

    lp_Tree_Trunk_Length_Max = FloatProperty(
        attr='lp_Tree_Trunk_Length_Max',
        name='Max',
        description='Maximum Trunk Length Ratio',
        default=1.15, min=0)

    lp_Tree_Trunk_Diameter1_Min = FloatProperty(
        attr='lp_Tree_Trunk_Diameter1_Min',
        name='Bottom Min',
        description='Minimum Trunk Diameter Bottom Ratio',
        default=1, min=0)

    lp_Tree_Trunk_Diameter1_Max = FloatProperty(
        attr='lp_Tree_Trunk_Diameter1_Max',
        name='Bottom Max',
        description='Maximum Trunk Diameter Bottom Ratio',
        default=1.1, min=0)

    lp_Tree_Trunk_Diameter2_Min = FloatProperty(
        attr='lp_Tree_Trunk_Diameter2_Min',
        name='Top Min',
        description='Minimum Trunk Diameter Top Ratio',
        default=0.25, min=0)

    lp_Tree_Trunk_Diameter2_Max = FloatProperty(
        attr='lp_Tree_Trunk_Diameter2_Max',
        name='Top Max',
        description='Maximum Trunk Diameter Top Ratio',
        default=0.3, min=0)

    # Palm
    lp_Tree_Palm_Trunk_Stages_Min = IntProperty(
        attr='lp_Tree_Palm_Trunk_Stages_Min',
        name='Min',
        description='Minimum Trunk Stages',
        default=7, min=1)

    lp_Tree_Palm_Trunk_Stages_Max = IntProperty(
        attr='lp_Tree_Palm_Trunk_Stages_Max',
        name='Max',
        description='Maximum Trunk Stages',
        default=8, min=1)

    lp_Tree_Palm_Trunk_Stage_Length_Min = FloatProperty(
        attr='lp_Tree_Palm_Trunk_Stage_Length_Min',
        name='Min',
        description='Minimum Trunk Stage Length',
        default=0.35, min=0)

    lp_Tree_Palm_Trunk_Stage_Length_Max = FloatProperty(
        attr='lp_Tree_Palm_Trunk_Stage_Length_Max',
        name='Max',
        description='Maximum Trunk Stage Length',
        default=0.45, min=0)

    lp_Tree_Palm_Trunk_Diameter1_Min = FloatProperty(
        attr='lp_Tree_Palm_Trunk_Diameter1_Min',
        name='Bottom Min',
        description='Minimum Trunk Diameter Bottom Ratio',
        default=0.15, min=0)

    lp_Tree_Palm_Trunk_Diameter1_Max = FloatProperty(
        attr='lp_Tree_Palm_Trunk_Diameter1_Max',
        name='Bottom Max',
        description='Maximum Trunk Diameter Bottom Ratio',
        default=0.17, min=0)

    lp_Tree_Palm_Trunk_Diameter2_Min = FloatProperty(
        attr='lp_Tree_Palm_Trunk_Diameter2_Min',
        name='Top Min',
        description='Minimum Trunk Diameter Top Ratio',
        default=0.25, min=0)

    lp_Tree_Palm_Trunk_Diameter2_Max = FloatProperty(
        attr='lp_Tree_Palm_Trunk_Diameter2_Max',
        name='Top Max',
        description='Maximum Trunk Diameter Top Ratio',
        default=0.27, min=0)

    # Top
    lp_Tree_Top_Scale_Min = FloatVectorProperty(
        attr='lp_Tree_Top_Scale_Min',
        name='',
        description='Minimum Top Scale',
        default=[0.8, 0.8, 0.8], size=3, min=0)

    lp_Tree_Top_Scale_Max = FloatVectorProperty(
        attr='lp_Tree_Top_Scale_Max',
        name='',
        description='Maximum Top Scale',
        default=[1.3, 1.3, 1.0], size=3, min=0)

    lp_Tree_Top_Subdivisions = IntProperty(
        attr='lp_Tree_Top_Subdivisions',
        name='Subdivisions',
        description='Tree Top Subdivisions',
        default=1, min=1)
    # Noise
    lp_Tree_Top_Strength_Min = FloatProperty(
        attr='lp_Tree_Top_Strength_Min',
        name='Min',
        description='Tree Top Strength',
        default=-1.8)

    lp_Tree_Top_Strength_Max = FloatProperty(
        attr='lp_Tree_Top_Strength_Max',
        name='Max',
        description='Tree Top Strength',
        default=-1.2)

    lp_Tree_Top_NScale_Min = FloatProperty(
        attr='lp_Tree_Top_NScale_Min',
        name='Min',
        description='Tree Top Noise Scale',
        default=0.25, min=0.0001)

    lp_Tree_Top_NScale_Max = FloatProperty(
        attr='lp_Tree_Top_NScale_Max',
        name='Max',
        description='Tree Top Noise Scale',
        default=0.25, min=0.0001)

    lp_Tree_Top_Weight1 = FloatProperty(
        attr='lp_Tree_Top_Weight1',
        name='1',
        description='Tree Top Weight 1',
        default=1, min=-2, max=2)

    lp_Tree_Top_Weight2 = FloatProperty(
        attr='lp_Tree_Top_Weight2',
        name='2',
        description='Tree Top Weight 2',
        default=0, min=-2, max=2)

    lp_Tree_Top_Weight3 = FloatProperty(
        attr='lp_Tree_Top_Weight3',
        name='3',
        description='Tree Top Weight 3',
        default=0, min=-2, max=2)
    # Pine
    lp_Tree_Top_Stage_Segments_Min = IntProperty(
        attr='lp_Tree_Top_Stage_Segments_Min',
        name='Min',
        description='Minimum Tree Top Stage Segments',
        default=6, min=3)

    lp_Tree_Top_Stage_Segments_Max = IntProperty(
        attr='lp_Tree_Top_Stage_Segments_Max',
        name='Max',
        description='Maximum Tree Top Stage Segments',
        default=7, min=3)

    lp_Tree_Top_Rotate_Stages = BoolProperty(
        attr='lp_Tree_Top_Rotate_Stages',
        name='Rotate Stages',
        description='Whether to rotate tree stages',
        default=False)

    lp_Tree_Top_Stages_Min = IntProperty(
        attr='lp_Tree_Top_Stages_Min',
        name='Min',
        description='Minimum Tree Top Stages',
        default=6, min=1)

    lp_Tree_Top_Stages_Max = IntProperty(
        attr='lp_Tree_Top_Stages_Max',
        name='Max',
        description='Maximum Tree Top Stages',
        default=7, min=1)

    lp_Tree_Top_Stage_Shrink = FloatProperty(
        attr='lp_Tree_Top_Stage_Shrink',
        name='Shrink Size',
        description='Tree Top Stage Shrink Size',
        default=0.09)

    lp_Tree_Top_Stage_Shrink_Multiplier = FloatProperty(
        attr='lp_Tree_Top_Stage_Shrink_Multiplier',
        name='Shrink Multiplier',
        description='Tree Top Stage Shrink Multiplier',
        default=1.0)

    lp_Tree_Top_Stage_Step_Min = FloatProperty(
        attr='lp_Tree_Top_Stage_Step_Min',
        name='Min',
        description='Tree Top Minimum Stage Step',
        default=0.35)

    lp_Tree_Top_Stage_Step_Max = FloatProperty(
        attr='lp_Tree_Top_Stage_Step_Max',
        name='Max',
        description='Tree Top Maximum Stage Step',
        default=0.37)

    lp_Tree_Top_Stage_Diameter = FloatProperty(
        attr='lp_Tree_Top_Stage_Diameter',
        name='Stage Diameter',
        description='Tree Top Stage Diameter Size',
        default=0.72)

    lp_Tree_Top_Stage_Size_Min = FloatVectorProperty(
        attr='lp_Tree_Top_Stage_Size_Min',
        name='',
        description='Tree Top Minimum Stage Size',
        default=[1.0, 1.0, 1.5], size=3, min=0)

    lp_Tree_Top_Stage_Size_Max = FloatVectorProperty(
        attr='lp_Tree_Top_Stage_Size_Max',
        name='',
        description='Tree Top Maximum Stage Size',
        default=[1.0, 1.0, 1.7], size=3, min=0)

    lp_Tree_Keep_Modifiers = BoolProperty(
        attr='lp_Tree_Keep_Modifiers',
        name='Keep Modifiers',
        description='Whether to apply modifiers or not',
        default=False)

    # Palm Top
    lp_Tree_Palm_Top_Coconuts_Min = IntProperty(
        attr='lp_Tree_Palm_Top_Coconuts_Min',
        name='Min',
        description='Minimum Tree Top Coconuts',
        default=1, min=0, max=4)

    lp_Tree_Palm_Top_Coconuts_Max = IntProperty(
        attr='lp_Tree_Palm_Top_Coconuts_Max',
        name='Max',
        description='Maximum Tree Top Coconuts',
        default=4, min=0, max=4)

    lp_Tree_Palm_Top_Leaves_Min = IntProperty(
        attr='lp_Tree_Palm_Top_Leaves_Min',
        name='Min',
        description='Minimum Tree Top Leaves',
        default=4, min=0)

    lp_Tree_Palm_Top_Leaves_Max = IntProperty(
        attr='lp_Tree_Palm_Top_Leaves_Max',
        name='Max',
        description='Maximum Tree Top Leaves',
        default=5, min=0)

    lp_Tree_Palm_Top_Leaf_Length_Min = IntProperty(
        attr='lp_Tree_Palm_Top_Leaf_Length_Min',
        name='Min',
        description='Minimum Tree Top Leaf Length',
        default=3, min=0)

    lp_Tree_Palm_Top_Leaf_Length_Max = IntProperty(
        attr='lp_Tree_Palm_Top_Leaf_Length_Max',
        name='Max',
        description='Maximum Tree Top Leaf Length',
        default=4, min=0)

    lp_Tree_Palm_Top_Leaf_Size_Min = FloatProperty(
        attr='lp_Tree_Palm_Top_Leaf_Size_Min',
        name='Min',
        description='Minimum Tree Top Leaf Size',
        default=0.3, min=0)

    lp_Tree_Palm_Top_Leaf_Size_Max = FloatProperty(
        attr='lp_Tree_Palm_Top_Leaf_Size_Max',
        name='Max',
        description='Maximum Tree Top Leaf Size',
        default=0.4, min=0)

    # Bush
    lp_Bush_Subdivisions = IntProperty(
        attr='lp_Bush_Subdivisions',
        name='Subdivisions',
        description='Bush Subdivisions',
        default=1, min=1)

    lp_Bush_Scale_Min = FloatVectorProperty(
        attr='lp_Bush_Scale_Min',
        name='',
        description='Minimum Scale',
        default=[0.8, 0.8, 1.0], size=3, min=0)

    lp_Bush_Scale_Max = FloatVectorProperty(
        attr='lp_Bush_Scale_Max',
        name='',
        description='Maximum Scale',
        default=[1.0, 1.0, 1.3], size=3, min=0)

    # Bush Noise
    lp_Bush_Strength_Min = FloatProperty(
        attr='lp_Bush_Strength_Min',
        name='Min',
        description='Bush Strength',
        default=-1.8)

    lp_Bush_Strength_Max = FloatProperty(
        attr='lp_Bush_Strength_Max',
        name='Max',
        description='Bush Strength',
        default=-1.2)

    lp_Bush_NScale_Min = FloatProperty(
        attr='lp_Bush_NScale_Min',
        name='Min',
        description='Bush Noise Scale',
        default=0.25, min=0.0001)

    lp_Bush_NScale_Max = FloatProperty(
        attr='lp_Bush_NScale_Max',
        name='Max',
        description='Bush Noise Scale',
        default=0.25, min=0.0001)

    lp_Bush_Weight1 = FloatProperty(
        attr='lp_Bush_Weight1',
        name='1',
        description='Bush Weight 1',
        default=1, min=-2, max=2)

    lp_Bush_Weight2 = FloatProperty(
        attr='lp_Bush_Weight2',
        name='2',
        description='Bush Weight 2',
        default=0, min=-2, max=2)

    lp_Bush_Weight3 = FloatProperty(
        attr='lp_Bush_Weight3',
        name='3',
        description='Bush Weight 3',
        default=0, min=-2, max=2)

    lp_Bush_Keep_Modifiers = BoolProperty(
        attr='lp_Bush_Keep_Modifiers',
        name='Keep Modifiers',
        description='Whether to apply modifiers or not',
        default=False)

    # Grass
    lp_Grass_Length_Min = IntProperty(
        attr='lp_Grass_Length_Min',
        name='Min',
        description='Minimum Grass Length',
        default=6, min=0)

    lp_Grass_Length_Max = IntProperty(
        attr='lp_Grass_Length_Max',
        name='Max',
        description='Maximum Grass Length',
        default=7, min=0)

    lp_Grass_Grow_Scale_Min = FloatProperty(
        attr='lp_Grass_Grow_Scale_Min',
        name='Min',
        description='Minimum Grow Scale',
        default=0.7)

    lp_Grass_Grow_Scale_Max = FloatProperty(
        attr='lp_Grass_Grow_Scale_Max',
        name='Max',
        description='Maximum Grow Scale',
        default=0.7)

    lp_Grass_Dir_Min = FloatVectorProperty(
        attr='lp_Grass_Dir_Min',
        name='',
        description='Minimum grow Direction',
        default=[0.007, 0, 0.2], size=3)

    lp_Grass_Dir_Max = FloatVectorProperty(
        attr='lp_Grass_Dir_Max',
        name='',
        description='Maximum Grow Direction',
        default=[0.009, 0, 0.25], size=3)

    lp_Grass_Scale_Min = FloatVectorProperty(
        attr='lp_Grass_Scale_Min',
        name='',
        description='Minimum Scale',
        default=[0.06, 0.02, 0.1], size=3, min=0)

    lp_Grass_Scale_Max = FloatVectorProperty(
        attr='lp_Grass_Scale_Max',
        name='',
        description='Maximum Scale',
        default=[0.06, 0.02, 0.1], size=3, min=0)

    lp_Grass_Keep_Modifiers = BoolProperty(
        attr='lp_Grass_Keep_Modifiers',
        name='Keep Modifiers',
        description='Whether to apply modifiers or not',
        default=False)

    # Cloud
    lp_Cloud_Subdivisions = IntProperty(
        attr='lp_Cloud_Subdivisions',
        name='Subdivisions',
        description='Cloud Subdivisions',
        default=1, min=1)

    lp_Cloud_Spheres_Min = IntProperty(
        attr='lp_Cloud_Spheres_Min',
        name='Min',
        description='Minimum Cloud Spheres',
        default=3, min=1)

    lp_Cloud_Spheres_Max = IntProperty(
        attr='lp_Cloud_Spheres_Max',
        name='Max',
        description='Minimum Cloud Spheres',
        default=6, min=1)

    lp_Cloud_Scale_Min = FloatVectorProperty(
        attr='lp_Cloud_Scale_Min',
        name='',
        description='Minimum Scale',
        default=[0.8, 0.8, 0.8], size=3, min=0)

    lp_Cloud_Scale_Max = FloatVectorProperty(
        attr='lp_Cloud_Scale_Max',
        name='',
        description='Maximum Scale',
        default=[1.4, 1.4, 1.4], size=3, min=0)

    lp_Cloud_Keep_Modifiers = BoolProperty(
        attr='lp_Cloud_Keep_Modifiers',
        name='Keep Modifiers',
        description='Whether to apply modifiers or not',
        default=False)

    # Terrain
    Terrain_Type_List = [
        ('lp_Terrain_Plane', 'Plane', 'Plane Terrain'),
        ('lp_Terrain_Sphere', 'Sphere', 'Sphere Terrain')]
    lp_Terrain_Type = EnumProperty(
        attr='lp_Terrain_Type',
        name='Type',
        description='Choose the terrain type',
        items=Terrain_Type_List, default='lp_Terrain_Plane')

    lp_Terrain_X_Segments = IntProperty(
        attr='lp_Terrain_X_Segments',
        name='X',
        description='Resolution along X axis',
        default=17, min=2)

    lp_Terrain_Y_Segments = IntProperty(
        attr='lp_Terrain_Y_Segments',
        name='Y',
        description='Resolution along Y axis',
        default=17, min=2)

    lp_Terrain_Subdivisions = IntProperty(
        attr='lp_Terrain_Subdivisions',
        name='Subdivisions',
        description='Terrain Resolution',
        default=4, min=1)

    lp_Terrain_Size = FloatProperty(
        attr='lp_Terrain_Size',
        name='Size',
        description='Terrain Size',
        default=8, min=0)

    Terrain_Displace_Type_List = [
        ('lp_Terrain_Displace_Voronoi', 'Voronoi', 'Voronoi Displace'),
        ('lp_Terrain_Displace_Clouds', 'Clouds', 'Clouds Displace')]
    lp_Terrain_Displace_Type = EnumProperty(
        attr='lp_Terrain_Displace_Type',
        name='Displace',
        description='Choose the terrain displace type',
        items=Terrain_Displace_Type_List, default='lp_Terrain_Displace_Clouds')

    lp_Terrain_Strength_Min = FloatProperty(
        attr='lp_Terrain_Strength_Min',
        name='Min',
        description='Terrain Strength',
        default=1)

    lp_Terrain_Strength_Max = FloatProperty(
        attr='lp_Terrain_Strength_Max',
        name='Max',
        description='Terrain Strength',
        default=1)

    lp_Terrain_Scale_Min = FloatProperty(
        attr='lp_Terrain_Scale_Min',
        name='Min',
        description='Terrain Scale',
        default=0.25, min=0.0001)

    lp_Terrain_Scale_Max = FloatProperty(
        attr='lp_Terrain_Scale_Max',
        name='Max',
        description='Terrain Scale',
        default=0.25, min=0.0001)

    lp_Terrain_Weight1 = FloatProperty(
        attr='lp_Terrain_Weight1',
        name='1',
        description='Terrain Weight 1',
        default=1, min=-2, max=2)

    lp_Terrain_Weight2 = FloatProperty(
        attr='lp_Terrain_Weight2',
        name='2',
        description='Terrain Weight 2',
        default=0, min=-2, max=2)

    lp_Terrain_Weight3 = FloatProperty(
        attr='lp_Terrain_Weight3',
        name='3',
        description='Terrain Weight 3',
        default=0, min=-2, max=2)

    lp_Terrain_Keep_Modifiers = BoolProperty(
        attr='lp_Terrain_Keep_Modifiers',
        name='Keep Modifiers',
        description='Whether to apply modifiers or not',
        default=False)

    # Water
    Water_Type_List = [
        ('lp_Water_Plane', 'Plane', 'Plane Water'),
        ('lp_Water_Sphere', 'Sphere', 'Sphere Water')]
    lp_Water_Type = EnumProperty(
        attr='lp_Water_Type',
        name='Type',
        description='Choose the water type',
        items=Water_Type_List, default='lp_Water_Plane')

    lp_Water_X_Segments = IntProperty(
        attr='lp_Water_X_Segments',
        name='X',
        description='Resolution along X axis',
        default=17)

    lp_Water_Y_Segments = IntProperty(
        attr='lp_Water_Y_Segments',
        name='Y',
        description='Resolution along Y axis',
        default=17)

    lp_Water_Subdivisions = IntProperty(
        attr='lp_Water_Subdivisions',
        name='Subdivisions',
        description='Water Resolution',
        default=4)

    lp_Water_Size = FloatProperty(
        attr='lp_Water_Size',
        name='Size',
        description='Water Size',
        default=8)

    lp_Water_Displace = BoolProperty(
        attr='lp_Water_Displace',
        name='Displace',
        description='Whether to displace water or not',
        default=True)

    lp_Water_Strength_Min = FloatProperty(
        attr='lp_Water_Strength_Min',
        name='Min',
        description='Water Strength',
        default=1.2)

    lp_Water_Strength_Max = FloatProperty(
        attr='lp_Water_Strength_Max',
        name='Max',
        description='Water Strength',
        default=1.8)

    lp_Water_Scale_Min = FloatProperty(
        attr='lp_Water_Scale_Min',
        name='Min',
        description='Water Scale',
        default=0.25, min=0.0001)

    lp_Water_Scale_Max = FloatProperty(
        attr='lp_Water_Scale_Max',
        name='Max',
        description='Water Scale',
        default=0.25, min=0.0001)

    lp_Water_Keep_Modifiers = BoolProperty(
        attr='lp_Water_Keep_Modifiers',
        name='Keep Modifiers',
        description='Whether to apply modifiers or not',
        default=False)
