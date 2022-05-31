import pygame as pg
import numpy as np
from camera import *
from projection import *
from object import *

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
        

    def create_objects(self):
        self.camera = Camera(self, [0.5,1,-4])
        self.projection = Projection(self)
        self.object = Object(self)
        self.create_default_scene()
    
    def read_obj(self, file):
        vertices, faces = [],[]
        with open(file) as f:
            for line in f:
                if line.startswith('v '):
                    vertices.append([coord for coord in line.split()[1:]]+[1])
                elif line.startswith('f '):
                    pass
        return Object(self, vertices, faces)

    def read_stl(self, file):
        vertices, faces = [],[]
        with open(file) as f:
            for line in f:
                pass

    def create_default_scene(self):
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
        self.axes.draw()
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
