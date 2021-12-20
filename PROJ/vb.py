import pygame, sys

from os import path

from map import *
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
        mapa_texto = path.join(pasta, 'aa.txt') #
        self.map = Mapa(mapa_texto)

    def setup(self): # setup do jogo
        self.todos_sprites = pygame.sprite.Group() # agrupar todos os sprites do jogo
        self
