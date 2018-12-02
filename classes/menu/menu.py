import pygame
import os
from pygame.locals import *


class Menu():
    def __init__(self, screen, screen_width, screen_height, pygame):
        self.screen = screen
        self.start = False
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.pygame = pygame
        self.file = 'classes/menu/music.wav'


        self.font = 'Retro.ttf'
        self.bg = pygame.image.load("classes/menu/background.jpg")


        self.scoreboard = False
        self.menu = False
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.gray = (50, 50, 50)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.yellow = (255, 255, 0)
        self.pacmanMode = ""
        self.pygame.mixer.init()
        self.pygame.mixer.music.load(self.file)

    def text_format(self, message, textFont, textSize, textColor):
        font = pygame.font.Font(textFont, textSize)
        newText = font.render(message, 0, textColor)
        return newText

    def main_menu(self):
        self.pygame.mixer.music.play(-1)
        self.menu = True
        selected = "start"

        self.bg = pygame.transform.scale(self.bg, (self.screen_width, self.screen_height))
        while self.menu:
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    self.pygame.quit()
                    quit()
                if event.type == self.pygame.KEYDOWN:
                    if event.key == self.pygame.K_UP or event.key == self.pygame.K_w:
                        selected = "start"
                    elif event.key == self.pygame.K_DOWN or event.key == self.pygame.K_s:
                        selected = "quit"
                    if event.key == self.pygame.K_RETURN:
                        if selected == "start":
                            self.start = True
                            self.menu = False
                        if selected == "quit":
                            self.menu = False
            self.screen.blit(self.bg, (0, 0))
            title = self.text_format("PACMAN", self.font, 130, self.yellow)
            if selected == "start":
                text_start = self.text_format("START", self.font, 75, self.yellow)
            else:
                text_start = self.text_format("START", self.font, 75, self.gray)
            if selected == "quit":
                text_quit = self.text_format("QUIT", self.font, 75, self.yellow)
            else:
                text_quit = self.text_format("QUIT", self.font, 75, self.gray)

            title_rect = title.get_rect()
            start_rect = text_start.get_rect()
            quit_rect = text_quit.get_rect()
            self.screen.blit(title, (self.screen_width / 2 - (title_rect[2] / 2), 80))
            self.screen.blit(text_start, (self.screen_width / 2 - (start_rect[2] / 2), 230))
            self.screen.blit(text_quit, (self.screen_width / 2 - (quit_rect[2] / 2), 330))
            self.pygame.display.flip()
            self.pygame.display.set_caption("Pacman menu")

    def score_board(self, scores):
        self.pygame.mixer.music.play(-1)
        self.scoreboard = True
        selected = "menu"
        self.bg = pygame.transform.scale(self.bg, (self.screen_width, self.screen_height))
        while self.scoreboard:
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    self.pygame.quit()
                    quit()
                if event.type == self.pygame.KEYDOWN:
                    if event.key == self.pygame.K_UP or event.key == self.pygame.K_w:
                        selected = "restart"
                    elif event.key == self.pygame.K_DOWN or event.key == self.pygame.K_s:
                        selected = "menu"
                    if event.key == self.pygame.K_RETURN:
                        if selected == "restart":
                            self.scoreboard = False
                        if selected == "menu":
                            self.scoreboard = False

            self.screen.blit(self.bg, (0, 0))
            title = self.text_format("SCORES: " + scores, self.font, 130, self.yellow)
            if selected == "start":
                text_start = self.text_format("restart", self.font, 75, self.yellow)
            else:
                text_start = self.text_format("restart", self.font, 75, self.gray)
            if selected == "menu":
                text_quit = self.text_format("menu", self.font, 75, self.yellow)
            else:
                text_quit = self.text_format("menu", self.font, 75, self.gray)

            title_rect = title.get_rect()
            start_rect = text_start.get_rect()
            quit_rect = text_quit.get_rect()
            self.screen.blit(title, (self.screen_width / 2 - (title_rect[2] / 2), 80))
            self.screen.blit(text_start, (self.screen_width / 2 - (start_rect[2] / 2), 230))
            self.screen.blit(text_quit, (self.screen_width / 2 - (quit_rect[2] / 2), 330))
            self.pygame.display.flip()
            self.pygame.display.set_caption("Pacman scoreboard")

    def game_mode(self):
        self.pygame.mixer.music.play(-1)
        self.mode = False
        selected = "pacman"
        gameMode = True
        self.bg = pygame.transform.scale(self.bg, (self.screen_width, self.screen_height))
        while gameMode:
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    self.pygame.quit()
                    quit()
                if event.type == self.pygame.KEYDOWN:
                    if event.key == self.pygame.K_DOWN or event.key == self.pygame.K_s:
                        selected = "tanks"
                    elif event.key == self.pygame.K_UP or event.key == self.pygame.K_w:
                        selected = "pacman"
                    if event.key == self.pygame.K_RETURN:
                        if selected == "tanks":
                            gameMode = False
                        if selected == "pacman":
                            gameMode = False
                            self.pacmanMode="1"

            self.screen.blit(self.bg, (0, 0))
            title = self.text_format("GAMEMODE", self.font, 130, self.yellow)
            if selected == "pacman":
                text_pacman = self.text_format("pacman", self.font, 75, self.yellow)
            else:
                text_pacman = self.text_format("pacman", self.font, 75, self.gray)
            if selected == "tanks":
                text_tanks = self.text_format("tanks", self.font, 75, self.yellow)
            else:
                text_tanks = self.text_format("tanks", self.font, 75, self.gray)

            title_rect = title.get_rect()
            pacman_rect = text_pacman.get_rect()
            tanks_rect = text_tanks.get_rect()
            self.screen.blit(title, (self.screen_width / 2 - (title_rect[2] / 2), 80))
            self.screen.blit(text_pacman, (self.screen_width / 2 - (pacman_rect[2] / 2), 230))
            self.screen.blit(text_tanks, (self.screen_width / 2 - (tanks_rect[2] / 2), 330))
            self.pygame.display.flip()
            self.pygame.display.set_caption("Pacman mode")

