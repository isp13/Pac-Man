import pygame
import os
from pygame.locals import *

def text_format(message, textFont, textSize, textColor):
    font=pygame.font.Font(textFont, textSize)
    newText=font.render(message, 0, textColor)
    return newText

os.environ['SDL_VIDEO_CENTERED'] = '1'
screen_width=800
screen_height=600
screen=pygame.display.set_mode((screen_width, screen_height))
# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)

clock = pygame.time.Clock()
FPS=30


file = 'music.wav'
font = "Retro.ttf"

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)

def main_menu():
    pygame.mixer.music.play(-1)


    menu=True
    selected="start"
    bg = pygame.image.load("background.jpg")
    bg=pygame.transform.scale(bg, (800, 600))
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        #начать игру
                    if selected=="quit":
                        pygame.quit()
                        quit()

        screen.blit(bg, (0, 0))
        title=text_format("PACMAN", font, 130, yellow)
        if selected=="start":
            text_start=text_format("START", font, 75, yellow)
        else:
            text_start = text_format("START", font, 75, gray)
        if selected=="quit":
            text_quit=text_format("QUIT", font, 75, yellow)
        else:
            text_quit = text_format("QUIT", font, 75, gray)

        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()

        
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 230))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 330))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Pacman menu")

main_menu()
pygame.quit()
quit()