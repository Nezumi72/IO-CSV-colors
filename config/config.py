import bpy
import os
import bpy.utils.previews


icons_dict = {}


def generate_previews():
    global icons_dict
    pcoll = icons_dict["thumbnail_previews"]
    image_location = pcoll.images_location
    enum_items = []
    for i, image in enumerate(os.listdir(image_location)):
        if image.endswith('.png'):
            filepath = os.path.join(image_location, image)
            try:
                thumb = pcoll.load(filepath, filepath, 'IMAGE')
                enum_items.append(
                    (image_location, image, "", thumb.icon_id, i)
                    )
            except KeyError:
                pass
    return enum_items


def register():
    global icons_dict
    pcoll = bpy.utils.previews.new()
    if __name__ == "__main__":
        script_path = bpy.context.space_data.text.filepath
        icons_dir = os.path.abspath(os.path.join(os.path.dirname(script_path), "images"))
    else:
        icons_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "images"))
    pcoll.images_location = icons_dir
    icons_dict["thumbnail_previews"] = pcoll
    bpy.types.Scene.my_thumbnails = bpy.props.EnumProperty(
        items=generate_previews(),
        )


def unregister():
    global icons_dict
    for pcoll in icons_dict.values():
        bpy.utils.previews.remove(pcoll)
    icons_dict.clear()
    del bpy.types.Scene.my_thumbnails
