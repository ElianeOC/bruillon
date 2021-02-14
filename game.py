from constantes import *
from maze import *

"""class MacGy():
    def __init__(self, mac, lab) :
        self.mac = pygame.image.load("images/MacGyver.png").convert_alpha()
        self.case_x = 0
        self.case_y = 0
        self.pos_X = 0
        self.pos_Y = 0
        self.lab = lab
        self.level = []

    def move(self, direction):
        if direction == 'right':
            # on reste dans l'ecran
            if self.case_x < (NBR_SPRITE - 1) :
                if self.lab.structure_map[self.case_y][self.case_x + 1] != '#' :
                    self.case_x += 1
                    self.pos_X = self.case_x * SPRITE_SIZE
        if direction == 'left':
            if self.case_x > 0:
                if self.lab.structure_map[self.case_y][self.case_x] != '#' :
                    self.case_x -= 1
                    self.pos_X = self.case_x * SPRITE_SIZE

        if direction == 'Up' :
            if self.case_y > 0 :
                if self.lab.structure_map[self.case_y - 1][self.case_x] != '#' :
                    self.case_y -= 1
                    self.pos_Y = self.case_y * SPRITE_SIZE

        if direction == 'Down' :
            if self.case_y <= (SIDE_WINDOW) :
                if self.lab.structure_map[self.case_y + 2][self.case_x] != '#' :
                    self.case_y += 2
                    self.pos_Y = self.case_y * SPRITE_SIZE"""