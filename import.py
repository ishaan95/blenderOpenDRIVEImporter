import bpy
import sys
import subprocess

argv = sys.argv
argv = argv[argv.index("--") + 1:]
bpy.ops.import_scene.obj(filepath=argv[0], axis_forward='X', axis_up='Z')
bpy.ops.import_scene.obj(filepath=argv[1], axis_forward='X', axis_up='Z')
bpy.ops.import_scene.obj(filepath=argv[1], axis_forward='X', axis_up='Z')

bpy.data.objects['lanes'].active_material.diffuse_color = (0.10224, 0.10224, 0.10224, 1)
bpy.data.objects['roadmarkings'].active_material.diffuse_color = (0.8, 0.3834, 0.0038, 1)
bpy.data.objects['roadmarkings'].location[2] = 0.1
bpy.data.objects['roadmarkings'].rotation_euler[2] = 0.0

bpy.data.objects['roadmarkings'].parent = bpy.data.objects['lanes']
bpy.data.objects.remove(bpy.data.objects['Cube'])
bpy.data.objects.remove(bpy.data.objects['Light'])
bpy.data.objects.remove(bpy.data.objects['Camera'])
bpy.ops.export_scene.fbx(filepath=argv[2], axis_forward='X', axis_up='Z', embed_textures=True)
