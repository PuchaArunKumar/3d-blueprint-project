import bpy
import sys

# Parse user input from command line arguments
user_input = " ".join(sys.argv[sys.argv.index("--") + 1:]).lower()

# Delete default cube
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Generate a car model based on user input
if "two-seater sports car" in user_input:
    # Create a basic car body
    bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 1))
    car_body = bpy.context.object
    car_body.name = "CarBody"
    car_body.scale = (3, 1.5, 0.5)

    # Add gull-wing doors if specified
    if "gull-wing doors" in user_input:
        bpy.ops.mesh.primitive_cube_add(size=1, location=(-1.2, 0, 1.5))
        door_left = bpy.context.object
        door_left.name = "DoorLeft"
        door_left.scale = (0.1, 0.5, 0.5)
        door_left.rotation_euler = (0, 0, 0.8)

        bpy.ops.mesh.primitive_cube_add(size=1, location=(1.2, 0, 1.5))
        door_right = bpy.context.object
        door_right.name = "DoorRight"
        door_right.scale = (0.1, 0.5, 0.5)
        door_right.rotation_euler = (0, 0, -0.8)

    # Add aggressive front grill if specified
    if "aggressive front grill" in user_input:
        bpy.ops.mesh.primitive_cube_add(size=1, location=(0, -1.5, 1))
        front_grill = bpy.context.object
        front_grill.name = "FrontGrill"
        front_grill.scale = (2, 0.1, 0.2)

# Export the model as an OBJ file
output_path = "/content/car.obj"
bpy.ops.export_scene.obj(filepath=output_path)

print(f"3D model exported to {output_path}")
