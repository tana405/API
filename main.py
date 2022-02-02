import pygame
import sys
import os

'''https://yandex.ru/maps/53/kurgan/?ll=65.369564%2C55.439279&z=13.57'''


class Map:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.coords1 = 65.369564
        self.coords2 = 55.439279
        self.coords3 = 13.57


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Инициализация API')
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)

    board = Board(5, 5)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        pygame.display.flip()
    pygame.quit()

