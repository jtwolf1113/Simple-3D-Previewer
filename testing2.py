from logging import error
from numba import njit
import numpy as np
import timeit

@njit(fastmath = True)
def sorting_function(input_tuple):
    return sorted(input_tuple)

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
            #f.write('Vertices \n')
            #f.writelines([str(vertex)+'\n' for vertex in vertices])
            #f.write('Faces \n')
            #f.writelines([str(face)+'\n' for face in faces]) 
            f.write('Polygons \n')
            for face in faces:
                f.writelines(str(vertices[sorted(face)]))

def read_obj2(file):
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
                    
                    #print(int(face_line.split(splitter)[0]) for face_line in face_lines)
                    #faces.append(sorted(list(int(face_line.split(splitter)[0]) - 1 for face_line in face_lines)))
                    #faces.append(np.array(sorted([int(face_line.split(splitter)[0])-1 for face_line in face_lines]), dtype = 'int16'))
                    faces.append(sorted([int(int(face_line.split(splitter)[0])-1) for face_line in face_lines]))
        print('faces preprocess test')
        print((faces[0][0]), (faces[0]))
        print('vertices preprocess test')
        print((vertices[0][0]), (vertices[0]))
        vertices = np.array(vertices, dtype='float16')
        vertices = vertices[:,:2]
        faces = np.array([sorted(face) for face in faces], dtype = list)
        print('faces and vertices postprocess')
        print(faces.dtype,faces)
        print(vertices.dtype, vertices)

        print('faces test')
        print(faces[0], faces[0][0])
        print('polygons test')
        
        print(vertices[faces[0]])

        
        #renormalize the coordinates after the transformation
        #renormalize the coordinates after the transformation
        #vertices /= vertices[:, -1].reshape(-1,1)

        #coordinates larger than two are not currently in view
        #vertices[(vertices > 2) | (vertices < -2)] = 0

        #slice out the 2D coordinates currently in view after projection
        vertices = vertices[:,:2]
        
        #for index, face in enumerate(faces):
            #faces[index] = sorted(face)

        #with open(r'C:\Users\jaket\Documents\GitHub\Simple-3D-engine\testing.txt', 'w') as f:
            #f.write('Vertices \n')
            #f.writelines([str(vertex)+'\n' for vertex in vertices])
            #f.write('Faces \n')
            #f.writelines([str(face)+'\n' for face in faces]) 
            #f.write('Polygons \n')
            #for face in faces:
                #f.writelines(str(vertices[face]))
        
#file = r'C:\Users\jaket\Documents\GitHub\Simple-3D-engine\Small 30 mm Shield Scaled up 10x V1.4 Gear  v2-export.obj'
file = r'C:\Users\jaket\Downloads\bugatti.obj'

t1 = timeit.default_timer()
read_obj2(file)
t2 = timeit.default_timer()
print(t2-t1)
t2 = timeit.default_timer()
#read_obj(file)
t3 = timeit.default_timer()

print(t3-t2)