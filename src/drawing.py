import math

import pygame
from settings import *
from ray_casting import ray_casting


class Drawing:
    def __init__(self, sc):
        self.sc = sc
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.textures = {'1': pygame.image.load('data/wall/a-brick3.png').convert()}

    def bg(self, angle):
        pygame.draw.rect(self.sc, (50, 50, 50), (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, world_objects):
        for obj in sorted(world_objects, key=lambda x: x[0], reverse=True):
            if obj[0]:
                _, object, object_pos = obj
                self.sc.blit(object, object_pos)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, RED)
        self.sc.blit(render, (10, 10))
