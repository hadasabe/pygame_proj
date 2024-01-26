import math

import pygame
from settings import *


class Sprites:
    def __init__(self):
        self.sprite_types = {
            'barrel': pygame.image.load('data/barrel/barrel.png').convert_alpha()
        }
        self.list_of_objects = [
            SpriteObject(self.sprite_types['barrel'], True, (7.1, 2.1), 1.8, 0.4),
            SpriteObject(self.sprite_types['barrel'], True, (5.9, 2.1), 1.8, 0.4)
        ]


class SpriteObject:
    def __init__(self, object, static, pos, shift, scale):
        self.object = object
        self.static = static
        self.pos = self.x, self.y = pos[0] * TILE, pos[1] * TILE
        self.shift = shift
        self.scale = scale

    def object_locate(self, player, walls):
        dx, dy = self.x - player.x, self.y - player.y
        dist_to_sprite = math.sqrt(dx ** 2 + dy ** 2)

        theta = math.atan2(dy, dx)
        gamma = theta - player.angle
        if dx > 0 and 180 <= math.degrees(player.angle) < 360 or dx < 0 and dy < 0:
            gamma += DOUBLE_PI

        delta_rays = int(gamma / DELTA_ANGLE)
        cur_ray = CENTER_RAY + delta_rays
        dist_to_sprite *= math.cos(HALF_FOV - cur_ray * DELTA_ANGLE)

        if 0 <= cur_ray <= NUM_RAYS - 1 and dist_to_sprite < walls[cur_ray][0]:
            proj_height = int(PROJ_COEF / dist_to_sprite * self.scale)
            half_proj_height = proj_height // 2
            shift = half_proj_height * self.shift

            sprite_pos = (cur_ray * SCALE - half_proj_height, HALF_HEIGHT - half_proj_height + shift)
            sprite = pygame.transform.scale(self.object, (proj_height, proj_height))
            return (dist_to_sprite, sprite, sprite_pos)
        else:
            return (False, )
