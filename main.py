import pygame
import sys
from math import sqrt

from classes.pacman.ghost import *
from classes.pacman.pacman import *
from classes.gameField.gameField import *
from classes.menu.menu import *

size = width, height = 800, 900  # Размеры экрана
black = 0, 0, 0  # RGB черного цвета


def main():
    global size, width, height
    pygame.init()
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)  # pygame.RESIZABLE - позволяет окну изменять размер
    # menu.score_board(str(100))
    MainGame = True
    while MainGame:
        menu = Menu(screen, width, height, pygame)
        menu.main_menu()
        if menu.start:
            menu.game_mode()
            field = gameField(screen, width, height - 100, menu.pacmanMode)
            pacman = Pacman(screen, menu.pacmanMode, width, height, pygame, field.blockWidth, field.field)
            ghosts = []
            for i in range(1):
                for j in range(1):
                    ghost = Ghost(width, height, pygame, field.blockWidth, field.field.copy(), menu.pacmanMode)
                    ghost.set_center_position(width // 2 + field.blockWidth * i,
                                              width // 2 + field.blockWidth * j*2)
                    ghosts.append(ghost)
            pacman.set_position(field.blockWidth, field.blockWidth)
            pygame.display.set_caption("Pacman")
            timer = 0

            while not pacman.game_over:
                pacman.move()
                screen.fill(black)
                screen.blit(pacman.image, pacman.geometry)
                field.draw()
                for i in range(0, len(ghosts)):
                    ghosts[i].logic(pacman, ghosts)
                    if pacman.fear_mode:
                        ghosts[i].image = ghosts[i].fearImage
                    else:
                        ghosts[i].image = ghosts[i].baseImage
                    screen.blit(ghosts[i].image, ghosts[i].geometry)
                    if pacman.collides_with(ghosts[i]):
                        if not pacman.fear_mode:
                            pacman.health -= 1
                            pacman.set_position(field.blockWidth, field.blockWidth)
                            ghosts[i].set_center_position(width // 2 + field.blockWidth * i, width // 2 + field.blockWidth * j * 2)
                        else:
                            ghosts.pop(i)
                            pacman.score += 200
                            break
                        # pacman.set_position(field.blockWidth, field.blockWidth)
                if pacman.health == 0:
                    menu.score_board(str(pacman.score))
                    MainGame = menu.start
                    menu.menu = True
                    break
                field.field = pacman.field
                screen.blit(pacman.image, pacman.geometry)
                pacman.set_health()
                pacman.set_score()
                pygame.display.flip()
                pygame.time.wait(180)
                timer += 1
                if timer % 15 == 0 and len(ghosts) < 4:
                    timer = 0
                    for i in range(1):
                        for j in range(1):
                            ghost = Ghost(width, height, pygame, field.blockWidth, field.field, menu.pacmanMode)
                            ghost.set_center_position(width // 2 + field.blockWidth * i,
                                                      width // 2 + field.blockWidth * j * 2)
                            ghosts.append(ghost)

        else:
            sys.exit()


if __name__ == "__main__":
    main()
