import math

import bpy
import mathutils

X = mathutils.Vector((1, 0, 0))
Y = mathutils.Vector((0, 1, 0))
Z = mathutils.Vector((0, 0, 1))

def get_rotation(normal):
    # Define local axes
    normal_z = normal
    normal_x = Z.cross(normal_z)
    normal_y = normal_z.cross(normal_x)
    
    # Get rotation angles
    angle_z = math.atan2(normal_x.y, normal_x.x)
    
    mat_rotate_z = mathutils.Matrix.Rotation(-angle_z, 4, 'Z')
    normal_y_rotated = mat_rotate_z * normal_y
    angle_y = math.atan2(normal_y_rotated.z, normal_y_rotated.y)
    
    return (0, angle_y, angle_z)

normal = bpy.context.selected_objects[0].data.polygons[0].normal
print(get_rotation(normal))