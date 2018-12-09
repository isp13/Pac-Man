import pygame
import sys, os
from pygame.locals import *


class seed():
    def __init__(self, screen, point):
        self.place = point
        self.screen_point = self.helpInseed.to_screen(point)
        self.Seed_color = Color.orange
        self.Seed_size = grid_size * 0.15

    def draw(self):
        (screen_x, screen_y) = self.screen_point
        pygame.draw.circle(screen_x, screen_y,
                          self.Seed_size,
                          color = self.Seed_color,
                          filled = 2)

    def to_screen(self, point):
        (x,y) = point
        x = x*grid_size + margin
        x = x*grid_size + margin
        return (x, y)

    def eat(self, place):
        (x,y) = place
        self.map[y][x] = 0
        self.foodcount = self.foodcount -1

    def win(self):
        if self.foodcount == 0:
            return 1
