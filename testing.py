import numpy as np
file = r'C:\Users\jaket\Downloads\bugatti.obj'

vertices = np.array([[0,1], [1,0],[0,0],[1,1]])
faces = np.array([(0,1,2)])
print(vertices[faces[0]])

def read_obj(file):
        vertices, faces = [],[]
        with open(file) as f:
            for line in f:
                if line.startswith('v '):
                    vertices.append([float(coord) for coord in line.split()[1:]]+[1])
                elif line.startswith('f '):
                    face_lines = line.split()[1:]
                    if '//' in line:
                        splitter = '//'
                    else:
                         splitter = '/'
                    faces.append(tuple([int(face_line.split(splitter)[0]) - 1 for face_line in face_lines]))
        vertices = np.array(vertices, dtype='float16')
        faces = np.array(faces, dtype=object)

        #renormalize the coordinates after the transformation
        #renormalize the coordinates after the transformation
        vertices /= vertices[:, -1].reshape(-1,1)

        #coordinates larger than two are not currently in view
        vertices[(vertices > 2) | (vertices < -2)] = 0

        #slice out the 2D coordinates currently in view after projection
        vertices = vertices[:,:2]
        
        with open(r'C:\Users\jaket\Documents\GitHub\Simple-3D-engine\testing.txt', 'w') as f:
            f.write('Vertices \n')
            f.writelines([str(vertex)+'\n' for vertex in vertices])
            f.write('Faces \n')
            f.writelines([str(face)+'\n' for face in faces]) 
            f.write('Polygons \n')
            f.writelines([str(vertices[face]) for face in faces])

read_obj(file)



