import bpy
import colorsys


def srgb_to_linsrgb(srgb):
    if srgb >= 0.04045:
        return ((srgb+0.055)/1.055)**2.4
    else:
        return (srgb/12.92)


class OBJECT_OT_apply_to_vp_obj(bpy.types.Operator):
    bl_idname = "object.obj_vp_color"
    bl_label = "Apply color to obj viewport color"

    @classmethod
    def poll(cls, context):
        my_props = context.scene.test_pg
        cond1 = context.view_layer.objects.active
        cond2 = context.object.type == 'MESH'
        cond3 = my_props.color_list
        return cond1 and cond2 and cond3

    def execute(self, context):
        print(f"{self.bl_idname} pressed")
        my_props = context.scene.test_pg
        obj = context.view_layer.objects.active
        me = my_props.f_details[my_props.color_list]
        # these need to be gamma corrected to linear
        if 'red_scaled' in me.keys():
            r = me.red_scaled
            g = me.green_scaled
            b = me.blue_scaled
        if 'hue_scaled' in me.keys():
            r, g, b = colorsys.hsv_to_rgb(
                me.hue_scaled,
                me.sat_scaled,
                me.val_scaled
                )
        if 'hex' in me.keys():
            r, g, b = tuple(int(me.hex[i:i+2], 16) for i in (0, 2, 4))
            r = float(r)/255.0
            g = float(g)/255.0
            b = float(b)/255.0
        r = srgb_to_linsrgb(r)
        g = srgb_to_linsrgb(g)
        b = srgb_to_linsrgb(b)
        obj.color[0] = r
        obj.color[1] = g
        obj.color[2] = b
        return {'FINISHED'}


classes = [
    OBJECT_OT_apply_to_vp_obj,
    ]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
