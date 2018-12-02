import pygame
import glob


class gameField:

    def __init__(self, screen, width, height, mode):
        self.field = [list(map(int, i.split())) for i in open('fieldConfig.txt', 'r+').read().strip().split('\n')]
        self.gameScreen = screen
        self.screenWidth = width
        self.screenHeight = height
        self.blockWidth = width // len(self.field[0])
        self.blockHeight = height // len(self.field)
        self.image = pygame.image.load(glob.glob(f'images/block{mode}.*')[0])
        self.image = pygame.transform.scale(self.image, (self.blockWidth, self.blockHeight))

    def draw(self):
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if self.field[i][j]:
                    self.gameScreen.blit(self.image,
                                         pygame.Rect(self.blockWidth * j, self.blockHeight * i, self.blockWidth,
                                                     self.blockHeight))
