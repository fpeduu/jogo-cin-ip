import pygame

from config import *

class Mapa:
    def __init__(self, arquivo):
        # usar o arquivo '.txt' para definir o mapa
        self.data = []
        with open(arquivo, 'rt') as texto:
            for line in texto:
                self.data.append(line.strip())
        # definir o tamanho do mapa:
        self.largura_tile = len(self.data[0])
        self.altura_tile = len(self.data)
        self.largura = self.largura_tile * TAM_TILE
        self.altura = self.altura_tile * TAM_TILE

class Camera:
    def __init__(self, largura, altura):
        self.camera = pygame.Rect(0, 0, largura, altura) # definindo q a camera, ou seja, o espaco apresentado na tela, sera um retangulo de tamanho X
        self.largura = largura
        self.altura = altura
    
    def aplicacao(self, objeto):
        return objeto.rect.move(self.camera.topleft) # ativar o funcionamento da camera

    def update(self,jogador): # definir que durante o loop do jogo, a camara se fixara no jogador
        # na movimentacao da camera, o jogado ficara no meio da tela
        x = -jogador.rect.x + int(LARGURA/2) 
        y = -jogador.rect.y + int(ALTURA/2)

        # definindo o limite do scroll da camera
        x = min(0,x)
        x = max(-(self.largura - LARGURA), x)
        
        y = min(0,y)
        y = max(-(self.altura - ALTURA), y)

        self.camera = pygame.Rect(x, y, self.largura, self.altura)


