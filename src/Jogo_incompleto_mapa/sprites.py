import pygame
from config import *

class Jogador(pygame.sprite.Sprite):
    def __init__(self, jogo, x, y):
        self.groups = jogo.todos_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.jogo = jogo
        self.imagem = pygame.image.load('fofo.jpg')
        self.imagem = pygame.transform.scale(self.imagem, (TAM_TILE,TAM_TILE))
        self.rect = pygame.Rect(x * TAM_TILE, y * TAM_TILE, TAM_TILE, TAM_TILE)
        self.vx, self.vy = 0, 0
        self.x = x * TAM_TILE
        self.y = y * TAM_TILE

    def render(self, screen):
        screen.blit(self.image, self.rect)

    def movimento(self): # movimento suave da personagem
        self.vx, self.vy = 0, 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vx = -VELOCIDADE
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vx = VELOCIDADE
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.vy = -VELOCIDADE
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.vy = VELOCIDADE
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071

    def colisoes(self, direcao):
        if direcao == 'x':
            hits = pygame.sprite.spritecollide(self, self.jogo.paredes, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if direcao == 'y':
            hits = pygame.sprite.spritecollide(self, self.jogo.paredes, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y

    def update(self):
        self.movimento()
        self.x += self.vx * self.jogo.dt
        self.y += self.vy * self.jogo.dt
        self.rect.x = self.x
        self.colisoes('x')
        self.rect.y = self.y
        self.colisoes('y')

class Parede(pygame.sprite.Sprite):

    def __init__(self, jogo, x, y, img_tile):
        self.groups = jogo.todos_sprites, jogo.paredes
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.jogo = jogo        

        self.imagem = pygame.image.load(img_tile)
        self.imagem = pygame.transform.scale(self.imagem, (TAM_TILE,TAM_TILE))
        self.rect = pygame.Rect(x * TAM_TILE, y * TAM_TILE, TAM_TILE, TAM_TILE)
        
        self.x = x
        self.y = y
        self.rect.x = x * TAM_TILE
        self.rect.y = y * TAM_TILE

    def render(self, screen):
        screen.blit(self.image, self.rect)

    

