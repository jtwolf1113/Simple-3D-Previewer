import numpy as np

def translate(trans_vector):
    dx, dy, dz = trans_vector
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [dx,dy,dz,1]
    ])

def rotate_x(angle):
    sin = np.sin(angle)
    cos = np.cos(angle)

    return np.array([
        [1, 0, 0, 0],
        [0, cos, sin, 0],
        [0, -sin, cos, 0],
        [0, 0, 0, 1]
    ])

def rotate_y(angle):
    sin = np.sin(angle)
    cos = np.cos(angle)

    return np.array([
        [cos, 0, -sin, 0],
        [0, 1, 0, 0],
        [sin, 0, cos, 0],
        [0, 0, 0, 1]
    ])

def rotate_z(angle):
    sin = np.sin(angle)
    cos = np.cos(angle)

    return np.array([
        [cos, sin, 0, 0],
        [-sin, cos, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

def scale(factor):
    return np.array([
        [factor, 0, 0, 0],
        [0, factor, 0, 0],
        [0, 0, factor, 0],
        [0, 0, 0, 1]
    ]) 

