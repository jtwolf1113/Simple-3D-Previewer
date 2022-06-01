import pygame as pg
import numpy as np
from camera import *
from projection import *
from object import *
import stl
from zipfile import ZipFile
from re import findall

class Render:
    def __init__(self) -> None:
        pg.init()
        self.RESOLUTION = self.WIDTH, self.HEIGHT = 1540, 800
        self.FPSMAX = 144
        self.screen = pg.display.set_mode(self.RESOLUTION)
        self.clock = pg.time.Clock()
        self.icon = pg.image.load('icon.png')
        pg.display.set_icon(self.icon)
        self.create_objects()
        self.axes = False
        self.world_axes = False
        

    def create_objects(self):
        self.camera = Camera(self, [-5,5,-50])
        self.projection = Projection(self)
        self.object = self.read_3mf('Small 30 mm Shield Scaled up 10x V1.4 Gear  v2-export.3mf')
        #self.object = self.read_stl('Small 30 mm Shield Scaled up 10x V1.4 Gear  v2.stl')
        #self.object = self.read_obj('Small 30 mm Shield Scaled up 10x V1.4 Gear  v2-export.obj')
        #self.create_default_scene()
    
    def read_obj(self, file):
        vertices, faces = [],[]
        with open(file) as f:
            for line in f:
                if line.startswith('v '):
                    vertices.append([float(coord) for coord in line.split()[1:]]+[1])
                elif line.startswith('f '):
                    face_lines = line.split()[1:]
                    faces.append(tuple([int(face_line.split('//')[0]) - 1 for face_line in face_lines]))
        vertices = np.array(vertices)
        faces = np.array(faces)
        return Object(self, vertices = vertices, faces = faces)

    def read_stl(self, file):
        vertices, faces = [],[]
        mesh = stl.mesh.Mesh.from_file(file)
        vertex_index = 0
        for face in mesh.data:
            for vertex in face[1]:
                vertices.append(vertex.tolist()+[1])
            #need to adjust this to tell which vertex    
            faces.append((vertex_index,vertex_index+1, vertex_index+2))
            vertex_index += 3
        vertices = np.array(vertices)
        faces = np.array(faces)
        return Object(self, vertices=vertices, faces=faces)
    
    def read_3mf(self, file):
        vertices, faces = [],[]
        with ZipFile(file) as zip_object:
            with zip_object.open('3D/3dmodel.model') as f:
                for line in f.readlines():
                    if line.startswith(b'                    <vertex'):
                        vertices.append([float(k) for k in findall(b'"([^"]*)"', line)]+[1])
                    elif line.startswith(b'                    <triangle'):
                        faces.append([int(k) for k in findall(b'"([^"]*)"', line)])
        vertices = np.array(vertices)
        faces = np.array(faces)
        return Object(self, vertices=vertices, faces=faces)
    

    def create_default_scene(self):
        self.object = Object(self)
        self.object.cube()
        self.object.translate([0.2, 0.4, 0.2])
        self.axes = Axes(self)
        self.axes.translate([0.7,.9,.7])
        self.world_axes = Axes(self)
        self.world_axes.scale(2.5)
        self.world_axes.translate([0.0001,0.0001,0.0001])
        self.world_axes.movement = False


    '''
    def draw_UI(self):
        return None
    '''
    def draw_frames(self):
        self.screen.fill(pg.Color(66,69,73))
        self.object.draw()
        if self.axes:
            self.axes.draw()
        if self.world_axes:
           self.world_axes.draw()

    def run_program(self):
        while True:
            self.draw_frames()
            self.camera.move_camera()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption('FPS: '+str(int(self.clock.get_fps())))
            pg.display.flip()
            self.clock.tick(self.FPSMAX)


if __name__ == '__main__':
    App = Render()
    App.run_program()
