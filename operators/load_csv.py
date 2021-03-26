import bpy
import os
import csv
from ..config import config


def upd_color_list(self, context):
    pcoll = config.icons_dict["thumbnail_previews"]
    my_props = context.scene.test_pg
    items = []
    my_icons = [ico for ico in config.icons_dict["thumbnail_previews"]]
    if __name__ == "__main__":
        script_path = bpy.context.space_data.text.filepath
        icons_dir = os.path.abspath(os.path.join(os.path.dirname(script_path), os.pardir, "images"))
    else:
        icons_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "images"))
    for i, item in enumerate(my_props.f_details):
        if 'desc' in item.keys():
            test_str = icons_dir + "\\" + item.id_name + "_" + item.desc + ".png"
        else:
            test_str = icons_dir + "\\" + item.id_name + "_" + item.id_name + ".png"
        if len(my_icons) > 0:
            try:
                my_icon = pcoll[test_str]
            except KeyError:
                my_icon = None
        else:
            my_icon = None
        if not my_icon:
            if 'desc' in item.keys():
                items.append((
                    str(item.id_name),
                    str(item.desc),
                    str(item.desc)
                    ))
            else:
                items.append((
                    str(item.id_name),
                    str(item.id_name),
                    str(item.id_name)
                    ))
        else:
            if 'desc' in item.keys():
                items.append((
                    str(item.id_name),
                    str(item.desc),
                    str(item.desc),
                    my_icon.icon_id,
                    i
                    ))
            else:
                items.append((
                    str(item.id_name),
                    str(item.id_name),
                    str(item.id_name),
                    my_icon.icon_id,
                    i
                    ))
    if len(items) == 0:
        items.append((
            "None",
            "None",
            "None"
        ))

    return items


def upd_color_list_cb(self, context):
    upd_color_list(self, context)
    return None

def load_csv(context):
    props = context.scene.test_pg
    props.f_details.clear()
    with open(props.ip_csv_fname, mode='r') as f:
        reader = csv.reader(f, delimiter=',')
        me_id = me_red = me_green = me_blue = me_alpha = me_hex = me_hue = me_sat = me_val = me_desc = None
        if [map for map in props.maplist if map.map_list == 'ID Name']:
            me_id = int([map for map in props.maplist if map.map_list == 'ID Name'][0].name)
        if [map for map in props.maplist if map.map_list == 'Red']:
            me_red = int([map for map in props.maplist if map.map_list == 'Red'][0].name)
        if [map for map in props.maplist if map.map_list == 'Green']:
            me_green = int([map for map in props.maplist if map.map_list == 'Green'][0].name)
        if [map for map in props.maplist if map.map_list == 'Blue']:
            me_blue = int([map for map in props.maplist if map.map_list == 'Blue'][0].name)
        if [map for map in props.maplist if map.map_list == 'Alpha']:
            me_alpha = int([map for map in props.maplist if map.map_list == 'Alpha'][0].name)
        if [map for map in props.maplist if map.map_list == 'Hexadecimal']:
            me_hex = int([map for map in props.maplist if map.map_list == 'Hexadecimal'][0].name)
        if [map for map in props.maplist if map.map_list == 'Hue']:
            me_hue = int([map for map in props.maplist if map.map_list == 'Hue'][0].name)
        if [map for map in props.maplist if map.map_list == 'Saturation']:
            me_sat = int([map for map in props.maplist if map.map_list == 'Saturation'][0].name)
        if [map for map in props.maplist if map.map_list == 'Value']:
            me_val = int([map for map in props.maplist if map.map_list == 'Value'][0].name)
        if [map for map in props.maplist if map.map_list == 'Description']:
            me_desc = int([map for map in props.maplist if map.map_list == 'Description'][0].name)
        next(reader)
        for row in reader:
            me = props.f_details.add()
            me.name = str(reader.line_num)
            if me_id != None:
                me.id_name = row[me_id]
                me.id_name = me.id_name.replace("\\", "")
                me.id_name = me.id_name.replace("/", "")
                me.id_name = me.id_name.replace("(", "")
                me.id_name = me.id_name.replace(")", "")
                me.id_name = me.id_name.replace("-", "")
                me.id_name = me.id_name.replace("&", "")
                me.name = me.id_name
            if me_red != None:
                me.red = row[me_red]
                me.red_scaled = float(me.red)/(props.maplist[me_red].scale)
            if me_green != None:
                me.green = row[me_green]
                me.green_scaled = float(me.green)/(props.maplist[me_green].scale)
            if me_blue != None:
                me.blue = row[me_blue]
                me.blue_scaled = float(me.blue)/(props.maplist[me_blue].scale)
            if me_alpha != None:
                me.alpha = row[me_alpha]
                me.alpha_scaled = float(me.alpha)/(props.maplist[me_alpha].scale)
            if me_hex != None:
                me.hex = row[me_hex]
                if me.hex.startswith("#"):
                    me.hex = me.hex[1:]
            if me_hue != None:
                me.hue = row[me_hue]
                me.hue_scaled = float(me.hue)/(props.maplist[me_hue].scale)
            if me_sat != None:
                me.sat = row[me_sat]
                me.sat_scaled = float(me.sat)/(props.maplist[me_sat].scale)
            if me_val != None:
                me.val = row[me_val]
                me.val_scaled = float(me.val)/(props.maplist[me_val].scale)
            if me_desc != None:
                me.desc = row[me_desc]


class TEST_OT_load_csv(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "file.load_csv"
    bl_label = "TEST_OT_load_csv"

    @classmethod
    def poll(cls, context):
        props = context.scene.test_pg
        cond1 = os.path.isfile(props.ip_csv_fname)
        id_used = [map for map in props.maplist if map.map_list == 'ID Name']
        cond2 = len(id_used) == 1
        return cond1 and cond2

    def execute(self, context):
        print(f"{self.bl_idname} pressed")
        props = context.scene.test_pg
        load_csv(context)
        upd_color_list_cb(self, context)
        if len(props.f_details) > 0:
            try:
                props.color_list = props.f_details[0].id_name
            except TypeError:
                pass
        return {'FINISHED'}



classes = [
    TEST_OT_load_csv,
    ]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()