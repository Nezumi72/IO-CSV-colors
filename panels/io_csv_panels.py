import bpy


class VIEW3D_PT_test(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Test Panel"
    bl_idname = "VIEW3D_PT_test"
    bl_label = "CSV Color Helper"

    def draw(self, context):
        props = context.scene.test_pg
        layout = self.layout


class TEST_PT_sub_01(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Test Panel"
    bl_idname = "TEST_PT_sub_01"
    bl_label = "Import Options"
    bl_parent_id = "VIEW3D_PT_test"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        props = context.scene.test_pg
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)
        col.prop(props, 'ip_csv_fname')
        box = layout.box()
        col = box.column(align=True)
        col.operator("file.sniff_csv")
        if not bpy.ops.file.sniff_csv.poll():
            col.label(text="Requires txt or csv file")
        box = layout.box()
        col = box.column(align=True)
        row = col.row()
        row.label(text="CSV Header:")
        row.label(text="Sample:")
        row.label(text="Map to:")
        row.label(text="Scale:")
        for i, item in enumerate(props.f_headers):
            row = col.row()
            row.label(text=item.header)
            row.label(text=item.sample)
            row.prop(props.maplist[i], 'map_list', text="")
            test = False
            try:
                if int(item.sample) < 361:
                    test = True
            except ValueError:
                pass
            try:
                if float(item.sample) < 361:
                    test = True
            except ValueError:
                pass
            if test:
                row.prop(props.maplist[i], 'scale', text="")
            else:
                row.label(text="")
        box = layout.box()
        col = box.column(align=True)
        col.operator("file.load_csv")
        if not bpy.ops.file.load_csv.poll():
            col.label(text="Requires 1 unique ID Name mapped")


class TEST_PT_sub_02(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Test Panel"
    bl_idname = "TEST_PT_sub_02"
    bl_label = "Export Options"
    bl_parent_id = "VIEW3D_PT_test"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        props = context.scene.test_pg
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)
        col.prop(props, 'op_csv_dir')
        col.prop(props, 'op_csv_fname')
        box = layout.box()
        col = box.column(align=True)
        row = col.row()
        row.label(text="Include (limited to mapped data):")
        ori_header = [h.header for h in props.f_headers]
        for i, item in enumerate(props.maplist):
            row = col.row()
            row.label(text=ori_header[i])
            row.prop(props.maplist[i], 'include_flag', text="")
            row.label(text=item.map_list)
        box = layout.box()
        col = box.column(align=True)
        col.operator("file.print_csv")
        col.operator("file.export_csv")
        if not bpy.ops.file.export_csv.poll():
            col.label(text="Requires Directory")
            col.label(text="Requires filename ending in .csv or .txt")


class TEST_PT_sub_03(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Test Panel"
    bl_idname = "TEST_PT_sub_03"
    bl_label = "Save Images"
    bl_parent_id = "VIEW3D_PT_test"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        props = context.scene.test_pg
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)
        col.prop(props, 'icons_dir')
        col.prop(props, 'icon_size')
        col.operator("file.save_icons")
        if not bpy.ops.file.save_icons.poll():
            col.label(text="Requires valid Icons Dir")
            col.label(text="Requires 1 color type RGB, HSV or Hex")
            col.label(text="RGB, HSV or Hex data loaded")


class TEST_PT_sub_04(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Testing"
    bl_idname = "TEST_PT_sub_04"
    bl_label = "Sample Color"
    bl_parent_id = "VIEW3D_PT_test"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        my_props = context.scene.test_pg
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)
        if my_props.color_list:
            col.prop(my_props, "color_list")
        else:
            col.label(text='No Data loaded')
        col = box.column(align=True)
        col.operator("object.obj_vp_color")


class TEST_PT_sub_05(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Testing"
    bl_idname = "TEST_PT_sub_05"
    bl_label = "Color Details"
    bl_parent_id = "TEST_PT_sub_04"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        my_props = context.scene.test_pg
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)
        if my_props.color_list:
            try:
                me = my_props.f_details[my_props.color_list]
                for key in me.keys():
                    col.label(text=f"{key}: {str(me[key])}")
            except KeyError:
                pass
        else:
            col.label(text='Color not Selected')


class TEST_PT_sub_06(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Testing"
    bl_idname = "TEST_PT_sub_06"
    bl_label = "Palette Colors"
    bl_parent_id = "TEST_PT_sub_04"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        my_props = context.scene.test_pg
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)
        col.prop(my_props, "palette")
        col.operator("palette.add_color")
        col.prop(my_props, 'palette_columns', text='Display Columns:')
        row = box.row(align=True)
        if my_props.palette in bpy.data.palettes:
            for i, me in enumerate(list(bpy.data.palettes[my_props.palette].colors)):
                row.prop(me, "color", text="")
                if ((i+1) % my_props.palette_columns) == 0:
                    row = box.row(align=True)


class TEST_PT_sub_07(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Testing"
    bl_idname = "TEST_PT_sub_07"
    bl_label = "Materials Colors"
    bl_parent_id = "TEST_PT_sub_04"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        my_props = context.scene.test_pg
        ob = context.object
        layout = self.layout
        box = layout.box()
        col = box.column(align=True)
        if ob:
            col.label(text=f"Material color options for: {ob.name}")
            for slot in ob.material_slots:
                layout = self.layout
                box = layout.box()
                col = box.column(align=True)
                col.label(text=f"Material slot: {slot.name}")
                box = col.box()
                for node in slot.material.node_tree.nodes:
                    col = box.column(align=True)
                    col.label(text=f"Node: {node.name}")
                    for ip in node.inputs:
                        if ip.type == 'RGBA':
                            col.label(text=f"Color IP: {ip.name}")
                            row = col.row()
                            row.prop(ip, "default_value")
                            props = row.operator("material.assign_lsrgb")
                            props.mat = slot.name
                            props.node = node.name
                            props.ipname = ip.name


classes = [
    VIEW3D_PT_test,
    TEST_PT_sub_01,
    TEST_PT_sub_02,
    TEST_PT_sub_03,
    TEST_PT_sub_04,
    TEST_PT_sub_05,
    TEST_PT_sub_06,
    TEST_PT_sub_07,
    ]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
