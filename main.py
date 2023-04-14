import pygame
import math

from pygame import Vector2

WIDTH = 800
HEIGHT = 600

BACKGROUND = (10, 10, 10)
WHITESMOKE = (200, 200, 200)

AB = 0
AC = 0
AD = 0
AE = 0
BD = 0
CE = 0

A = Vector2(100, 300)
C = Vector2(700, 150)
B = Vector2((A.x + C.x) / 2, (A.y + C.y) / 2)

E = Vector2(700, 450)
D = Vector2((A.x + E.x) / 2, (A.y + E.y) / 2)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    CONSOLAS = pygame.font.SysFont('Consolas', 20)

    A_POINT = CONSOLAS.render("A", True, WHITESMOKE)
    B_POINT = CONSOLAS.render("B", True, WHITESMOKE)
    C_POINT = CONSOLAS.render("C", True, WHITESMOKE)
    D_POINT = CONSOLAS.render("D", True, WHITESMOKE)
    E_POINT = CONSOLAS.render("E", True, WHITESMOKE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill(BACKGROUND)

        # Draw AB & AC
        circle_a = pygame.draw.circle(screen, WHITESMOKE, A, 7)
        pygame.draw.line(screen, WHITESMOKE, A, B, 2)
        pygame.draw.circle(screen, WHITESMOKE, B, 7)
        pygame.draw.line(screen, WHITESMOKE, B, C, 2)
        pygame.draw.circle(screen, WHITESMOKE, C, 7)

        # Draw AD & AE
        pygame.draw.line(screen, WHITESMOKE, A, D, 2)
        pygame.draw.circle(screen, WHITESMOKE, D, 7)
        pygame.draw.line(screen, WHITESMOKE, D, E, 2)
        pygame.draw.circle(screen, WHITESMOKE, E, 7)

        # Draw BD & CE
        pygame.draw.line(screen, WHITESMOKE, B, D, 2)
        pygame.draw.line(screen, WHITESMOKE, C, E, 2)

        # Draw points name
        A_TEXT = screen.blit(A_POINT, (A.x + 5, A.y - 25))
        B_TEXT = screen.blit(B_POINT, (B.x + 5, B.y - 25))
        C_TEXT = screen.blit(C_POINT, (C.x + 5, C.y - 25))
        D_TEXT = screen.blit(D_POINT, (D.x + 5, D.y - 25))
        E_TEXT = screen.blit(E_POINT, (E.x + 5, E.y - 25))

        if pygame.mouse.get_pressed()[0] and A_TEXT.collidepoint(pygame.mouse.get_pos()):
            print("Clicked !")

        pygame.display.update()


if __name__ == "__main__":
    main()
