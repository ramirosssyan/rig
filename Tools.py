import pygame as pg
from pygame import Vector2 as vec2
from Bone import Bone
from numpy import sin, cos, pi, arctan2


class Rotate:
    def __init__(self, pos):
        self.pos = pos
        self.on_rotation = False
        self.last_angle = 0
        self.angle = 0
    
    def update(self):
        mouse = pg.mouse
        keys = pg.key.get_pressed()

        if keys[pg.K_r]:
            self.on_rotation = True
        else:
            self.on_rotation = False
            return 0

        if self.on_rotation:
            self.last_angle = self.angle
            self.angle = arctan2(
                self.pos.x - mouse.get_pos()[0],
                self.pos.y - mouse.get_pos()[1]
            )

        return -(self.angle - self.last_angle)
        
    def draw(self, window: pg.SurfaceType):
        pg.draw.circle(
            window, pg.Color(200, 20, 20),
            self.pos, 100, 1
        )
        pg.draw.line(
            window, pg.Color(20, 200, 20),
            self.pos, self.pos + vec2(sin(self.angle-pi)*100, cos(self.angle-pi)*100)
        )
