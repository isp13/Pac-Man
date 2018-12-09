import pygame
import glob
from classes.seed.seed import seed



class gameField:

    def __init__(self, screen, width, height, mode):
        self.field = [list(map(int, i.split())) for i in open('fieldConfig.txt', 'r+').read().strip().split('\n')]
        self.gameScreen = screen
        self.screenWidth = width
        self.screenHeight = height
        self.blockWidth = width // len(self.field[0])
        self.blockHeight = height // len(self.field)
        self.image = pygame.image.load(glob.glob(f'images/block{mode}.*')[0])
        self.seedImage = pygame.image.load(glob.glob(f'images/seed{mode}.*')[0])
        self.bigSeed = pygame.image.load(glob.glob(f'images/bigSeed{mode}.*')[0])
        # SCALING ALL THE IMAGES FFS!
        self.image = pygame.image.load(glob.glob(f'images/block{mode}.*')[0])
        self.image = pygame.transform.scale(self.image, (self.blockWidth, self.blockHeight))

        # SMALL SEED SPRITE
        self.smallSeedImage = pygame.transform.scale(self.seedImage, (int(self.blockWidth * 0.35), int(self.blockHeight * 0.35)))
        self.smallSeedRect = self.smallSeedImage.get_rect().size

        # BIG SEED SPRITE
        self.bigSeedImage = pygame.transform.scale(self.bigSeed, (int(self.blockWidth * 0.5), int(self.blockHeight * 0.5)))
        self.bigSeedRect = self.bigSeedImage.get_rect().size

    def draw(self):
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                if self.field[i][j] == 1:
                    self.gameScreen.blit(self.image, pygame.Rect(self.blockWidth*j, self.blockHeight*i, self.blockWidth, self.blockHeight))
                elif self.field[i][j] == 2:
                    self.gameScreen.blit(self.smallSeedImage, 
                        pygame.Rect(self.blockWidth*j + self.blockWidth // 2 - self.smallSeedRect[0] // 2,
                        self.blockHeight*i + self.blockHeight // 2 - self.smallSeedRect[1] // 2, self.blockWidth, self.blockHeight))
                elif self.field[i][j] == 3:
                    self.gameScreen.blit(self.bigSeedImage,
                        pygame.Rect(self.blockWidth*j + self.blockWidth // 2 - self.bigSeedRect[0] // 2,
                        self.blockHeight*i + self.blockHeight // 2 - self.bigSeedRect[1] // 2, self.blockWidth, self.blockHeight))
                    
    
