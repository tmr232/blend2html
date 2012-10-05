import math

import bpy
import mathutils

X = mathutils.Vector((1, 0, 0))
Y = mathutils.Vector((0, 1, 0))
Z = mathutils.Vector((0, 0, 1))

def get_rotation(normal):
    # Make sure the normal is not the Z axis
    if normal.x == normal.y == 0:
        return (0, 0, 0)
    
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

def create_rotation_matrix(x, y, z):
    def rot_mat(*args): return mathutils.Matrix.Rotation(*args)
    return rot_mat(z, 4, 'Z') * rot_mat(y, 4, 'Y') * rot_mat(x, 4, 'X')

def flatten_face(face, mesh):
    # Create the rotation matrix to reverse the rotation
    rotation = get_rotation(face.normal)
    print (rotation)
    rotation_matrix = create_rotation_matrix(*rotation)
    print (rotation_matrix)
    inverse_rotation_matrix = rotation_matrix.transposed()
    
    flattened_verts = []
    
#    for vert in (mesh.vertices[i].co for i in face.vertices):
#        flattened_verts.append(inverse_rotation_matrix * vert)
    for i in face.vertices:
        mesh.vertices[i].co = inverse_rotation_matrix * mesh.vertices[i].co
        
    return flattened_verts
    

normal = bpy.context.selected_objects[0].data.polygons[0].normal
print(normal)
print(get_rotation(normal))
print()
print(flatten_face(bpy.context.selected_objects[0].data.polygons[0], bpy.context.selected_objects[0].data))