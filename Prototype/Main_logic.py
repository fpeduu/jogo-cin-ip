import pygame, random
from pygame.locals import *
from Prototype.Player_logic import Player
from Prototype.Collectable import Coin

pygame.init()

''' Standards  '''
BLACK = (0, 0, 0)
screen_size = (960, 960)
pixel = 10
key = 0

''' Collision function '''
def collision(p1, p2):
    return abs(p1[0] - p2[0]) <= 20 and abs(p1[1] - p2[1]) <= 20

''' Gets the background image '''
background = pygame.image.load('Scr/Img/mapa_prototipo.png')
background = pygame.transform.scale(background, screen_size)

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

player_x = player.rect.x = 100  # Initial position
player_y = player.rect.y = 100
coordinates_player = (player_x, player_y)

coin_x = coin.rect.x = 0  # Initial position
coin_y = coin.rect.y = 0
coordinates_coin = (coin_x, coin_y)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:  # Gets input
            key = event.key
            if key == K_LEFT:
                player.control(-pixel, 0)


            elif key == K_RIGHT:
                player.control(pixel, 0)

            elif key == K_UP:
                if pygame.key.get_pressed()[K_LEFT]:
                    player.control(-pixel / (2 ** 0.5), -pixel / (2 ** 0.5))

                elif pygame.key.get_pressed()[K_RIGHT]:
                    player.control(pixel / (2 ** 0.5), -pixel / (2 ** 0.5))
                else:
                    player.control(0, -pixel)
            elif key == K_DOWN:
                if pygame.key.get_pressed()[K_LEFT]:
                    player.control(-pixel / (2 ** 0.5), pixel / (2 ** 0.5))

                elif pygame.key.get_pressed()[K_RIGHT]:
                    player.control(pixel / (2 ** 0.5), pixel / (2 ** 0.5))
                else:
                    player.control(0, pixel)

                ''' Movement '''

        elif event.type == KEYUP:
            player.control(0, 0)

    player_x = player.rect.x
    player_y = player.rect.y
    coordinates_player = (player_x, player_y)

    coin_x = coin.rect.x
    coin_y = coin.rect.y
    coordinates_coin = (coin_x, coin_y)

    if collision(coordinates_coin, coordinates_player):  # Implements collision
        new_x = random.randint(0, screen_size[0])
        new_x = int(new_x / pixel) * 10
        new_y = random.randint(0, screen_size[1])
        new_y = int(new_y / pixel) * 10
        coin.new_pos(new_x, new_y)

    ''' Updates the screen '''
    screen.blit(background, backdropbox)
    player.update()
    coin.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    pygame.time.Clock().tick(20)
