import pygame
import sys
import os
import request

'''https://static-maps.yandex.ru/1.x/?ll=65.369564,55.439279&spn=0.05045,0.00619&l=map'''


class Map:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.coords1 = 65.369564
        self.coords2 = 55.439279
        self.coords3 = 0.05045
        self.coords4 = 0.00619
        self.type = "map"

    def ll_format(self):
        v = 'https://static-maps.yandex.ru/1.x/?ll={0},{1}&spn={2},{3}&l={4}'.format(str(self.coords1),
                                                                                     str(self.coords2),
                                                                                     str(self.coords3),
                                                                                     str(self.coords4),
                                                                                     self.type)
        return v

    def load_map(self):
        pass


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Инициализация API')
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)

    board = Map(5, 5)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        pygame.display.flip()
    pygame.quit()
