import pygame as pg
import numpy as np

class Render:
    def __init__(self) -> None:
        pg.init()
        self.RESOLUTION = self.WIDTH, self.HEIGHT = 1540, 800
        self.FPSMAX = 144
        self.screen = pg.display.set_mode(self.RESOLUTION)
        self.clock = pg.time.Clock()
        self.icon = pg.image.load('icon.png')
        pg.display.set_icon(self.icon)


    def draw_frames(self):
        self.screen.fill(pg.Color(120,120,120))

    def run_program(self):
        while True:
            self.draw_frames()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption('FPS: '+str(int(self.clock.get_fps())))
            pg.display.flip()
            self.clock.tick(self.FPSMAX)


if __name__ == '__main__':
    App = Render()
    App.run_program()
