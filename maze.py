from pygame import Surface
from constantes import *
pygame.init()

window = Surface(DIMENSIONS)
DIMENSIONS = pygame.display.set_mode((800, 800))
image_wall = "images/mur.png"
image_start = "images/start.png"
image_goal = "images/goal.jpg"
image_mac = "images/Gardien.png"
image_ether = "images/ether.png"
image_aiguille = "images/aiguille.png"
image_seringue = "images/seringue.png"
image_gardien = "images/Gardien.png"
objects = ["images/ether.png", "images/seringue.png", "images/tube_plastique.png"]


class Labi:
    def __init__(self, file):
        self.structure_map = []
        with open(file, "r") as f:
            structure_level = []
            for line in f:
                f.read()
                line_level = []
                for sprite in line:
                    if sprite != '\n':
                        line_level.append(sprite)
                structure_level.append(line_level)
            self.structure_map = structure_level

    def readmap(self):
       self.list_position_wall = []
       self.start_pos = []
       self.finish_pos =[]
       self.object_pos = []

    def display_the_maze(self):
        num_line = 0
        for line in self.structure_map:
            num_case = 0
            for sprite in line:
                if sprite == '#':
                    wall = pygame.image.load(image_wall).convert_alpha()
                    position_wall = wall.get_rect()
                    position_wall.x = num_case * SPRITE_SIZE
                    position_wall.y = num_line * SPRITE_SIZE
                    self.list_position_wall.append(position_wall)
                if sprite == 's':
                    start = pygame.image.load(image_start).convert_alpha()
                    start_position = start.get_rect()
                    start_position.x = num_case * SPRITE_SIZE
                    start_position.y = num_line * SPRITE_SIZE
                    self.start_pos.append(start_position)
                if sprite == 'G':
                    guardian = pygame.image.load(image_gardien).convert_alpha()
                    finish_position = guardian.get_rect()
                    finish_position.x = num_case * SPRITE_SIZE
                    finish_position.y = num_line * SPRITE_SIZE
                    self.finish_pos.append(finish_position)
                if sprite == " ":
                    objects = pygame.image.load(objects[0]).convert_alpha()
                    position_objet = objects.get_rect()
                    position_objet.x = num_case * SPRITE_SIZE
                    position_objet.y = num_line * SPRITE_SIZE
                    self.object_pos.append(position_objet)



