from pygame import image, init, key, transform, font, display, \
    event, time

from maze import *

init()

window = pygame.display.get_surface()
pos_x = (NBR_SPRITE, SPRITE_SIZE)
pos_y = (NBR_SPRITE, SPRITE_SIZE)
HOME = image.load("images/acceuil.png")
BACKGROUND = image.load("images/fond.jpg")

key.set_repeat()
main_loop = True
while main_loop:
    window.blit(transform.scale(HOME, (800, 800)), (0, 0))
    # print text on the screen
    FONT = font.Font(None, 50)
    TEXT_HOME = FONT.render("Press Enter to continue or ECHAP to quit", True, (200, 200, 200))
    window.blit(TEXT_HOME, (50, 400))
    # refersh the screen
    display.flip()
    run_home = True
    run_game = True
    # run_home loop
    while run_home:
        time.Clock().tick(30)
        for e in event.get():
            if e.type == QUIT or e.type == KEYDOWN and e.key == K_ESCAPE:
                main_loop = False
                run_home = False
                run_game = False
            # if user presses "Enter", the maze starts
            elif e.type == KEYDOWN and e.key == K_RETURN:
                run_home = False
            elif e.type == K_KP_ENTER and e.key == K_CLEAR:
                run_home = False
                run_game = True
    display.flip()

    run_game = True
    while run_game:
        labi = Labi('my_map')
        labi.display_the_maze()
        display.flip()
        wall = pygame.image.load("images/mur.png")
        window.blit(wall, (30, 30))
        time.Clock().tick(30)
        for e in event.get():
            if e.type == K_KP_ENTER and e.key == K_CLEAR:
                run_game = True
        display.flip()
