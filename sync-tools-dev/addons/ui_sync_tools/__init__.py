
bl_info = {
    "name": "Synchronized Flight Tools",
    "author": "Stan Humphries",
    "version": (0, 1),
    "blender": (3, 3, 0),
    "description": "Tools to speed up creating flight plans for synchronized flight using Skybrush Blender Studio.",
    "category": "Interface",
}


from . import operators
from . import img_loader
from . import panel
from . import preferences
from . import _refresh_
_refresh_.reload_modules()


def register():
    preferences.register_classes()
    operators.register_classes()
    img_loader.register_icons()
    panel.register_classes()


def unregister():
    panel.unregister_classes()
    img_loader.unregister_icons()
    operators.unregister_classes()
    preferences.unregister_classes()