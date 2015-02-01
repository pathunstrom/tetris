import pygame


def run(display):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = not running


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600, 600))

    run(screen)