import bpy
from . import img_loader
from . import operators


class OBJECT_PT_structured(bpy.types.Panel):
    """Custom Blender panel that allows the user to speed up
    the process of creating a synchronized flight plan.
    """

    bl_idname = "OBJECT_PT_stan_syncflight_panel"
    bl_label = "Sync Flt Tools"

    # The following three settings determine that the Synchronized Flight panel gets
    # added to the sidebar of the 3D view
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'Synchronized Flight'


    def draw(self, context):
        layout = self.layout
        icons = img_loader.get_icons_collection()

        layout.operator(operators.STAN_TEST.bl_idname)

        row = layout.row(align=True)
        row.label(text="Scene Objects", icon_value=icons['pack_64'].icon_id)
        row.label(text="", icon_value=icons["smile_64"].icon_id)

        grid = layout.grid_flow(columns=2, row_major=True)        
        add_on = context.preferences.addons[__package__]
        preferences = add_on.preferences

        for i, ob in enumerate(context.scene.objects):
            if i >= preferences.max_objects:
                grid.label(text="...")
                break

            grid.label(text=ob.name, icon=f'OUTLINER_OB_{ob.type}')
        
        layout.operator(operators.TRANSFORM_OT_random_location.bl_idname)
    


def register_classes():
    bpy.utils.register_class(OBJECT_PT_structured)


def unregister_classes():
    bpy.utils.unregister_class(OBJECT_PT_structured)