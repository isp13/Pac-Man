import pygame
import sys
from math import sqrt
from classes.pacman.pacman import *
from classes.gameField.gameField import *
from classes.menu.menu import *

size = width, height = 800, 800  # Размеры экрана
black = 0, 0, 0  # RGB черного цвета


def main():
    global size, width, height
    pygame.init()
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)  # pygame.RESIZABLE - позволяет окну изменять размер
    menu = Menu(screen, width, height, pygame)
    # menu.score_board(str(100))
    menu.main_menu()
    if menu.start:
        menu.game_mode()
        field = gameField(screen, width, height, menu.pacmanMode)
        pacman = Pacman(menu.pacmanMode, width, height, pygame, field.blockWidth, field.field)
        pacman.set_position(field.blockWidth, field.blockWidth)
        pygame.display.set_caption("Pacman")
        while not pacman.game_over:
            pacman.move()
            screen.fill(black)
            screen.blit(pacman.image, pacman.geometry)
            field.draw()
            pygame.display.flip()
            pygame.time.wait(180)
        sys.exit()
    else:
        sys.exit()


if __name__ == "__main__":
    main()
