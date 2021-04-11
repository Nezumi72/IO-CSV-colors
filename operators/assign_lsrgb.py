import bpy
import colorsys


def srgb_to_linsrgb(srgb):
    if srgb >= 0.04045:
        return ((srgb+0.055)/1.055)**2.4
    else:
        return (srgb/12.92)


class MATERIAL_OT_assign_lsrgb(bpy.types.Operator):
    bl_idname = "material.assign_lsrgb"
    bl_label = "Add selected to material input"

    mat: bpy.props.StringProperty(
        name="mat_name",
        default="Material",
    )
    node: bpy.props.StringProperty(
        name="node_name",
        default="",
    )
    ipname: bpy.props.StringProperty(
        name="ipname",
        default="",
    )

    @classmethod
    def poll(cls, context):
        my_props = context.scene.test_pg
        ob = context.object
        if ob:
            cond1 = True
        else:
            cond1 = False
        return cond1

    def execute(self, context):
        print(f"{self.bl_idname} pressed")
        my_props = context.scene.test_pg
        my_mat = bpy.data.materials[self.mat]
        my_node = my_mat.node_tree.nodes[self.node]
        my_ip = my_node.inputs[self.ipname]
        me = my_props.f_details[my_props.color_list]
        # material colors seem to want linear color data
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
        my_ip.default_value = (r, g, b, 1.0)
        return {'FINISHED'}


classes = [
    MATERIAL_OT_assign_lsrgb,
    ]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
