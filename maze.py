from constantes import *

pygame.init()

WINDOW = pygame.display.set_mode(SCREEN_SIZE)

WALL = pygame.image.load("images/mur.png").convert()
START = pygame.image.load("images/start.png").convert()
GOAL = pygame.image.load("images/goal.jpg").convert()
mac = pygame.image.load("images/Gardien.png").convert
ETHER = pygame.image.load("images/ether.png").convert()
AIGUILLE = pygame.image.load("images/aiguille.png").convert()
SERINGUE = pygame.image.load("images/seringue.png").convert()
laby = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", ".", "A"],
    [".", "#", "#", "#", "#", "#", "#", "#", ".", "#", ".", ".", ".", ".", "."],
    [".", "#", "#", ".", ".", ".", "#", ".", ".", ".", "#", "#", "s", ".", "#"],
    ["#", "#", "#", ".", "#", ".", ".", ".", "#", ".", "#", ".", ".", ".", "."],
    ["#", "#", "#", ".", "#", "#", ".", "#", ".", ".", ".", ".", "#", "#", "."],
    ["#", "#", "#", ".", ".", "e", "#", "#", "#", "#", "#", "#", ".", ".", "."],
    [".", "#", "#", "#", ".", ".", "#", ".", ".", ".", "#", "#", "#", ".", "."],
    ["#", "#", "#", "#", "#", ".", ".", ".", "#", ".", ".", ".", "#", ".", "."],
    ["#", "#", ".", ".", ".", ".", "#", "#", "#", "#", "#", ".", ".", ".", "#"],
    ["#", "#", ".", "#", ".", "#", "#", "#", "#", "#", "W", "#", ".", "#", "#"],
    ["#", "#", ".", "i", "#", "#", ".", ".", ".", "#", "#", ".", ".", "#", "#"],
    [".", "#", "#", ".", "#", ".", ".", "#", ".", ".", ".", ".", "#", "#", "#"],
    [".", ".", ".", ".", ".", "#", ".", "#", ".", ".", ".", "#", "#", "#", "#"],
    [".", "D", "#", "#", ".", ".", ".", "#", "#", ".", ".", "#", "#", "#", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
]


class Labi:
    def __init__(self, file):
      self.file = file
      self.structure_map = []
      with open("my_map", "r") as file:
            structure_level = []
            for line in file:
                print(file)
                line_level = []
                for sprite in line:
                    if sprite != '\n':
                        line_level.append(sprite)
                        structure_level.append(line_level)
                        self.structure_map = structure_level

    for line in laby:
        print(laby)

    def display_the_maze(self):
        num_line = 0
        for line in self.structure_map:
            num_case = 0
            for sprite in line:
                pos_X = num_case * SPRITE_SIZE
                pos_Y = num_line * SPRITE_SIZE
                if sprite == '#':
                    WINDOW.blit(WALL, (pos_X, pos_Y))
                if sprite == 's':
                    WINDOW.blit(START, (pos_X, pos_Y))
                if sprite == 'g':
                    WINDOW.blit(GOAL, (pos_X, pos_Y))
                if sprite == 's':
                    WINDOW.blit(SERINGUE, (pos_X, pos_Y))
                if sprite == 'e':
                    WINDOW.blit(ETHER, (pos_X, pos_Y))
                if sprite == 'i':
                    WINDOW.blit(AIGUILLE, (pos_X, pos_Y))
                    num_case = pos_X + 1
                    num_line = pos_Y + 1

class Mur(pygame.sprite.Sprite):
    def __init__(self, pos_X, pos_Y) :
         pygame.sprite.Sprite.__init__(self)
         self.wall = pygame.image.load("images/wall.png").convert()
         self.rect = self.image.get_rect()
         self.rect.pos_Y = SPRITE_SIZE * pos_Y
         self.rect.pos_X = SPRITE_SIZE * pos_X

    pygame.display.flip()
