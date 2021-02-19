import pygame

from pygame.locals import K_ESCAPE, KEYDOWN, K_UP, K_RIGHT, QUIT, K_LEFT, K_RETURN, K_KP_ENTER, K_CLEAR


pygame.init()
# Paramètres de la fenêtre
WIDTH = 800
HEIGHT = 800
DIMENSIONS = (WIDTH, HEIGHT)
NBR_SPRITE = 15
SPRITE_SIZE = 30
WINDOW_TITLE = "Escape Game"
SIDE_WINDOW = NBR_SPRITE * SPRITE_SIZE


