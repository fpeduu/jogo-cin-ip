import pygame
from pygame.locals import *
from Prototype.Player_logic import Player
from Prototype.Collectable import Coin

pygame.init()

''' Standards  '''
BLACK = (0, 0, 0)
screen_size = (960, 960)
pixel = 10
key = 0

''' Gets the background image '''

screen = pygame.display.set_mode(screen_size)
backdropbox = screen.get_rect()
pygame.display.set_caption('Sprites')

''' Gets the classes'''
all_sprites = pygame.sprite.Group()
player = Player()
coin = Coin()
''' Creation the group of sprites'''
all_sprites.add(player)
all_sprites.add(coin)

player_x = player.rect.x = 400  # Initial position
player_y = player.rect.y = 400
coordinates_player = (player_x, player_y)

coin_x = coin.rect.x = 480  # Initial position
coin_y = coin.rect.y = 480
coordinates_coin = (coin_x, coin_y)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_DOWN]:

        if pygame.key.get_pressed()[K_RIGHT]:
            player.control(-pixel / (2 ** 0.5), -pixel / (2 ** 0.5))

        elif pygame.key.get_pressed()[K_LEFT]:
            player.control(pixel / (2 ** 0.5), -pixel / (2 ** 0.5))

        else:
            player.control(0, -pixel)

    elif pygame.key.get_pressed()[K_UP]:

        if pygame.key.get_pressed()[K_RIGHT]:
            player.control(-pixel / (2 ** 0.5), pixel / (2 ** 0.5))

        elif pygame.key.get_pressed()[K_LEFT]:
            player.control(pixel / (2 ** 0.5), pixel / (2 ** 0.5))

        else:
            player.control(0, pixel)

    elif pygame.key.get_pressed()[K_LEFT]:
        player.control(pixel, 0)

    elif pygame.key.get_pressed()[K_RIGHT]:
        player.control(-pixel, 0)

    print(player.rect.x, player.rect.y)
    ''' Updates the screen '''

    player.update()
    coin.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    pygame.time.Clock().tick(20)
