import pygame
import game


def main(display):
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.event.post(pygame.Event(pygame.QUIT))
                running = not running
            elif event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
                game.run(display)