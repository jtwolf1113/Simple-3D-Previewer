from matrix_math import *
import pygame as pg
import numpy as np
from numba import njit
#reduce np.any bottleneck
@njit(fastmath =True)
def np_any_function(arr, a, b):
    return np.any((arr == a) | (arr == b))


class Object:
    def __init__(self, app, vertices = None, faces= None, draw_vertices = True) -> None:
        self.window = app
        #vertices are the coordinates in 4-space
        self.line_color = pg.Color('pink')
        self.vertex_color = pg.Color('white')
        self.text_color = pg.Color('white')
        if vertices is not None:
            self.vertices = vertices
        else:
            self.vertices = np.array([])
        #faces are indices of relevant vertices
        if faces is not None:
            self.faces = faces
            self.label = '' 
        else:
            self.faces = np.array([])
        self.font = pg.font.SysFont('Arial', 30, bold=True)
        self.movement = True
        self.draw_vertices = draw_vertices

    def projection(self):
        #how do the vertices appear relative to the camera position
        vertices = self.vertices @ self.window.camera.camera_matrix()
        #how does the image scale due to the projection properties
        vertices = vertices @ self.window.projection.projection_matrix

        #renormalize the coordinates after the transformation
        #renormalize the coordinates after the transformation
        vertices /= vertices[:, -1].reshape(-1,1)

        #coordinates larger than two are not currently in view
        vertices[(vertices > 2) | (vertices < -2)] = 0

        #scale the normalized space to the screen resolution
        vertices = vertices @ self.window.projection.screen_matrix
        #slice out the 2D coordinates currently in view after projection
        vertices = vertices[:,:2]

        #iterate over each face to ensure it's in view and draw the projection
        for index, face in enumerate(self.faces):
            polygon = vertices[face]
            if hasattr(self, 'colors'):
                self.line_color = self.colors[index]
            if not np_any_function(polygon, self.window.WIDTH/2, self.window.HEIGHT/2): #np.any((polygon == self.window.WIDTH/2) | (polygon == self.window.HEIGHT/2)):
                pg.draw.polygon(self.window.screen, self.line_color, polygon, 1)
                if self.label:
                    text = self.font.render(self.label[index], True, self.text_color)
                    self.window.screen.blit(text, polygon[-1])
        #similar for each vertex
        if self.draw_vertices:
            for vertex in vertices:
                if not np_any_function(vertex, self.window.WIDTH/2, self.window.HEIGHT/2): #np.any((vertex == self.window.WIDTH/2) | (vertex == self.window.HEIGHT/2)):
                    pg.draw.circle(self.window.screen, self.vertex_color, vertex, 2)

    #object draw function
    def draw(self):
        self.projection()
        self.default_movement()
    
    #simple animation for inspection
    def default_movement(self):
        if self.movement:
            self.rotateY(-(pg.time.get_ticks() % 0.005))
    
    #basic triangular pyramid shape
    def triangular_pyramid(self):
        self.vertices = np.array([(0,0,0,1),(1,0,0,1),(0,1,0,1),(0,0,1,1)])
        self.faces = np.array([(0,1,2),(0,1,3),(0,2,3),(1,2,3)])
        self.translate([0.0001,0.0001,0.0001])

        self.color_faces = [(pg.Color('pink'), face) for face in self.faces]
        self.label = ''

    #basic cube shape
    def cube(self):
        self.vertices = np.array([(0,0,0,1),(1,0,0,1),(0,1,0,1),(0,0,1,1),
                                  (1,1,0,1),(1,0,1,1),(0,1,1,1),(1,1,1,1)])
        self.faces = np.array([(0,1,4,2), (0,1,5,3), (1,4,7,5), 
                               (0,3,6,2), (3,5,7,6), (2,6,7,4)])
        self.translate([0.0001,0.0001,0.0001])

        self.color_faces = []
        for face in self.faces:
            self.color_faces.append((pg.Color('pink'), face)) 
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
    #create Axes inheriting from Object
    #want to use these to visualize the global coordinates vs object's local coordinates
    def __init__(self, app) -> None:
        super().__init__(app)
        self.vertices = np.array([(0,0,0,1),(1,0,0,1),(0,1,0,1),(0,0,1,1)])
        self.faces = np.array([(0,1),(0,2),(0,3)])
        self.colors = [pg.Color('red'),pg.Color('green'),pg.Color('blue')]
        self.color_faces = [(color, face) for color, face in zip(self.colors, self.faces)]
        self.draw_vertices = False
        self.label = 'XYZ'

