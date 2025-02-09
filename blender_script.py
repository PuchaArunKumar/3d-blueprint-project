import bpy

# Delete default objects (cube, light, camera)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Create a cube
bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0))
cube = bpy.context.object

# Scale the cube
cube.scale = (1.5, 1.5, 1.5)

# Select the cube
bpy.ops.object.select_all(action='DESELECT')  # Deselect all objects
cube.select_set(True)  # Select the cube
bpy.context.view_layer.objects.active = cube  # Set the cube as the active object

# Set the desired output path
output_path = "/content/cube.obj"  # Save in Colab's workspace

# Export the selected object as an OBJ file
bpy.ops.export_scene.obj(filepath=output_path, use_selection=True)

print(f"3D model exported to {output_path}")
