from matrix_math import *
import pygame as pg
import numpy as np

class Object:
    def __init__(self, app) -> None:
        self.window = app
        #vertices are the coordinates in 4-space
        self.vertices = np.array([])
        #faces are indices of relevant vertices
        self.faces = np.array([])
        self.font = pg.font.SysFont('Arial', 30, bold=True)
        self.movement = True
        self.draw_vertices = True

    def projection(self):
        #how do the vertices appear relative to the camera position
        vertices = self.vertices @ self.window.camera.camera_matrix()
        #how does the image scale due to the projection properties
        vertices = vertices @ self.window.projection.projection_matrix
        #renormalize the coordinates after the transformation
        vertices /= vertices[:, -1].reshape(-1,1)
        #coordinates larger than one are not currently in view
        vertices[(vertices > 2) | (vertices < -2)] = 0
        #scale the normalized space to the screen resolution
        vertices = vertices @ self.window.projection.screen_matrix
        #slice out the 2D coordinates currently in view
        vertices = vertices[:,:2]

        for index, color_face in enumerate(self.color_faces):
            color, face = color_face
            polygon = vertices[face]
            if not np.any((polygon == self.window.WIDTH/2) | (polygon == self.window.HEIGHT/2)):
                pg.draw.polygon(self.window.screen, color, polygon, 3)
                if self.label:
                    text = self.font.render(self.label[index], True, pg.Color('white'))
                    self.window.screen.blit(text, polygon[-1])
        if self.draw_vertices:
            for vertex in vertices:
                if not np.any((vertex == self.window.WIDTH/2) | (vertex == self.window.HEIGHT/2)):
                    pg.draw.circle(self.window.screen, pg.Color('white'), vertex, 6)


    def draw(self):
        self.projection()
        self.default_movement()
    
    def default_movement(self):
        if self.movement:
            self.rotateY(-(pg.time.get_ticks() % 0.005))
    
    def triangular_pyramid(self):
        self.vertices = np.array([(0,0,0,1),(1,0,0,1),(0,1,0,1),(0,0,1,1)])
        self.faces = np.array([(0,1,2),(0,1,3),(0,2,3),(1,2,3)])
        self.translate([0.0001,0.0001,0.0001])

        self.color_faces = [(pg.Color('pink'), face) for face in self.faces]
        self.label = ''

    def cube(self):
        self.vertices = np.array([(0,0,0,1),(1,0,0,1),(0,1,0,1),(0,0,1,1),
                                  (1,1,0,1),(1,0,1,1),(0,1,1,1),(1,1,1,1)])
        self.faces = np.array([(0,1,4,2), (0,1,5,3), (1,4,7,5), 
                               (0,3,6,2), (3,5,7,6), (2,6,7,4)])
        self.translate([0.0001,0.0001,0.0001])

        self.color_faces = []
        for face in self.faces:
            self.color_faces.append((pg.Color('blue'), face)) 
        #self.color_faces = [(pg.Color('blue'), face) for face in self.faces]
        self.label = ''


    #implement transformation matrix math
    def translate(self, dr):
        self.vertices = self.vertices @ translate(dr)
    
    def scale(self, factor):
        self.vertices = self.vertices @ scale(factor)
    
    def rotateX(self, angle):
        self.vertices = self.vertices @ rotate_x(angle)
    
    def rotateY(self, angle):
        self.vertices = self.vertices @ rotate_y(angle)
    
    def rotateZ(self, angle):
        self.vertices = self.vertices @ rotate_z(angle)

class Axes(Object):
    def __init__(self, app) -> None:
        super().__init__(app)
        self.vertices = np.array([(0,0,0,1),(1,0,0,1),(0,1,0,1),(0,0,1,1)])
        self.faces = np.array([(0,1),(0,2),(0,3)])
        self.colors = [pg.Color('red'),pg.Color('green'),pg.Color('blue')]
        self.color_faces = [(color, face) for color, face in zip(self.colors, self.faces)]
        self.draw_vertices = False
        self.label = 'XYZ'

