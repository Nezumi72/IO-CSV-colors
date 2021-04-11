import bpy
import colorsys


class PALETTE_OT_add_color(bpy.types.Operator):
    bl_idname = "palette.add_color"
    bl_label = "Add selected to color palette"

    @classmethod
    def poll(cls, context):
        my_props = context.scene.test_pg
        try:
            cond1 = bpy.data.palettes[my_props.palette]
        except KeyError:
            cond1 = False
        cond2 = context.scene.test_pg.color_list
        return cond1 and cond2

    def execute(self, context):
        print(f"{self.bl_idname} pressed")
        my_props = context.scene.test_pg
        pal = bpy.data.palettes[my_props.palette].colors.new()
        me = my_props.f_details[my_props.color_list]
        # palette colors seem to want non linear color data
        if 'red_scaled' in me.keys():
            pal.color[0] = me.red_scaled
            pal.color[1] = me.green_scaled
            pal.color[2] = me.blue_scaled
        if 'hue_scaled' in me.keys():
            r, g, b = colorsys.hsv_to_rgb(
                me.hue_scaled,
                me.sat_scaled,
                me.val_scaled
                )
            pal.color[0] = r
            pal.color[1] = g
            pal.color[2] = b
        if 'hex' in me.keys():
            r, g, b = tuple(int(me.hex[i:i+2], 16) for i in (0, 2, 4))
            pal.color[0] = float(r)/255.0
            pal.color[1] = float(g)/255.0
            pal.color[2] = float(b)/255.0
        return {'FINISHED'}


classes = [
    PALETTE_OT_add_color,
    ]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
