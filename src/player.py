import pygame
import math

from settings import *


class PLayer:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        # mouse_x, mouse_y = pygame.mouse.get_pos()
        # rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        # self.angle = math.atan2(rel_y, rel_x)

        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += player_speed * cos_a
            self.y += player_speed * sin_a
        if keys[pygame.K_w] and keys[pygame.K_LSHIFT]:
            self.x += player_speed * 2 * cos_a
            self.y += player_speed * 2 * sin_a
        if keys[pygame.K_s]:
            self.x += -player_speed * cos_a
            self.y += -player_speed * sin_a
        if keys[pygame.K_a]:
            self.x += player_speed * sin_a
            self.y += -player_speed * cos_a
        if keys[pygame.K_d]:
            self.x += -player_speed * sin_a
            self.y += player_speed * cos_a
        if keys[pygame.K_q]:
            self.angle -= 0.02
        if keys[pygame.K_e]:
            self.angle += 0.02

        self.angle %= DOUBLE_PI