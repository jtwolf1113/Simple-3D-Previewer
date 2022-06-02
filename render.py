import pygame as pg
import numpy as np
from camera import *
from projection import *
from object import *
from stl import mesh
from zipfile import ZipFile
from re import findall

class Render:
    def __init__(self, file = None, fullscreen = False, draw_vertices = True) -> None:

        self.fullscreen = fullscreen
        if file is not None:
            self.file = file
            self.filetype = file[-4:]
        else:
            self.file = None
            self.filetype = ''
        self.RESOLUTION = self.WIDTH, self.HEIGHT = 1540, 800
        self.draw_vertices = draw_vertices
        self.FPSMAX = 144
        pg.init()
        if self.fullscreen:
            self.screen = pg.display.set_mode((0,0), pg.FULLSCREEN)
        else:
            self.screen = pg.display.set_mode(self.RESOLUTION)
        self.clock = pg.time.Clock()
        self.icon = pg.image.load('icon.png')
        pg.display.set_icon(self.icon)
        
        self.create_objects()
        
        
        

    def create_objects(self):
        self.camera = Camera(self, [.5,1,-4])
        self.projection = Projection(self)
        if self.filetype == '.stl':
            self.object = self.read_stl(self.file)
        elif self.filetype == '.obj':
            self.object = self.read_obj(self.file)
        elif self.filetype == '.3mf':
            self.object = self.read_3mf(self.file)
        else:
            self.create_default_scene()
    
    def read_obj(self, file):
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
        faces = np.array(faces)
        return Object(self, vertices=vertices, faces=faces, draw_vertices=self.draw_vertices)

    def read_stl(self, file):
        vertices, faces = [],[]
        mesh_item = mesh.Mesh.from_file(file)
        vertex_index = 0
        for face in mesh_item.data:
            for vertex in face[1]:
                vertices.append(vertex.tolist()+[1])
            #need to adjust this to tell which vertex    
            faces.append((vertex_index,vertex_index+1, vertex_index+2))
            vertex_index += 3
        vertices = np.array(vertices, dtype='float16')
        faces = np.array(faces)
        return Object(self, vertices=vertices, faces=faces, draw_vertices=self.draw_vertices)
    
    def read_3mf(self, file):
        vertices, faces = [],[]
        with ZipFile(file) as zip_object:
            with zip_object.open('3D/3dmodel.model') as f:
                for line in f.readlines():
                    if line.startswith(b'                    <vertex'):
                        vertices.append([float(k) for k in findall(b'"([^"]*)"', line)]+[1])
                    elif line.startswith(b'                    <triangle'):
                        faces.append([int(k) for k in findall(b'"([^"]*)"', line)])
        vertices = np.array(vertices, dtype='float16')
        faces = np.array(faces)
        return Object(self, vertices=vertices, faces=faces, draw_vertices=self.draw_vertices)
    

    def create_default_scene(self):
        self.object = Object(self, draw_vertices=self.draw_vertices)
        self.object.cube()
        self.object.translate([0.2, 0.4, 0.2])
        self.axes = Axes(self)
        self.axes.translate([0.7,.9,.7])
        self.world_axes = Axes(self)
        self.world_axes.scale(2.5)
        self.world_axes.translate([0.0001,0.0001,0.0001])
        self.world_axes.movement = False

    def draw_frames(self):
        self.screen.fill(pg.Color(66,69,73))
        self.object.draw()
        if hasattr(self, 'axes'):
            self.axes.draw()
        if hasattr(self,'world_axes'):
           self.world_axes.draw()

    def run_program(self):
        while True:
            self.draw_frames()
            self.camera.move_camera()
            [pg.quit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption('FPS: '+str(int(self.clock.get_fps())))
            pg.display.flip()
            self.clock.tick(self.FPSMAX)

