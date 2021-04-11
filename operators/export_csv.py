import bpy
import os
import csv


def export_csv(context):
    props = context.scene.test_pg
    op_file = os.path.join(props.op_csv_dir, props.op_csv_fname)
    fieldnames = [field.map_list for field in props.maplist if field.include_flag and field.map_list != 'None']
    with open(op_file, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, restval='')
        writer.writeheader()
    with open(op_file, mode='a') as f:
        for detail in props['f_details']:
            dict_keys = []
            dict_vals = []
            # csv_dict = None
            for item in detail.keys():
                if item == 'id_name':
                    if 'ID Name' in fieldnames:
                        dict_keys.append('ID Name')
                        dict_vals.append(detail[item])
                elif item == 'red':
                    if 'Red' in fieldnames:
                        dict_keys.append('Red')
                        dict_vals.append(detail[item])
                elif item == 'green':
                    if 'Green' in fieldnames:
                        dict_keys.append('Green')
                        dict_vals.append(detail[item])
                elif item == 'blue':
                    if 'Blue' in fieldnames:
                        dict_keys.append('Blue')
                        dict_vals.append(detail[item])
                elif item == 'alpha':
                    if 'Alpha' in fieldnames:
                        dict_keys.append('Alpha')
                        dict_vals.append(detail[item])
                elif item == 'hex':
                    if 'Hexadecimal' in fieldnames:
                        dict_keys.append('Hexadecimal')
                        dict_vals.append(f"#{detail[item]}")
                elif item == 'hue':
                    if 'Hue' in fieldnames:
                        dict_keys.append('Hue')
                        dict_vals.append(detail[item])
                elif item == 'sat':
                    if 'Saturation' in fieldnames:
                        dict_keys.append('Saturation')
                        dict_vals.append(detail[item])
                elif item == 'val':
                    if 'Value' in fieldnames:
                        dict_keys.append('Value')
                        dict_vals.append(detail[item])
                elif item == 'desc':
                    if 'Description' in fieldnames:
                        dict_keys.append('Description')
                        dict_vals.append(detail[item])
#                else:
#                    dict_keys.append('None')
#                    dict_vals.append('')
#            csv_dict = dict(zip(dict_keys, dict_vals))
            me = str([i for i in dict_vals])
            me = me.replace(" ", "")
            me = me.replace("[", "")
            me = me.replace("]", "")
            me = me.replace("\'", "")
            f.write(me)
            f.write("\n")


class TEST_OT_export_csv(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "file.export_csv"
    bl_label = "TEST_OT_export_csv"

    @classmethod
    def poll(cls, context):
        props = context.scene.test_pg
        cond1 = os.path.isdir(props.op_csv_dir)
        cond2 = (
            props.op_csv_fname.lower().endswith(".txt") or
            props.op_csv_fname.lower().endswith(".csv")
            )
        return cond1 and cond2

    def execute(self, context):
        print(f"{self.bl_idname} pressed")
        export_csv(context)
        return {'FINISHED'}


classes = [
    TEST_OT_export_csv,
    ]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
