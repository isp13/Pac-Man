import pygame
import glob
from random import randint


class Ghost:
    direction = "right"

    def __init__(self, screenWidth, screenHeight, pygame, step, field, mode):
        self.image = pygame.image.load(glob.glob(f'images/ghost{mode}.*')[0])
        self.fearImage = pygame.image.load(glob.glob(f'images/ghostFear{mode}.*')[0])
        self.image = pygame.transform.scale(self.image, (step, step))
        self.baseImage = self.image
        self.fearImage = pygame.transform.scale(self.fearImage, (step, step))
        self.geometry = self.image.get_rect()
        self.velocity = 1
        self.speed = [self.velocity, 0]
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.pygame = pygame
        self.step = step
        self.field = field

    def set_center_position(self, x, y):
        self.geometry.center = (x, y)

    def set_position(self, x, y):
        self.geometry.x = x
        self.geometry.y = y

    def check_edges(self):
        if self.geometry.left < 0:
            self.geometry.left = 0
        if self.geometry.right > self.screenWidth:
            self.geometry.right = self.screenWidth
        if self.geometry.top < 0:
            self.geometry.top = 0
        if self.geometry.bottom > self.screenHeight:
            self.geometry.bottom = self.screenHeight

    def move(self):
        if self.field[(self.geometry.y + int(self.speed[1] * self.step)) // self.step][
            self.geometry.x // self.step] != 1:
            self.geometry.y += int(self.speed[1] * self.step)
        if self.field[self.geometry.y // self.step][
            (self.geometry.x + int(self.speed[0] * self.step)) // self.step] != 1:
            self.geometry.x += int(self.speed[0] * self.step)
        self.check_edges()

    def randomize(self):
        self.direction = ["right", "left", "up", "down"][randint(0, 3)]

    def is_ok(self, ghosts):
        x, y = self.geometry.x // self.step, self.geometry.y // self.step

        if self.direction == "right":
            x += 1
        elif self.direction == "left":
            x -= 1
        elif self.direction == "up":
            y -= 1
        elif self.direction == "down":
            y += 1

        if self.field[y][x] == 1:
            return False

        for i in ghosts:
            if x == i.geometry.x // i.step and y == i.geometry.y // i.step:
                return False
        return True

    def logic(self, target, ghosts):
        while not self.is_ok(ghosts):
           self.randomize()

        if self.direction == "left":
            self.speed = [-1, 0]
        elif self.direction == "right":
            self.speed = [1, 0]
        elif self.direction == "down":
            self.speed = [0, 1]
        elif self.direction == "up":
            self.speed = [0, -1]
        self.move()
