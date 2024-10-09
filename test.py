import pygame
import random

pygame.init()

main_screen = pygame.display.set_mode((1000, 720))

test_clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        pygame.display.update()
        test_clock.tick(60)