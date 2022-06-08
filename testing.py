import numpy as np
faces = []
for k in range(2):
    faces.append((tuple(sorted([int(num)-1 for num in range(1,10)]))))

print((np.array(faces, dtype = object)[0]))
