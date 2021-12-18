import pygame

ALPHA = (0, 255, 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.movex = 0
        self.movey = 0
        self.images = []

        img = pygame.image.load('Scr/Img/mapa_prototipo.png')  # Loads the image

        img.convert_alpha()
        img.set_colorkey(ALPHA)
        self.images.append(img)

        self.image = self.images[0]  # Defines my sprite
        self.rect = self.image.get_rect()

    def control(self, x, y):
        self.movex = x
        self.movey = y

    def update(self):
        # Updates the coordinates of fofolete
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
