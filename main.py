from maze import *
pygame.init()


HOME = pygame.image.load("images/acceuil.png").convert()
BACKGROUND = pygame.image.load("images/fond.jpg").convert()
pygame.key.set_repeat()
main_loop = True
while main_loop:
    WINDOW.blit(pygame.transform.scale(HOME, (800, 800)), (0, 0))
    # print text on the screen
    FONT = pygame.font.Font(None, 50)
    TEXT_HOME = FONT.render("Press Enter to continue or ECHAP to quit", 1, (200, 200, 200))
    WINDOW.blit(TEXT_HOME, (50, 400))
    # refersh the screen
    pygame.display.flip()
    pygame.display.flip()
    run_home = True
    run_game = True
    # run_home loop
    while run_home:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                main_loop = False
                run_home = False
                run_game = False
            # if user presses "Enter", the maze starts
            elif event.type == KEYDOWN and event.key == K_RETURN:
                run_home = False
            elif event.type == K_KP_ENTER and event.key == K_CLEAR:
                run_home = False
                run_game = True
    pygame.display.flip()

run_game = True

while run_game:
    labi = Labi('self')
    labi.__init__('file')
    labi.display_the_maze()
    pygame.display.flip()
    WINDOW.blit(pygame.transform.scale(BACKGROUND, (800, 800)), (0, 0))
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
        if event.type == K_KP_ENTER and event.key == K_CLEAR:
            run_game = True
    pygame.display.flip()




