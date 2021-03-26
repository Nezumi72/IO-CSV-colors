import bpy
import os
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
            except ValueError:
                my_icon = None
            except IndexError:
                my_icon = None
            except TypeError:
                my_icon = None
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
    return items


def upd_color_list_cb(self, context):
    upd_color_list(self, context)
    return None


def add_palette(self, context):
    my_props = context.scene.test_pg
    if self.palette not in bpy.data.palettes:
        bpy.data.palettes.new(self.palette)


class TEST_PG_headers(bpy.types.PropertyGroup):
    header: bpy.props.StringProperty(
        name="header",
        description="Header",
        default="",
        )
    sample: bpy.props.StringProperty(
        name="sample",
        description="Sample",
        default="",
        )


class TEST_PG_maplist(bpy.types.PropertyGroup):
    map_list: bpy.props.EnumProperty(
        items=(
            ("ID Name", "ID Name", "ID Name"),
            ("Red", "Red", "Red"),
            ("Green", "Green", "Green"),
            ("Blue", "Blue", "Blue"),
            ("Alpha", "Alpha", "Alpha"),
            ("Hexadecimal", "Hexadecimal", "Hexadecimal"),
            ("Hue", "Hue", "Hue"),
            ("Saturation", "Saturation", "Saturation"),
            ("Value", "Value", "Value"),
            ("Description", "Description", "Description"),
            ("None", "None", "None"),
            ),
        name="map_list",
        default="None",
        )
    scale:bpy.props.IntProperty(
        name="Scale",
        description="Scaling factor data/scale should be 0.0-1.0 range",
        min=1,
        max=360,
        default=1,
        )
    include_flag:bpy.props.BoolProperty(
        name="include_flag",
        description="Include in output CSV",
        default=False,
        ) 


class TEST_PG_details(bpy.types.PropertyGroup):
    id_name: bpy.props.StringProperty(
        name="ID Name",
        description="Unique Name",
        default="",
        )
    red: bpy.props.StringProperty(
        name="Red",
        description="RGB - Red value",
        default="",
        )
    red_scaled: bpy.props.FloatProperty(
        name="Red Scaled",
        description="Import Value Scaled 0-1.0 float",
        min=0.0,
        max=1.0,
        )
    green: bpy.props.StringProperty(
        name="Green",
        description="RGB - Green value",
        default="",
        )
    green_scaled: bpy.props.FloatProperty(
        name="Green Scaled",
        description="Import Value Scaled 0-1.0 float",
        min=0.0,
        max=1.0,
        )
    blue: bpy.props.StringProperty(
        name="Blue",
        description="RGB - Blue value",
        default="",
        )
    blue_scaled: bpy.props.FloatProperty(
        name="Blue Scaled",
        description="Import Value Scaled 0-1.0 float",
        min=0.0,
        max=1.0,
        )
    alpha: bpy.props.StringProperty(
        name="Alpha",
        description="Alpha value",
        default="",
        )
    alpha_scaled: bpy.props.FloatProperty(
        name="Alpha Scaled",
        description="Import Value Scaled 0-1.0 float",
        min=0.0,
        max=1.0,
        )
    hex: bpy.props.StringProperty(
        name="Hexadecimal",
        description="Hexadecimal value",
        default="",
        )
    hue: bpy.props.StringProperty(
        name="Hue",
        description="HSV - Hue",
        default="",
        )
    hue_scaled: bpy.props.FloatProperty(
        name="Hue Scaled",
        description="Import Value Scaled 0-1.0 float",
        min=0.0,
        max=1.0,
        )
    sat: bpy.props.StringProperty(
        name="Saturation",
        description="HSV - Saturation",
        default="",
        )
    sat_scaled: bpy.props.FloatProperty(
        name="Saturation Scaled",
        description="Import Value Scaled 0-1.0 float",
        min=0.0,
        max=1.0,
        )
    val: bpy.props.StringProperty(
        name="Value",
        description="HSV - Value",
        default="",
        )
    val_scaled: bpy.props.FloatProperty(
        name="Value Scaled",
        description="Import Value Scaled 0-1.0 float",
        min=0.0,
        max=1.0,
        )
    desc: bpy.props.StringProperty(
        name="Description",
        description="Generic description",
        default="",
        )


class TEST_PG_props(bpy.types.PropertyGroup):
    ip_csv_fname: bpy.props.StringProperty(
        name="IP CSV file",
        description="CSV file",
        default=os.path.join(os.path.dirname(__file__), os.pardir, "sample data", "IP_RAL_colors.csv"),
        subtype='FILE_PATH',
        )
    f_headers: bpy.props.CollectionProperty(
        type=TEST_PG_headers)
    maplist: bpy.props.CollectionProperty(
        type=TEST_PG_maplist)
    f_details: bpy.props.CollectionProperty(
        type=TEST_PG_details)
    op_csv_dir: bpy.props.StringProperty(
        name="OP CSV dir",
        description="OP CSV dir",
        default=os.path.join(os.path.dirname(__file__), os.pardir, "sample data"),
        subtype='DIR_PATH',
        )
    op_csv_fname: bpy.props.StringProperty(
        name="OP CSV file name",
        description="OP CSV file name",
        default="OP_RAL_colors.csv",
        )
    icons_dir: bpy.props.StringProperty(
        name="Icons Directory",
        description="Icons Directory",
        default=os.path.join(os.path.dirname(__file__), os.pardir, "images"),
        subtype='DIR_PATH',
        )
    icon_size: bpy.props.IntProperty(
        name="Icons Size",
        description="Pixel size",
        default=16,
        min=1,
        soft_max=32,
        )
    color_list: bpy.props.EnumProperty(
        items=upd_color_list,
        )
    palette: bpy.props.StringProperty(
        name="Palette:",
        description="Palette to add color",
        default='test_palette',
        update=add_palette,
        )
    palette_columns: bpy.props.IntProperty(
        name="Palette Columns",
        description="Number of columns before repeating row",
        default=4,
        min=1,
        soft_max=10,
        )

classes = [
    TEST_PG_headers,
    TEST_PG_details,
    TEST_PG_maplist,
    TEST_PG_props,
    ]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.test_pg = bpy.props.PointerProperty(
        type=TEST_PG_props)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.test_pg


if __name__ == "__main__":
    register()