import stl
file = 'Small 30 mm Shield Scaled up 10x V1.4 Gear  v2.stl'
new_file = file[:-4] + '(1).stl'
#print(new_file)

vertices, faces = [],[]
mesh = stl.mesh.Mesh.from_file(file)
vertex_index = 0
for face_data in mesh.data:
    #facedata[0] is the normal vector
    #facedata[1] is the list of coordinate lists
    #facedata[2] is the attribute info
    for vertex in face_data[1]:
        vertices.append(vertex)
        vertex_index += 1
        if not vertex_index % 3:
            faces.append((vertex_index-3,vertex_index-2, vertex_index-1))
print(vertices)

#mesh.data
#mesh.speedups
#mesh.name



'''
with open(file, mode='rb') as f:
    q = str(f.readline())
    print(q)
    #if 'solid' not in f.readline:
        
        #binary file
        #stl_object = stl.read_binary_file(new_file)
        #stl_object.write_ascii(new_file)
'''