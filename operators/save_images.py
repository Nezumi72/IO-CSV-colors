import bpy
import os
import colorsys
from ..config import config


def gen_images(context):
    props = context.scene.test_pg
    me_id = me_red = me_green = me_blue = me_alpha = me_hex = me_hue = me_sat = me_val = me_desc = None
    if [map for map in props.maplist if map.map_list == 'Red']:
        me_red = int([map for map in props.maplist if map.map_list == 'Red'][0].name)
    if [map for map in props.maplist if map.map_list == 'Green']:
        me_green = int([map for map in props.maplist if map.map_list == 'Green'][0].name)
    if [map for map in props.maplist if map.map_list == 'Blue']:
        me_blue = int([map for map in props.maplist if map.map_list == 'Blue'][0].name)
    if [map for map in props.maplist if map.map_list == 'Alpha']:
        me_alpha = int([map for map in props.maplist if map.map_list == 'Alpha'][0].name)
    if [map for map in props.maplist if map.map_list == 'Hue']:
        me_hue = int([map for map in props.maplist if map.map_list == 'Hue'][0].name)
    if [map for map in props.maplist if map.map_list == 'Saturation']:
        me_sat = int([map for map in props.maplist if map.map_list == 'Saturation'][0].name)
    if [map for map in props.maplist if map.map_list == 'Value']:
        me_val = int([map for map in props.maplist if map.map_list == 'Value'][0].name)
    for i, items in enumerate(props.f_details):
        my_id = my_red = my_green = my_blue = my_alpha = my_hex = my_hue = my_sat = my_val = my_desc = None
        if 'id_name' in items.keys():
            if items.id_name != "":
                my_id = items.id_name
        if 'red' in items.keys():
            if items.red != "":
                try:
                    my_red = float(items.red)/float(props.maplist[me_red].scale)
                except ValueError:
                    pass
        if 'green' in items.keys():
            if items.green != "":
                try:
                    my_green = float(items.green)/float(props.maplist[me_green].scale)
                except ValueError:
                    pass
        if 'blue' in items.keys():
            if items.blue != "":
                try:
                    my_blue = float(items.blue)/float(props.maplist[me_blue].scale)
                except ValueError:
                    pass
        if 'alpha' in items.keys():
            if items.alpha != "":
                try:
                    my_alpha = float(items.alpha)/float(props.maplist[me_alpha].scale)
                except ValueError:
                    pass
        if 'hex' in items.keys():
            if items.hex != "":
                my_hex = items.hex
                if my_hex.startswith("#"):
                    my_hex = my_hex[1:]
        if 'hue' in items.keys():
            if items.hue != "":
                try:
                    my_hue = float(items.hue)/float(props.maplist[me_hue].scale)
                except ValueError:
                    pass
        if 'sat' in items.keys():
            if items.sat != "":
                try:
                    my_sat = float(items.sat)/float(props.maplist[me_sat].scale)
                except ValueError:
                    pass
        if 'val' in items.keys():
            if items.val != "":
                try:
                    my_val = float(items.val)/float(props.maplist[me_val].scale)
                except ValueError:
                    pass
        if 'desc' in items.keys():
            if items.desc != "":
                my_desc = items.desc
        if my_desc:
            img_name = f"{my_id}_{my_desc}"
        else:
            img_name = f"{my_id}_{my_id}"
        if img_name not in bpy.data.images:
            img = bpy.data.images.new(img_name, width=props.icon_size, height=props.icon_size, alpha=True)
        else:
            img = bpy.data.images[img_name]
            bpy.data.images.remove(img)
            img = bpy.data.images.new(img_name, width=props.icon_size, height=props.icon_size, alpha=True)
        if not my_alpha:
            my_alpha = 1.0
        if my_hue and my_sat and my_val:
            my_red, my_green, my_blue = colorsys.hsv_to_rgb(my_hue, my_sat, my_val)
        if my_hex:
            r, g, b = tuple(int(my_hex[i:i+2], 16) for i in (0, 2, 4))
            my_red = float(r)/255.0
            my_green = float(g)/255.0
            my_blue = float(b)/255.0
        img.generated_color = (my_red, my_green, my_blue, my_alpha)


def save_icons(context):
    props = context.scene.test_pg
    gen_images(context)
    icon_names = []
    for i, items in enumerate(props.f_details):
        if 'desc' in items.keys():
            if items.desc != "":
                icon_names.append(f"{items.id_name}_{items.desc}")
            else:
                icon_names.append(f"{items.id_name}_{items.id_name}")
        else:
            icon_names.append(f"{items.id_name}_{items.id_name}")
    for img in bpy.data.images:
        my_icons_dir = props.icons_dir
        if img.name in icon_names:
            img.save_render(os.path.join(my_icons_dir, f"{img.name}.png"))
            # print(f"{img.name}.png\tsaved")
            

class TEST_OT_save_icons(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "file.save_icons"
    bl_label = "TEST_OT_save_icons"

    @classmethod
    def poll(cls, context):
        props = context.scene.test_pg
        cond1 = os.path.isdir(props.icons_dir)
        cond2 = cond3 = cond4 = False
        for i, items in enumerate(props.f_details):
            rgb_r = rgb_g = rgb_b = False
            if 'red' in items.keys():
                if items.red != "":
                    rgb_r = True
            if 'green' in items.keys():
                if items.green != "":
                    rgb_g = True
            if 'blue' in items.keys():
                if items.blue != "":
                    rgb_b = True
            cond2 = rgb_r and rgb_g and rgb_b
            hsv_h = hsv_s = hsv_v = False
            if 'hue' in items.keys():
                if items.hue != "":
                    hsv_h = True
            if 'sat' in items.keys():
                if items.sat != "":
                    hsv_s = True
            if 'val' in items.keys():
                if items.val != "":
                    hsv_v = True
            cond3 = hsv_h and hsv_s and hsv_v
            hex_h = False
            if 'hex' in items.keys():
                if items.hex != "":
                    hex_h = True
            cond4 = hex_h
        return cond1 and (cond2 or cond3 or cond4)

    def execute(self, context):
        print(f"{self.bl_idname} pressed")
        save_icons(context)
        config.generate_previews()
        return {'FINISHED'}


classes = [
    TEST_OT_save_icons,
    ]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()