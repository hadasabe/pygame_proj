import pygame
import math
import os

from settings import *
from player import PLayer
from sprite_objects import *
from ray_casting import ray_casting
from drawing import Drawing

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
clock = pygame.time.Clock()
player = PLayer()
drawing = Drawing(sc)
sprites = Sprites()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.movement()

    sc.fill(BLACK)

    drawing.bg(player.angle)
    walls = ray_casting(player, drawing.textures)
    drawing.world(walls + [obj.object_locate(player, walls) for obj in sprites.list_of_objects])
    drawing.fps(clock)

    pygame.display.flip()
    clock.tick(FPS)
