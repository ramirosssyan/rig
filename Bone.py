import pygame as pg
from pygame import Vector2 as vec2


class Bone:
    def __init__(self, p0: vec2, p1: vec2, *children):
        self.p0 = p0
        self.p1 = p1
        self.dist = vec2.distance_to(p0, p1)
        self.children = children

    def rotate(self, angle):
        self.p1 = (self.p1 - self.p0).rotate_rad(angle) + self.p0

        for child in self.children:
            child.rotate_around_vec(self.p0, angle)

    def rotate_around_vec(self, vec: vec2, angle):
        self.p0 = (self.p0 - vec).rotate_rad(angle) + vec
        self.p1 = (self.p1 - vec).rotate_rad(angle) + vec

        for child in self.children:
            child.rotate_around_vec(vec, angle)

    def move(self, vec: vec2):
        self.p0 += vec
        self.p1 += vec

        for child in self.children:
            child.move(vec)

    def draw(self, window):
        pg.draw.circle(
            window, pg.Color(0, 0, 0),
            self.p0, 3
        )
        pg.draw.circle(
            window, pg.Color(0, 0, 0),
            self.p1, 2
        )
        pg.draw.line(
            window, pg.Color(0, 0, 0),
            self.p0, self.p1
        )

        for child in self.children:
            child.draw(window)


# lol!!!
