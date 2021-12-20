import pygame, sys

from os import path

from map import *
from sprites import *
from config import *

class Jogo_principal:

    def __init__(self): # inicializaçao do pygame
        pygame.init()
        self.screen = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption('JOGO PRINCIPAL')
        self.clock = pygame.time.Clock()
        self.load_mapa()
       

        
        
    def load_mapa(self): # inicializar o mapa
        pasta = path.dirname(__file__) # especificar que a pasta a qual o arquivo 'mapa.txt' esta e a mesma do 'main.py'
        mapa_texto = path.join(pasta, 'map_txt.txt') #
        self.map = Mapa(mapa_texto)

    def setup(self): # setup do jogo
        # agrupar todos os sprites do jogo
        self.todos_sprites = pygame.sprite.Group() 
        self.paredes = pygame.sprite.Group()

        
        
        for linha, tiles in enumerate(self.map.data):
            for coluna, tile in enumerate(tiles):
                if tile == 'P':
                    Parede(self,coluna,linha,'src/img/parede_alt.png')
                if tile == 'p':
                    Parede(self,coluna,linha,'src/img/parede_cont.png')
                if tile == 'K':
                    Parede(self,coluna,linha,'src/img/parede_1.png')
                if tile == 'L':
                    Parede(self,coluna,linha,'src/img/parede_2.png')
                if tile == 'M':
                    Parede(self,coluna,linha,'src/img/mesa_5.png')
                if tile == 'Q':
                    Parede(self,coluna,linha,'src/img/mesa_2.png')
                if tile == 'Y':
                    Parede(self,coluna,linha,'src/img/mesa_3.png')
                if tile == 'T':
                    Parede(self,coluna,linha,'src/img/mesa_4.png')
                if tile == 'V':
                    Parede(self,coluna,linha,'src/img/mesa_1.png')

                if tile == 'E':
                    self.jogador = Jogador(self, coluna, linha)
                #bota fofolete tbm

        self.camera = Camera(self.map.largura, self.map.altura)

    def rodando(self):
        #loop do jogo
        self.funcionando = True
        while self.funcionando:
            self.dt = self.clock.tick(FPS) / 1000
            self.eventos()
            self.update()
            self.draw()

    def sai(self):
        pygame.quit()
        sys.exit()

    
    def update(self):
        self.todos_sprites.update()
        self.camera.update(self.jogador)

    def draw(self):
        self.screen.fill(COR_BACKGROUND)
        for sprite in self.todos_sprites:
            self.screen.blit(sprite.imagem, self.camera.aplicacao(sprite))
        pygame.display.flip()

    def eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.quit()
    
 

jogo = Jogo_principal()