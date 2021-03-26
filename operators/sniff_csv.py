import bpy
import os
import csv


def sniff_csv(context):
    props = context.scene.test_pg
    props.f_headers.clear()
    props.maplist.clear()
    with open(props.ip_csv_fname, mode='r') as f:
        reader = csv.DictReader(f, delimiter=',')
        for i, field in enumerate(reader.fieldnames):
            h = props.f_headers.add()
            h.name = str(i)
            map = props.maplist.add()
            map.name = str(i)
            props.f_headers[i].header = field
    with open(props.ip_csv_fname, mode='r') as f:
        reader = csv.reader(f, delimiter=',')
        second_line = list(reader)[1]
        for i, field in enumerate(second_line):
            props.f_headers[i].sample = field
            props.f_headers[i].include_flag = False


class TEST_OT_sniff_csv(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "file.sniff_csv"
    bl_label = "TEST_OT_sniff_csv"

    @classmethod
    def poll(cls, context):
        props = context.scene.test_pg
        cond1 = os.path.isfile(props.ip_csv_fname)
        return cond1

    def execute(self, context):
        print(f"{self.bl_idname} pressed")
        props = context.scene.test_pg
        sniff_csv(context)
        if len(props.f_details) > 0:
            try:
                props.color_list = props.f_details[0].id_name
            except TypeError:
                pass
        return {'FINISHED'}


classes = [
    TEST_OT_sniff_csv,
    ]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()