import pygame, random
from pygame.locals import *
from pygame import mixer

mixer.init()
eating_sound = mixer.Sound(r"src\audio\eating.wav")
eating_sound.set_volume(1)

background_music = mixer.music.load(r"src\audio\fofolete_theme.mp3")
mixer.music.set_volume(0.05)
mixer.music.play(-1)

bg = pygame.image.load(r"src\img\dark_forest.png")
apple_img = pygame.image.load(r"src\img\apple.png")
grape_img = pygame.image.load(r"src\img\grape.png")
blueberry_img = pygame.image.load(r"src\img\blueberry.png")

clock = pygame.time.Clock()

 #Cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (250, 0, 0)
blue = (0, 0, 250)
purple = (160, 0, 200)

# DIREÇÕES
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3


class Snake:
    def __init__(self, size, head_pos, game_version):
        self.size = size
        self.head_pos = head_pos
        self.body = []
        self.game_version = game_version
        self.sprites = {    'head up':          pygame.image.load(r'src\img\snake_sprites\head_up.png')         ,
                            'head down':        pygame.image.load(r'src\img\snake_sprites\head_down.png')       ,
                            'head left':        pygame.image.load(r'src\img\snake_sprites\head_left.png')       ,
                            'head right':       pygame.image.load(r'src\img\snake_sprites\head_right.png')      ,
                            'horizontal body':  pygame.image.load(r'src\img\snake_sprites\horizontal_body.png') ,
                            'vertical body':    pygame.image.load(r'src\img\snake_sprites\vertical_body.png')   ,
                            'curve left down':  pygame.image.load(r'src\img\snake_sprites\curve_left_down.png') ,
                            'curve left up':    pygame.image.load(r'src\img\snake_sprites\curve_left_up.png')   ,
                            'curve right down': pygame.image.load(r'src\img\snake_sprites\curve_right_down.png'),
                            'curve right up':   pygame.image.load(r'src\img\snake_sprites\curve_right_up.png')  ,
                            'tail up':          pygame.image.load(r'src\img\snake_sprites\tail_up.png')         ,
                            'tail left':        pygame.image.load(r'src\img\snake_sprites\tail_left.png')       ,
                            'tail right':       pygame.image.load(r'src\img\snake_sprites\tail_right.png')      ,
                            'tail down':        pygame.image.load(r'src\img\snake_sprites\tail_down.png')       }

        
        self.l = [self.sprites['head up']]
        for i in range(size - 2):
            self.l.append(self.sprites['vertical body'])             # Define o corpo da cobra com base no tamanho dado como parâmetro
        else:
            self.l.append(self.sprites['tail up'])
        for i in range(size):
            self.body.append([[head_pos[0], head_pos[1] +  20*i], self.l[i], UP])   # body[i] == [[x, y], sprite, dir]


    def movement(self, speed, direction, paused, alive):
        
        if direction == UP:
            self.body[0][0][1] -= speed
            self.body[0][1] = self.sprites['head up']
        elif direction == DOWN:
            self.body[0][0][1] += speed
            self.body[0][1] = self.sprites['head down']
        elif direction == LEFT:
            self.body[0][0][0] -= speed
            self.body[0][1] = self.sprites['head left']
        elif direction == RIGHT:
            self.body[0][0][0] += speed
            self.body[0][1] = self.sprites['head right']
        
        for c in range(len(self.body) - 1, 0, -1): 
            if not paused and alive:
                (self.body[c][0][0], self.body[c][0][1]) = (self.body[c-1][0][0], self.body[c-1][0][1])
                self.body[c][2] = self.body[c-1][2]

                if self.game_version > 2:
                    self.body[c][1] = self.body[c-1][1]
        
        if self.game_version > 2:
            tail_dir = self.body[-1][2]
            if tail_dir == UP:
                self.body[-1][1] = self.sprites['tail up']
            elif tail_dir == LEFT:
                self.body[-1][1] = self.sprites['tail left']
            elif tail_dir == DOWN:
                self.body[-1][1] = self.sprites['tail down']
            elif tail_dir == RIGHT:
                self.body[-1][1] = self.sprites['tail right']


    def directions(self, direction, event_key, pressed):
        if not pressed:
            if event_key == K_UP and direction != DOWN and direction != UP: #Direção da cobra
                if direction == LEFT:
                    self.body[1][1] = self.sprites['curve right up']
                elif direction == RIGHT:
                    self.body[1][1] = self.sprites['curve left up']
                direction = UP
                self.body[1][2] = 4

            elif event_key == K_DOWN and direction != UP and direction != DOWN:
                if direction == LEFT:
                    self.body[1][1] = self.sprites['curve right down']
                elif direction == RIGHT:
                    self.body[1][1] = self.sprites['curve left down']
                direction = DOWN
                self.body[1][2] = 4

            elif event_key == K_LEFT  and direction != RIGHT and direction != LEFT:
                if direction == UP:
                    self.body[1][1] = self.sprites['curve left down']
                elif direction == DOWN:
                    self.body[1][1] = self.sprites['curve left up']
                direction = LEFT    
                self.body[1][2] = 4      

            elif event_key == K_RIGHT and direction != LEFT and direction != RIGHT:
                if direction == UP:
                    self.body[1][1] = self.sprites['curve right down']
                elif direction == DOWN:
                    self.body[1][1] = self.sprites['curve right up']

                direction = RIGHT
                self.body[1][2] = 4
            
            self.body[0][2] = direction
            
        return direction, pressed

    def draw(self, screen):
        if self.game_version <= 2:
            for c in range(len(self.body)):
                pygame.draw.rect(screen, white, (self.body[c][0][0], self.body[c][0][1], 20, 20))

        else:

            for c in range(len(self.body)-1):
                if c > 1:
                    if self.body[c][2] == LEFT or self.body[c][2] == RIGHT:
                        self.body[c][1] = self.sprites['horizontal body']
                    elif self.body[c][2] == UP or self.body[c][2] == DOWN:
                        self.body[c][1] = self.sprites['vertical body']


            tail_dir = self.body[-1][2]
            if tail_dir == UP:
                self.body[-1][1] = self.sprites['tail up']
            elif tail_dir == LEFT:
                self.body[-1][1] = self.sprites['tail left']
            elif tail_dir == DOWN:
                self.body[-1][1] = self.sprites['tail down']
            elif tail_dir == RIGHT:
                self.body[-1][1] = self.sprites['tail right']
            
            for c in self.body:
                screen.blit(c[1].convert_alpha(), c[0])
    
    def increase(self):
        self.body.append([[self.body[-1][0][0], self.body[-1][0][1] + 20], self.sprites['head up'], self.body[-1][2]])


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
            width, height = self.sprite.get_width(), self.sprite.get_height()
            screen.blit(self.sprite, [self.fruit.x - (width - 20)/2, self.fruit.y - (height - 20)/2])

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
    player = Snake(4, [400, 400], game_version)

    dir = UP #Direção do player
    alive = True
    SPEED = 20
    speed = SPEED

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

    paused = False
    first = False
    while True:
        
        #Limpando a tela (IMPORTANTE)
        screen.fill(black)
        if game_version > 1: screen.blit(bg, [0, 0])

        pressed = False
        if first:
            player.draw(screen)
        first = True
        for event in pygame.event.get(): #Testa os eventos
            if event.type == QUIT:
                pygame.quit()
            
            if event.type == KEYDOWN:   # Sai do minigame
                if event.key == K_ESCAPE:
                    return pts
                if alive == True:
                    dir, pressed = player.directions(dir, event.key, pressed)

                    if event.key == K_SPACE: #Pausa e despausa
                        if alive:
                            if not paused:
                                paused = True
                                speed = 0
                            else:
                                paused = False
                                speed = SPEED

                    if starting == True:
                        starting = False
                

        #Colisão Player-Player
        for c in range(len(player.body) - 1, 1 , -1):
            if collision(player.body[0][0], player.body[c][0]):
                alive = False

        #Colisão Player-Fruta
        if collision(player.body[0][0], fruit_pos): 
            last_fruit = fruit
            fruit_pos = pos_grid()

            if game_version > 1: 
                fruit = random.randint(1, 3)
                eating_sound.play()            
             
            player.increase()

            if last_fruit == 1:
                pts += apple.eat()
            elif last_fruit == 2: 
                pts += grape.eat()
            else: 
                pts += blueberry.eat()

        
        #Verifica se o player está saindo da tela
        if player.body[0][0][0] == 0 and dir == LEFT: #Dividi em várias linhas para não ficar feio
            alive = False
        if player.body[0][0][0] == 780 and dir == RIGHT:
            alive = False
        if player.body[0][0][1] == 0 and dir == UP:
            alive = False
        if player.body[0][0][1] == 580 and dir == DOWN:
            alive = False

        #Verifica se o player está vivo
        if alive == False:
            paused = True
            speed = 0
            screen.blit(lose_text, [300, 0])
            screen.blit(quit_text, [250, 30])

        player.movement(speed, dir, paused, alive)

        if paused:
            if not starting and alive:
                screen.blit(pause_text, [335, 280])
            if alive:
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

        pygame.display.update()
        
        if game_version == 1:
            clock.tick(10)
        
        elif game_version == 2:
            clock.tick(15)

        else:
            clock.tick(20)

    return pts