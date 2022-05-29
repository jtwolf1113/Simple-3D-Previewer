import numpy as np

class Projection:
    def __init__(self, app) -> None:
        #need distance and FOV properties
        NEAR = app.camera.near
        FAR = app.camera.far
        RIGHT = np.tan(app.camera.hFOV / 2)
        LEFT = -RIGHT
        TOP = np.tan(app.camera.vFOV / 2)
        BOTTOM = -TOP

        #define projection matrix
        m00 = 2 / (RIGHT-LEFT)
        m11 = 2 / ()
        m22 = (FAR+NEAR) / (FAR - NEAR)
        m32 = -2* NEAR * FAR / (FAR - NEAR)

        self.projection_matrix = np.array([
            [m00,0,0,0],
            [0,m11,0,0],
            [0,0,m22,1],
            [0,0,m32,0]
        ])

        HW, HH = app.WIDTH/2, app.HEIGHT/2
        self.screen_matrix = np.array([
            [HW,0,0,0],
            [0,-HH,0,0],
            [0,0,1,1],
            [HW,HH,0,1]
        ])
