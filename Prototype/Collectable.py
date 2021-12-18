import pygame


AlPHA = (0, 255, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = []

        img = pygame.image.load('Scr/Img/fofolete.png')
        img.convert_alpha()
        img.set_colorkey(AlPHA)

        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def new_pos(self, new_x, new_y):
        self.rect.x = new_x
        self.rect.y = new_y
