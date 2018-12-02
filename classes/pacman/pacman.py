import pygame
import glob
from classes.gameField.gameField import *


class Pacman():
    game_over = False

    def __init__(self,mode, screenWidth, screenHeight, pygame, step, field):
        self.image = pygame.image.load(glob.glob(f'images/pacman{mode}.*')[0])
        self.image = pygame.transform.scale(self.image, (step, step))
        self.baseImage = self.image
        self.geometry = self.image.get_rect()
        self.speed = [1, 0]
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.pygame = pygame
        self.step = step
        self.field = field
        self.savedSpeed = []

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
        if self.savedSpeed:
            if self.field[(self.geometry.y + self.step * self.savedSpeed[1]) // self.step][(self.geometry.x + self.step * self.savedSpeed[0]) // self.step] != 1:
                self.speed = self.savedSpeed
                self.savedSpeed = []
                if self.speed == [0, -1]:
                    self.image = pygame.transform.rotate(self.baseImage, 90)
                elif self.speed == [0, 1]:
                    self.image = pygame.transform.rotate(self.baseImage, 270)
                elif self.speed == [-1, 0]:
                    self.image = pygame.transform.rotate(self.baseImage, 180)
                else:
                    self.image = pygame.transform.rotate(self.baseImage, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    if self.field[(self.geometry.y + self.step * -1) // self.step][self.geometry.x // self.step] != 1:
                        self.speed = [0, -1]
                        self.image = pygame.transform.rotate(self.baseImage, 90)
                    else:
                        self.savedSpeed = [0, -1]

                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if self.field[(self.geometry.y + self.step) // self.step][self.geometry.x // self.step] != 1:
                        self.speed = [0, 1]
                        self.image = pygame.transform.rotate(self.baseImage, 270)
                    else:
                        self.savedSpeed = [0, 1]

                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if self.field[self.geometry.y // self.step][(self.geometry.x + self.step * -1) // self.step] != 1:
                        self.speed = [-1, 0]
                        self.image = pygame.transform.rotate(self.baseImage, 180)
                    else:
                        self.savedSpeed = [-1, 0]

                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if self.field[self.geometry.y // self.step][(self.geometry.x + self.step) // self.step] != 1:
                        self.speed = [1, 0]
                        self.image = pygame.transform.rotate(self.baseImage, 0)
                    else:
                        self.savedSpeed = [1, 0]
        if self.field[(self.geometry.y + self.step * self.speed[1]) // self.step][(self.geometry.x + self.step * self.speed[0]) // self.step] != 1:
            self.geometry.x += self.step * self.speed[0]
            self.geometry.y += self.step * self.speed[1]
        self.check_edges()

    def collides_with(self, b):
        return self.geometry.colliderect(b.ballrect)

    def collides_with_simple(self, b):
        x1 = self.geometry.centerx
        y1 = self.geometry.centery
        x2 = b.geometry.centerx
        y2 = b.geometry.centery
        r = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return r < self.geometry.width
