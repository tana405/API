import pygame
import sys
import os
import requests

'''https://static-maps.yandex.ru/1.x/?ll=65.369564,55.439279&spn=0.05045,0.00619&l=map'''


class Map:
    # создание поля
    def __init__(self):
        self.coords1 = 65.369564
        self.coords2 = 55.439279
        self.coords3 = 0.05045
        self.coords4 = 0.00619
        self.type = "map"
        self.map_file = ''

    def ll_format(self):
        v = 'https://static-maps.yandex.ru/1.x/?ll={0},{1}&spn={2},{3}&l={4}'.format(str(self.coords1),
                                                                                     str(self.coords2),
                                                                                     str(self.coords3),
                                                                                     str(self.coords4),
                                                                                     self.type)
        return v

    def load_map(self):
        self.map_file = "map.png"
        try:
            map_request = self.ll_format()
            response = requests.get(map_request)
            with open(self.map_file, "wb") as file:
                file.write(response.content)
        except IOError as ex:
            print("Ошибка записи временного файла:", ex)
            sys.exit(1)
        except:
            print('ошибка')
            sys.exit(2)
        return self.map_file

    def main(self):
        pygame.init()
        pygame.display.set_caption('Инициализация API')
        size = width, height = 600, 450
        screen = pygame.display.set_mode(size)
        # mp = Map()
        w = True
        clock = pygame.time.Clock()
        while w:
            for event in pygame.event.get():
            # event = pygame.event.wait()
                if event.type == pygame.QUIT:
                    w = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.coords1 -= 0.0001
            elif keys[pygame.K_RIGHT]:
                self.coords1 += 0.0001
            elif keys[pygame.K_UP]:
                self.coords2 += 0.0001
            elif keys[pygame.K_DOWN]:
                self.coords2 -= 0.0001
            elif keys[pygame.K_PAGEUP]:
                print(8)
                #self.coords3 += 0.0001
                self.coords4 += 0.1
            elif keys[pygame.K_PAGEDOWN]:
                print(4)
                #self.coords3 -= 0.0001
                self.coords4 -= 0.1
            self.map_file = self.load_map()
            screen.blit(pygame.image.load(self.map_file), (0, 0))
            pygame.display.flip()
        pygame.quit()
        os.remove(self.map_file)
        clock.tick(70)


if __name__ == "__main__":
    map = Map()
    map.main()
