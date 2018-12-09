import pygame
import os
from pygame.locals import *


class Menu():
    def __init__(self,screen,screen_width,screen_height,pygame):
        self.screen=screen
        self.screen_width=screen_width
        self.screen_height=screen_height
        self.pygame=pygame
        self.file='music.wav'
        self.font='Retro.ttf'
        self.bg = pygame.image.load("background.jpg")
        self.menu=False
        self.white=(255, 255, 255)
        self.black=(0, 0, 0)
        self.gray=(50, 50, 50)
        self.red=(255, 0, 0)
        self.green=(0, 255, 0)
        self.blue=(0, 0, 255)
        self.yellow=(255, 255, 0)
        self.pygame.mixer.init()
        self.pygame.mixer.music.load(self.file)

    def text_format(self,message, textFont, textSize, textColor):
        font=pygame.font.Font(textFont, textSize)
        newText=font.render(message, 0, textColor)
        return newText

    def main_menu(self):
        self.pygame.mixer.music.play(-1)
        self.menu=True
        selected="start"
        
        self.bg=pygame.transform.scale(self.bg, (self.screen_width, self.screen_height))
        while self.menu:
            for event in self.pygame.event.get():
                if event.type==self.pygame.QUIT:
                    self.pygame.quit()
                    quit()
                if event.type==self.pygame.KEYDOWN:
                    if event.key==self.pygame.K_UP:
                        selected="start"
                    elif event.key==self.pygame.K_DOWN:
                        selected="quit"
                    if event.key==self.pygame.K_RETURN:
                        if selected=="start":
                            print("Start")
                        if selected=="quit":
                            self.pygame.quit()
                            quit()
            self.screen.blit(self.bg, (0, 0))
            title=self.text_format("PACMAN", self.font, 130, self.yellow)
            if selected=="start":
                text_start=self.text_format("START", self.font, 75, self.yellow)
            else:
                text_start = self.text_format("START", self.font, 75, self.gray)
            if selected=="quit":
                text_quit=self.text_format("QUIT", self.font, 75, self.yellow)
            else:
                text_quit = self.text_format("QUIT", self.font, 75, self.gray)

            title_rect=title.get_rect()
            start_rect=text_start.get_rect()
            quit_rect=text_quit.get_rect()
            self.screen.blit(title, (self.screen_width/2 - (title_rect[2]/2), 80))
            self.screen.blit(text_start, (self.screen_width/2 - (start_rect[2]/2), 230))
            self.screen.blit(text_quit, (self.screen_width/2 - (quit_rect[2]/2), 330))
            self.pygame.display.update()
            self.pygame.display.set_caption("Pacman menu")


pygame.init()
screen=pygame.display.set_mode((800,800))
pacman_menu=Menu(screen,800,800,pygame)
pacman_menu.main_menu()
