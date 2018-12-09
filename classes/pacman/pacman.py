import pygame
import glob
from classes.gameField.gameField import *
from classes.menu.menu import *

class Pacman():
    class InterfaceText:
        def __init__(self, text, size, x=0, y=0, color=(255, 255, 255)):
            self.position = (x, y)
            self.text = text
            self.size = size
            self.color = color
            self.font = pygame.font.Font('classes/menu/Retro.ttf', self.size)
            self.surface = self.font.render(self.text, False, self.color)
            self.pointsTotal=0
            self.pointsLeft=0

        def update_text(self, new_text):
            self.text = new_text
            self.surface = self.font.render(self.text, False, self.color)

        def update_position(self, x, y):
            self.position = (x, y)

        def get_text_size(self):
            r = self.surface.get_rect()
            return [r.width, r.height]

        def draw(self, screen):
            screen.blit(self.surface, self.position)

    game_over = False

    def __init__(self, screen, mode, screenWidth, screenHeight, pygame, step, field):
        self.image = pygame.image.load(glob.glob(f'images/pacman{mode}.*')[0])
        self.image = pygame.transform.scale(self.image, (step, step))
        self.baseImage = self.image
        self.geometry = self.image.get_rect()
        self.speed = [1, 0]
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.pygame = pygame
        self.step = step
        self.timeFearStart = pygame.time.get_ticks()
        self.mode = mode
        self.screen = screen
        self.field = field
        self.score = 0
        self.fear_mode = False
        self.health = 3
        self.screenHeight = screenHeight
        self.screenWidth = screenWidth
        self.savedSpeed = []
        self.pointsTotal=0
        self.pointsLeft=0
        for blocks in self.field:
                self.pointsTotal+=str(blocks).count("2")
                #pointsTotal+=blocks.count("3")

    def set_center_position(self, x, y):
        self.geometry.center = (x, y)

    def set_position(self, x, y):
        self.geometry.x = x
        self.geometry.y = y

    def set_health(self):
        for bar in range(self.health):
            image = pygame.image.load(glob.glob(f'images/pacman{self.mode}.*')[0])
            image = pygame.transform.scale(image, (self.step, self.step))
            geometry = image.get_rect()
            geometry.x += 50 + self.step * bar
            geometry.bottom = self.screenHeight - 50 + self.step // 2
            self.screen.blit(image, geometry)

    def set_score(self):
        text = self.InterfaceText(f"score: {self.score}", 75)
        text.update_position(self.screenWidth - self.screenHeight // 3, self.screenHeight - 90)
        text.draw(self.screen)

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
                        self.savedSpeed = []
                        self.image = pygame.transform.rotate(self.baseImage, 90)
                    else:
                        self.savedSpeed = [0, -1]

                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if self.field[(self.geometry.y + self.step) // self.step][self.geometry.x // self.step] != 1:
                        self.speed = [0, 1]
                        self.savedSpeed = []
                        self.image = pygame.transform.rotate(self.baseImage, 270)
                    else:
                        self.savedSpeed = [0, 1]

                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if self.field[self.geometry.y // self.step][(self.geometry.x + self.step * -1) // self.step] != 1:
                        self.speed = [-1, 0]
                        self.savedSpeed = []
                        self.image = pygame.transform.rotate(self.baseImage, 180)
                    else:
                        self.savedSpeed = [-1, 0]

                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if self.field[self.geometry.y // self.step][(self.geometry.x + self.step) // self.step] != 1:
                        self.speed = [1, 0]
                        self.savedSpeed = []
                        self.image = pygame.transform.rotate(self.baseImage, 0)
                    else:
                        self.savedSpeed = [1, 0]

        if pygame.time.get_ticks() - self.timeFearStart >= 5000 and self.fear_mode:
            self.fear_mode = False
        # check small seed
        if self.field[(self.geometry.y + self.step * self.speed[1]) // self.step][
            (self.geometry.x + self.step * self.speed[0]) // self.step] == 2:
            self.score += 10
            ##
            print("point eating")
            self.pointsTotal-=1
            print(self.pointsTotal)
            if self.pointsTotal<=0:
                game_over=False
                
                
                



            
                
            ##
            self.field[(self.geometry.y + self.step * self.speed[1]) // self.step][
                (self.geometry.x + self.step * self.speed[0]) // self.step] = 0
        # check big seed
        if self.field[(self.geometry.y + self.step * self.speed[1]) // self.step][
            (self.geometry.x + self.step * self.speed[0]) // self.step] == 3:
            self.timeFearStart = pygame.time.get_ticks()
            self.fear_mode = True
            self.field[(self.geometry.y + self.step * self.speed[1]) // self.step][
                (self.geometry.x + self.step * self.speed[0]) // self.step] = 0
        if self.check_walls():
            self.geometry.x += self.step * self.speed[0]
            self.geometry.y += self.step * self.speed[1]
        self.check_edges()

    def collides_with(self, b):
        return self.geometry.colliderect(b.ballrect)

    def check_walls(self):
        if self.field[(self.geometry.y + self.step * self.speed[1]) // self.step][(self.geometry.x + self.step * self.speed[0]) // self.step] != 1:
            return True
        return False

    def collides_with(self, b):
        x1 = self.geometry.centerx
        y1 = self.geometry.centery
        x2 = b.geometry.centerx
        y2 = b.geometry.centery
        r = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2)
        return r < self.geometry.width
