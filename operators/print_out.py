import bpy

def print_csv(context):
    props = context.scene.test_pg
    for detail in props['f_details']:
        for k in detail.keys():
            print(f"{k}: {detail[k]}")


class TEST_OT_print_csv(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "file.print_csv"
    bl_label = "TEST_OT_print_csv"

    @classmethod
    def poll(cls, context):
        props = context.scene.test_pg
        cond1 = len(props['f_details']) > 0
        return cond1

    def execute(self, context):
        print(f"{self.bl_idname} pressed")
        print_csv(context)
        return {'FINISHED'}


classes = [
    TEST_OT_print_csv,
    ]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)