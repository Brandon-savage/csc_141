import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((860, 670))  # width x height
pygame.display.set_caption("Blue Sky")

blue = (125, 200, 230)  # sky blue

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(blue)

    pygame.display.flip()

pygame.quit()
sys.exit()