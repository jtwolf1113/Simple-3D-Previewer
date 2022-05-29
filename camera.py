from matrix_math import *
import pygame as pg

class Camera():
    def __init__(self, app_window, position) -> None:
        #where are we rendering to
        self.window = app_window
        #where is the camera located
        self.pos = np.array([*position, 1.0])
        #what is the direction the camera faces
        self.z_ori = np.array([0,0,1,1])
        self.y_ori = np.array([0,1,0,1])
        self.x_ori = np.array([1,0,0,1])
        #set fov params
        self.hFOV = np.pi/3 #60 degrees
        self.vFOV = self.hFOV*(self.window.HEIGHT/self.window.WIDTH) #scale accordingly
        #set near and far render params
        self.near = 0.1
        self.far = 100

    def move_camera(self):
        key = pg.key.get_pressed()
        #choose controls for camera
    
    def position(self):
        x,y,z,w = self.pos
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 0],
            [-x,-y,-z,1]
        ])
    
    def orientation(self):
        x1,x2,x3,x4 = self.x_ori
        y1,y2,y3,y4 = self.y_ori
        z1,z2,z3,z4 = self.z_ori
        return np.array([
            [x1,y1,z1, 0],
            [x2, y2, z2, 0],
            [x3, y3, z3, 0],
            [0, 0, 0, 1]
        ])


    def camera_matrix(self):
        return self.position() @ self.orientation()