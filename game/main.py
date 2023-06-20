import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption("Pygame training")
icon = pygame.image.load("game/taing.png")
pygame.display.set_icon(icon)


run = True
while run:

    # screen.fill((142, 50, 50))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
             if event.key == pygame.K_a:
                
                screen.fill((0,255,0))

