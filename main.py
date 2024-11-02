import pygame as pg
from pygame import Vector2 as vec2
from Bone import Bone
from Tools import Rotate
from numpy import pi


FPS = 60
WINDOW_SIZE = vec2(1440, 900)

pg.init()

clock = pg.time.Clock()
window = pg.display.set_mode(WINDOW_SIZE)

pg.display.toggle_fullscreen()

bones = Bone(
    vec2(720, 450), vec2(720, 350),
    Bone(vec2(720, 350), vec2(720, 300)),
    Bone(vec2(795, 350), vec2(795, 450)),
    Bone(vec2(645, 350), vec2(645, 450)),
    Bone(vec2(745, 450), vec2(745, 550)),
    Bone(vec2(695, 450), vec2(695, 550))
)

rotate_tool = Rotate(WINDOW_SIZE / 2)

running = True
while running:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()
    if keys[pg.K_ESCAPE]:
        running = False

    # programm
    rotation = rotate_tool.update()
    bones.children[0].rotate(rotation)

    # draw ui
    window.fill(pg.Color(50, 50, 75))

    bones.draw(window)
    rotate_tool.draw(window)
    
    # step
    pg.display.update()
    clock.tick(FPS)

pg.quit()