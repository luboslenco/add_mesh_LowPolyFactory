import bpy
from random import seed, uniform


def get_theme():
    prefs = bpy.context.user_preferences.addons[__package__].preferences
    return prefs.lp_Theme_Type


def get_terrain_colors(theme=None):
    if theme is None:
        theme = get_theme()

    if theme == 'lp_Theme_Autumn':
        return [0.216, 0.509, 0.144, 1.0], [0.216, 0.509, 0.144, 1.0]
    elif theme == 'lp_Theme_Winter':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Tropic':
        return [1, 0.695, 0.613, 1], [1, 0.662, 0.219, 1]
    elif theme == 'lp_Theme_Spring':
        return [0.216, 0.509, 0.144, 1.0], [0.216, 0.509, 0.144, 1.0]
    elif theme == 'lp_Theme_Summer':
        return [0.216, 0.509, 0.144, 1.0], [0.216, 0.509, 0.144, 1.0]


def get_bush_colors(theme=None):
    if theme is None:
        theme = get_theme()

    if theme == 'lp_Theme_Autumn':
        return [0.07, 0.7, 0.06, 1.0], [0.07, 0.7, 0.06, 1.0]
    elif theme == 'lp_Theme_Winter':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Tropic':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Spring':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Summer':
        return [1, 1, 1, 1], [1, 1, 1, 1]


def get_grass_colors(theme=None):
    if theme is None:
        theme = get_theme()

    if theme == 'lp_Theme_Autumn':
        return [0.07, 0.7, 0.06, 1.0], [0.07, 0.7, 0.06, 1.0]
    elif theme == 'lp_Theme_Winter':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Tropic':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Spring':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Summer':
        return [1, 1, 1, 1], [1, 1, 1, 1]


def get_cloud_colors(theme=None):
    if theme is None:
        theme = get_theme()

    if theme == 'lp_Theme_Autumn':
        return [0.8, 0.85, 1.0, 1.0], [0.8, 0.85, 1.0, 1.0]
    elif theme == 'lp_Theme_Winter':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Tropic':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Spring':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Summer':
        return [1, 1, 1, 1], [1, 1, 1, 1]


def get_rock_colors(theme=None):
    if theme is None:
        theme = get_theme()

    if theme == 'lp_Theme_Autumn':
        return [0.8, 0.7, 0.8, 1.0], [0.8, 0.7, 0.8, 1.0]
    elif theme == 'lp_Theme_Winter':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Tropic':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Spring':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Summer':
        return [1, 1, 1, 1], [1, 1, 1, 1]


def get_tree_trunk_colors(theme=None):
    if theme is None:
        theme = get_theme()

    if theme == 'lp_Theme_Autumn':
        return [0.02, 0.05, 0.012, 1.0], [0.02, 0.05, 0.012, 1.0]
    elif theme == 'lp_Theme_Winter':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Tropic':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Spring':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Summer':
        return [1, 1, 1, 1], [1, 1, 1, 1]


def get_tree_trunk_palm_colors(theme=None):
    if theme is None:
        theme = get_theme()

    if theme == 'lp_Theme_Autumn':
        return [0.266, 0.09, 0.05, 1.0], [0.266, 0.09, 0.05, 1.0]
    elif theme == 'lp_Theme_Winter':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Tropic':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Spring':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Summer':
        return [1, 1, 1, 1], [1, 1, 1, 1]


def get_tree_top_oak_colors(theme=None):
    if theme is None:
        theme = get_theme()

    if theme == 'lp_Theme_Autumn':
        return [1.0, 0.07, 0.05, 1.0], [0.79, 0.672, 0.05, 1.0]
    elif theme == 'lp_Theme_Winter':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Tropic':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Spring':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Summer':
        return [1, 1, 1, 1], [1, 1, 1, 1]


def get_tree_top_pine_colors(theme=None):
    if theme is None:
        theme = get_theme()

    if theme == 'lp_Theme_Autumn':
        return [0.200, 0.444, 0.444, 1.0], [0.0, 0.420, 0.420, 1.0]
    elif theme == 'lp_Theme_Winter':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Tropic':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Spring':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Summer':
        return [1, 1, 1, 1], [1, 1, 1, 1]


def get_tree_top_palm_colors(theme=None):
    if theme is None:
        theme = get_theme()

    if theme == 'lp_Theme_Autumn':
        return [0.112, 0.342, 0.0, 1.0], [0.132, 0.362, 0.0, 1.0]
    elif theme == 'lp_Theme_Winter':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Tropic':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Spring':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Summer':
        return [1, 1, 1, 1], [1, 1, 1, 1]


def get_tree_coconut_colors(theme=None):
    if theme is None:
        theme = get_theme()

    if theme == 'lp_Theme_Autumn':
        return [0.156, 0.067, 0.0, 1.0], [0.156, 0.067, 0.0, 1.0]
    elif theme == 'lp_Theme_Winter':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Tropic':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Spring':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Summer':
        return [1, 1, 1, 1], [1, 1, 1, 1]


def get_water_colors(theme=None):
    if theme is None:
        theme = get_theme()

    if theme == 'lp_Theme_Autumn':
        return [0.4, 0.7, 1.0, 1.0], [0.4, 0.7, 1.0, 1.0]
    elif theme == 'lp_Theme_Winter':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Tropic':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Spring':
        return [1, 1, 1, 1], [1, 1, 1, 1]
    elif theme == 'lp_Theme_Summer':
        return [1, 1, 1, 1], [1, 1, 1, 1]
