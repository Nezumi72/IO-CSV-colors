import bpy
import colorsys


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
        if 'hue_scaled' in me.keys():
            my_red, my_green, my_blue = colorsys.hsv_to_rgb(me.hue_scaled, me.sat_scaled, me.val_scaled)
            obj.color[0] = my_red
            obj.color[1] = my_green
            obj.color[2] = my_blue
        if 'hex' in me.keys():
            r, g, b = tuple(int(me.hex[i:i+2], 16) for i in (0, 2, 4))
            obj.color[0] = float(r)/255.0
            obj.color[1] = float(g)/255.0
            obj.color[2] = float(b)/255.0
        if 'red_scaled' in me.keys():
            obj.color[0] = me.red_scaled
            obj.color[1] = me.green_scaled
            obj.color[2] = me.blue_scaled
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