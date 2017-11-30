import bpy
import bmesh
from mathutils import Matrix
from mathutils import Euler
from math import radians
from random import seed, uniform, randint


def get_voronoi_texture(context, name, scale=(0.25, 0.25),
                        weight1=(1.0, 1.0), weight2=(0, 0), weight3=(0, 0)):
    # if not 'cached_voronoi' in locals():
    #   cached_voronoi = None
    # if cached_voronoi != None:
    #   return cached_voronoi

    tex = context.blend_data.textures.new(name, 'VORONOI')
    tex.noise_scale = uniform(scale[0], scale[1])
    tex.noise_intensity = uniform(1.0, 1.0)
    tex.contrast = 1.0
    tex.weight_1 = uniform(weight1[0], weight1[1])
    tex.weight_2 = uniform(weight2[0], weight2[1])
    tex.weight_3 = uniform(weight3[0], weight3[1])
    tex.weight_4 = uniform(0, 0)
    tex.use_color_ramp = True

    ramp = tex.color_ramp
    ramp.interpolation = 'B_SPLINE'
    ramp.elements[0].color = (0.0, 0.0, 0.0, 1.0)
    ramp.elements[0].position = 0.5

    # cached_voronoi = tex
    return tex


def get_clouds_texture(context, name, scale=(0.25, 0.25)):
    tex = context.blend_data.textures.new(name, 'CLOUDS')
    tex.noise_scale = uniform(scale[0], scale[1])
    return tex


def get_material(context, material_name, colors_from, colors_to):
    if context.scene.render.engine != 'CYCLES':
        context.scene.render.engine = 'CYCLES'

    if bpy.data.materials.get(material_name) is not None:
        bmaterial = bpy.data.materials[material_name]
    else:
        bmaterial = bpy.data.materials.new(name=material_name)
        bmaterial.use_nodes = True
        nodes = bmaterial.node_tree.nodes
        links = bmaterial.node_tree.links

        # Clear default nodes
        for n in nodes:
            nodes.remove(n)

        out_node = nodes.new('ShaderNodeOutputMaterial')
        out_node.location = 0, 0

        bsdf_node = nodes.new('ShaderNodeBsdfDiffuse')
        bsdf_node.location = -250, 0
        links.new(bsdf_node.outputs[0], out_node.inputs[0])

        cr_node = nodes.new('ShaderNodeValToRGB')
        cr_node.location = bsdf_node.location.x - 300, bsdf_node.location.y
        cr_node.color_ramp.elements[0].color = colors_from
        cr_node.color_ramp.elements[1].color = colors_to
        links.new(cr_node.outputs[0], bsdf_node.inputs[0])

        oi_node = nodes.new('ShaderNodeObjectInfo')
        oi_node.location = cr_node.location.x - 200, cr_node.location.y
        links.new(oi_node.outputs[3], cr_node.inputs[0])

    return bmaterial


def get_material_water(context, material_name, colors_from, colors_to):
    if context.scene.render.engine != 'CYCLES':
        context.scene.render.engine = 'CYCLES'

    if bpy.data.materials.get(material_name) is not None:
        bmaterial = bpy.data.materials[material_name]
    else:
        bmaterial = bpy.data.materials.new(name=material_name)
        bmaterial.use_nodes = True
        nodes = bmaterial.node_tree.nodes
        links = bmaterial.node_tree.links

        for n in nodes:
            nodes.remove(n)

        out_node = nodes.new('ShaderNodeOutputMaterial')
        out_node.location = 0, 0

        mix1_node = nodes.new('ShaderNodeMixShader')
        mix1_node.location = -250, 0
        mix1_node.inputs[0].default_value = 0.7
        links.new(mix1_node.outputs[0], out_node.inputs[0])

        diffuse_node = nodes.new('ShaderNodeBsdfDiffuse')
        diffuse_node.location = -500, 0
        diffuse_node.inputs[0].default_value = colors_from
        links.new(diffuse_node.outputs[0], mix1_node.inputs[1])

        mix2_node = nodes.new('ShaderNodeMixShader')
        mix2_node.location = -500, -250
        mix2_node.inputs[0].default_value = 0.5
        links.new(mix2_node.outputs[0], mix1_node.inputs[2])

        transp_node = nodes.new('ShaderNodeBsdfTransparent')
        transp_node.location = -750, -250
        links.new(transp_node.outputs[0], mix2_node.inputs[1])

        glass_node = nodes.new('ShaderNodeBsdfGlass')
        glass_node.location = -750, -500
        glass_node.inputs[2].default_value = 1.333
        links.new(glass_node.outputs[0], mix2_node.inputs[2])

    return bmaterial


def create_object(context, object_name, mesh, material):
    bobject = context.blend_data.objects.new(object_name, mesh)
    bobject.show_all_edges = True

    context.scene.objects.link(bobject)
    context.scene.objects.active = bobject

    if len(bobject.data.materials):
        bobject.data.materials[0] = material
    else:
        bobject.data.materials.append(material)

    return bobject


def get_name_number(name):
    dot_index = name.rfind('.')
    if dot_index != -1:
        return name[dot_index:]
    else:
        return ''


def apply_displacement(context, bobject, direction='NORMAL',
                       disptype='lp_Terrain_Displace_Clouds',
                       strength=(-1.8, -1.2),
                       scale=(0.25, 0.25),
                       weight1=(1.0, 1.0),
                       weight2=(0, 0),
                       weight3=(0, 0)):
    number = get_name_number(bobject.name)
    noise_origin = context.blend_data.objects.new(
        bobject.name + "Origin" + number, None)
    noise_origin.location = [
        uniform(-100, 100.0),
        uniform(-100, 100.0),
        uniform(-100, 100.0)]
    context.scene.objects.link(noise_origin)

    disp = bobject.modifiers.new('displace', 'DISPLACE')
    disp.direction = direction
    disp.mid_level = 0.5
    disp.strength = uniform(strength[0], strength[1])
    disp.texture_coords = 'OBJECT'
    disp.texture_coords_object = noise_origin
    if disptype == 'lp_Terrain_Displace_Clouds':
        disp.texture = get_clouds_texture(
            context, bobject.name + "Texture" + number, scale=scale)
    else:
        disp.texture = get_voronoi_texture(
            context, bobject.name + "Texture" + number,
            scale=scale, weight1=weight1, weight2=weight2, weight3=weight3)

    return noise_origin


def get_random(min_val, max_val):
    try:
        result = randint(min_val, max_val)
    except Exception as e:
        result = min_val
    return result


def lerp(t, val_a, val_b):
    return (1 - t) * val_a + t * val_b


def make_vertex_colors(mesh, colors_from, colors_to, prefs):
    if prefs.lp_Populate_VCols is False:
        return

    if not mesh.vertex_colors:
        mesh.vertex_colors.new()

    # color_layer = mesh.vertex_colors[0]
    color_layer = mesh.vertex_colors.active
    t = uniform(0, 1)
    col = (
        lerp(t, colors_to[0], colors_from[0]) ** (1.0 / 2.2),
        lerp(t, colors_to[1], colors_from[1]) ** (1.0 / 2.2),
        lerp(t, colors_to[2], colors_from[2]) ** (1.0 / 2.2))

    i = 0
    for poly in mesh.polygons:
        for idx in poly.loop_indices:
            color_layer.data[i].color = col
            i += 1
