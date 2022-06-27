import pygame

pygame.init()
pygame.font.init()
pygame.display.set_caption("Schiffeversenken")
bigtext = pygame.font.SysFont("futura", 60)
welcometexter = pygame.font.SysFont("brushscript", 100)
Playerturntext = pygame.font.SysFont("futura", 40)
Timertextfont = pygame.font.SysFont("futura", 30)
continuequit = pygame.font.SysFont("futura", 30)
clock = pygame.time.Clock()


# global variables
SQ_SIZE = 35
H_MARGIN = SQ_SIZE * 4  # horizontal
V_MARGIN = SQ_SIZE  # vertical


# Size of Window
WIDTH = SQ_SIZE * 10 * 2 + H_MARGIN
HEIGHT = SQ_SIZE * 10 * 2 + V_MARGIN
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# colors
GREY = (30, 30, 30)
WHITE = (40, 130, 50)
GREEN = (90, 80, 80)
RED = (250, 50, 100)



def Startscreen():
    starting = True
    while starting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_s:
                    from mainsmall import Gamesmall
                    starting = False
                    Gamesmall()
                if event.key == pygame.K_n:
                    from main_final import Game
                    starting = False
                    Game()
        SCREEN.fill(GREY)

        welcometext = "Welcome to Battleships!"
        welcometextbox = welcometexter.render(welcometext, False, RED)
        SCREEN.blit(welcometextbox, (WIDTH // 2 - 390, HEIGHT // 2 - 200))

        textstart = "Get ready Player 1:"
        textboxstart = bigtext.render(textstart, False, WHITE, GREY)
        SCREEN.blit(textboxstart, (WIDTH // 2 - 270, HEIGHT // 2 - 50))

        textnextplayercq = "Press S to start Small or N to Start Normal"
        textboxcontinue = continuequit.render(textnextplayercq, False, GREY, WHITE)
        SCREEN.blit(textboxcontinue, (WIDTH // 2 - 290, HEIGHT // 2 + 50))
        pygame.display.update()
        clock.tick(5)

Startscreen()










