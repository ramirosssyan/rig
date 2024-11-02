import pygame as pg
from pygame import Vector2 as vec2
from numpy import sin, cos


class Instance:
    def __init__(self, name, parent, *children, **properties):
        self.name = name
        self.parent = parent
        self.children = children
        self.properties = properties

        if isinstance(parent, Instance):
            parent.children[name] = self

class Attachment:
    def __init__(self, name, parent, position, rotation):
        self = Instance(
            name=name,
            parent=parent,
            position=position,
            rotation=rotation
        )

    @property
    def position

    @property.getter
    def vector(self):
        return vec2(
            sin(self.properties["rotation"]),
            cos(self.properties["rotation"])
        )
    
    
Attachment(
    name="nah",
    position=vec2
)