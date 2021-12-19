import pygame, random
from pygame.locals import *
from pygame import mixer

mixer.init()
eating_sound = mixer.Sound(r"src\audio\eating.wav")
eating_sound.set_volume(1)

bg = pygame.image.load(r"src\img\dark_forest.png")
apple_img = pygame.image.load(r"src\img\apple.png")
grape_img = pygame.image.load(r"src\img\grape.png")
blueberry_img = pygame.image.load(r"src\img\blueberry.png")

clock = pygame.time.Clock()

class Fruit:

    def __init__(self, color, points, sprite = None):
        self.fruit = pygame.Rect(0, 0, 20, 20)
        self.color = color
        self.points = points
        self.pos = (0, 0)
        self.counter = 0

        self.sprite = sprite

    def change_pos(self, new_pos):
        self.fruit.x = new_pos[0]
        self.fruit.y = new_pos[1]

    def draw(self, screen):
        if not self.sprite: pygame.draw.rect(screen, self.color, self.fruit)
        else:
            screen.blit(self.sprite, [self.fruit.x, self.fruit.y])

    def eat(self):
        self.counter += 1
        return self.points

def snake_game(screen, game_version):

    def pos_grid(): #Gera uma posição no grid 20x20
        x = 0
        y = 0
    
        while x <= 160 and y <= 40 or x <= 100 and y >= 560: #Evita que a maçã apareça sobre os textos da esquerda
            x = random.randint(0, 780) 
            y = random.randint(0, 580)
        
        return (x // 20 * 20, y // 20 * 20)

    def collision(c1, c2): #Testa colisões
        return (c1[0] == c2[0] and c1[1] == c2[1])

    #Cores
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (250, 0, 0)
    blue = (0, 0, 250)
    purple = (160, 0, 200)

    #Texto
    font = pygame.font.SysFont(pygame.font.get_default_font(), 45)
    font_2 = pygame.font.SysFont(pygame.font.get_default_font(), 30) #Autoria
    lose_text = font.render('GAME OVER', 1, red)
    quit_text = font.render('PRESS ESC TO QUIT', 1, red)
    pause_text = font.render('PAUSE', 1, white)
    tutorial_text = font_2.render('ARROWS = MOVEMENT', 1, white)
    tutorial_text_2 = font_2.render('SPACE = PAUSE', 1, white)
    tutorial_text_3 = font_2.render('ESC = QUIT', 1, white)
    starting = True
    pts = 0

    #Player
    player = pygame.Surface((20, 20))
    player.fill(white)
    player_pos = [[400, 400], [400, 420], [400, 440]]
    dir = 'stopped' #Direção do player
    last_dir = 'none'
    pressed = False
    alive = True

    #Comida da cobra
    if game_version > 2:
        apple = Fruit(red, 5, apple_img)
        grape = Fruit(purple, 7, grape_img)
        blueberry = Fruit(blue, 10, blueberry_img)

    else:
        apple = Fruit(red, 5)
        grape = Fruit(purple, 7)
        blueberry = Fruit(blue, 10)

    fruit = 1
    fruit_pos = pos_grid()

    while True:
        for event in pygame.event.get(): #Testa os eventos
            if event.type == QUIT:
                pygame.quit()
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return pts

                if alive == True:
                    if event.key == K_UP: #Direção da cobra
                        if dir == 'down' or last_dir == 'down' or dir == 'up': #Impede que a cobra se atravesse
                            pass
                        elif pressed == True: #Resolve o BUG (Olhar última linha)
                            pass
                        else:
                            dir = 'up'
                            last_dir = 'stopped'
                            pressed = True
                    if event.key == K_DOWN:
                        if dir == 'up' or last_dir == 'up' or dir == 'down':
                            pass
                        elif pressed == True or starting == True:
                            pass
                        else:
                            dir = 'down'
                            last_dir = 'stopped'
                            pressed = True
                    if event.key == K_LEFT:
                        if dir == 'right' or last_dir == 'right' or dir == 'left':
                            pass
                        elif pressed == True:
                            pass
                        else:
                            dir = 'left'   
                            last_dir = 'stopped'
                            pressed = True
                    if event.key == K_RIGHT:
                        if dir == 'left' or last_dir == 'left' or dir == 'right':
                            pass
                        elif pressed == True:
                            pass
                        else:
                            dir = 'right'
                            last_dir = 'stopped'
                            pressed = True
                    if event.key == K_SPACE: #Pausa e despausa
                        if not dir == 'stopped':
                            last_dir = dir
                            dir = 'stopped'
                        elif dir == 'stopped' and last_dir == 'none':
                            pass
                        else:
                            dir = last_dir
                            last_dir = 'stopped'
                    if pressed == True and starting == True:
                        starting = False
                else:
                    pass

        #Limpando a tela (IMPORTANTE)
        screen.fill(black)
        if game_version > 1: screen.blit(bg, [0, 0])

        #Colisão Player-Fruta
        if collision(player_pos[0], fruit_pos): 
            last_fruit = fruit
            fruit_pos = pos_grid()

            if game_version > 1: 
                fruit = random.randint(1, 3)
                eating_sound.play()            

            player_pos.append([0, 0])

            if last_fruit == 1:
                pts += apple.eat()
            elif last_fruit == 2: 
                pts += grape.eat()
            else: 
                pts += blueberry.eat()

        #Colisão Player-Player
        for c in range(len(player_pos) - 2, 0 , -1):
            if collision(player_pos[0], player_pos[c]):
                alive = False
        
        #Verifica se o player está saindo da tela
        if player_pos[0][0] == 0 and dir == 'left': #Dividi em várias linhas para não ficar feio
            alive = False
        if player_pos[0][0] == 780 and dir == 'right':
            alive = False
        if player_pos[0][1] == 0 and dir == 'up':
            alive = False
        if player_pos[0][1] == 580 and dir == 'down':
            alive = False

        #Verifica se o player está vivo
        if alive == False:
            dir = 'stopped'
            screen.blit(lose_text, [300, 0])
            screen.blit(quit_text, [250, 30])

        #Atualizando as posições do corpo da cobra
        for c in range(len(player_pos) - 1, 0, -1): 
            if dir == 'stopped':
                pass
            else:
                (player_pos[c][0], player_pos[c][1]) = (player_pos[c-1][0], player_pos[c-1][1])
        
        #Atualiza a posição da cabeça da cobra com base na direção
        if dir == 'up':
            player_pos[0][1] -= 20
        if dir == 'down':
            player_pos[0][1] += 20
        if dir == 'left':
            player_pos[0][0] -= 20
        if dir == 'right':
            player_pos[0][0] += 20
        if dir == 'stopped':
            player_pos = player_pos
            if starting == False and alive == True:
                screen.blit(pause_text, [335, 280])
            if alive == True:
                screen.blit(tutorial_text, [560, 10])
                screen.blit(tutorial_text_2, [560, 35])
                screen.blit(tutorial_text_3, [560, 60])
        
        #Gerando os elementos da tela
        if fruit == 1:
            apple.change_pos(fruit_pos) # Apple
            apple.draw(screen)

        elif fruit == 2:
            grape.change_pos(fruit_pos) # Grape
            grape.draw(screen)

        else:
            blueberry.change_pos(fruit_pos) # Blueberry 
            blueberry.draw(screen)
        
        for pos in player_pos: #Gerar a cobra
            screen.blit(player, pos)

        if game_version > 2:
            apples = font.render(f"x{apple.counter}", 1, white)
            grapes = font.render(f"x{grape.counter}", 1, white)
            blueberries = font.render(f"x{blueberry.counter}", 1, white)

            screen.blit(apple_img.convert_alpha(), (0, 580))
            screen.blit(apples, (15, 570))

            screen.blit(grape_img.convert_alpha(), (65, 580))
            screen.blit(grapes, (80, 570))

            screen.blit(blueberry_img.convert_alpha(), (130, 580))
            screen.blit(blueberries, (145, 570))

        text = font.render(f'POINTS: {pts}', 1, white)
        screen.blit(text, [0, 0])
        
        pressed = False

        pygame.display.update()
        clock.tick(11)

    return pts