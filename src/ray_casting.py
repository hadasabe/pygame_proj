import math

import pygame

from settings import *
from map import world_map


def mapping(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE


def ray_casting(player, texture):
    walls = []
    xo, yo = player.pos
    xm, ym = mapping(xo, yo)
    cur_angle = player.angle - HALF_FOV

    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        if cos_a >= 0:
            x = xm + TILE
            dx = 1
        else:
            x = xm
            dx = -1

        for i in range(0, WIDTH, TILE):
            depth_v = (x - xo) / cos_a
            yv = yo + depth_v * sin_a
            if mapping(x + dx, yv) in world_map:
                break
            x += dx * TILE

        y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, HEIGHT, TILE):
            depth_h = (y - yo) / sin_a
            xh = xo + depth_h * cos_a
            if mapping(xh, y + dy) in world_map:
                break
            y += dy * TILE

        depth, offset = (depth_v, yv) if depth_v < depth_h else (depth_h, xh)
        offset = int(offset) % TILE
        depth *= math.cos(player.angle - cur_angle)
        depth = max(depth, 0.00001)
        proj_height = min(int(PROJ_COEF / depth), 2 * HEIGHT)

        wall_column = texture['1'].subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)
        wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
        wall_pos = (ray * SCALE, HALF_HEIGHT - proj_height // 2)
        walls.append((depth, wall_column, wall_pos))

        cur_angle += DELTA_ANGLE
    return walls
