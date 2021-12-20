#menu e botões que chamam as funções
import pygame, sys
from pygame import draw
from pygame import font
from pygame import mixer
from pygame.locals import *

sys.path.append("src/")
from snake import *
import main_game

class Button():
    def __init__(self, text, width, height, pos):
        self.size = (width, height)

        self.hover = False

        self.top_rect = pygame.Rect(pos, self.size)
        self.top_color = RED

        self.bottom_rect = pygame.Rect((pos[0] -3, pos[1] + 3), self.size)
        self.bottom_color = GRAY

        self.text_surface = font_normal.render(text, True, WHITE)
        self.text_rect = self.text_surface.get_rect(center = self.top_rect.center)

    def draw(self):
        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius = 12)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius = 12)
        screen.blit(self.text_surface, self.text_rect)

screens = ["menu", "game", "minigames", "snake1", "snake2", "snake3", "ending"]

#converter a criação de botões p classes (fazer animado)
#configurar git bash p fazer o push inicial

clock = pygame.time.Clock()

width, height = 800, 600

pygame.init()
pygame.display.set_caption('CalouCIn')
screen = pygame.display.set_mode((width, height))

#whoosh = mixer.Sound(r"src\audio\#whoosh.ogg")
#whoosh.set_volume(0.2)

font_normal = pygame.font.SysFont(None, 30)
font_big = pygame.font.SysFont(None, 50)

logo_cin = pygame.image.load(r"src\img\cin-logo.png") #128x108

# Colors
BLACK = (0, 0, 0)
WHITE = "#f2ebeb"
RED = (200, 0, 0)
DARK_RED = (158, 0, 16)
GRAY = (128, 128, 128)

def verify_click(button, mouse_pos, click, current_screen, new_screen):
    if button.top_rect.collidepoint(mouse_pos):
        button.top_color = DARK_RED

        if click:
            #whoosh.play()
            
            current_screen = new_screen

    return current_screen

def write(text, font, color, surface, pos):
    text_obj = font.render(text, 1, color)
    text_surface = text_obj.get_rect()
    text_surface.center = pos

    surface.blit(text_obj, text_surface)

def draw_button(color, pos):
    x, y = pos

    button = pygame.Rect(x, y, 300, 70)
    pygame.draw.rect(screen, color, button)

    return button

def menu():
    screen.fill(WHITE)
    write("CInTítulo Totoso", font_big, GRAY, screen, (width/2, 100))
    write("CInTítulo Totoso", font_big, RED, screen, (width/2 + 2, 98))

    #start x and y, end x and y
    pos_play_button = (250, 220)
    pos_minigames_button = (250, 320)

    play_button = Button("Jogar", 300, 70, pos_play_button)
    minigames_button = Button("Minigames", 300, 70, pos_minigames_button)

    play_button.draw()
    minigames_button.draw()

    screen.blit(logo_cin, (652, 472)) 

    return play_button, minigames_button

def game():
    main_game.jogo.setup()
    main_game.jogo.rodando()

def minigames(high_score1, high_score2, high_score3):
    screen.fill(WHITE)

    write(f"High-score 1: {high_score1}", font_normal, RED, screen, (710, 12))
    write(f"High-score 2: {high_score2}", font_normal, RED, screen, (710, 32))
    write(f"High-score 3: {high_score3}", font_normal, RED, screen, (710, 52))

    pos_snake1_button = (250, 170)
    snake1_button = Button("Snake v1.0", 300, 70, pos_snake1_button)
    snake1_button.draw()

    pos_snake2_button = (250, 270)
    snake2_button = Button("Snake v2.0", 300, 70, pos_snake2_button)
    snake2_button.draw()

    pos_snake3_button = (250,370)
    snake3_button = Button("Snake v3.0", 300, 70, pos_snake3_button)
    snake3_button.draw()

    return snake1_button, snake2_button, snake3_button

def main():
    current_screen = screens[0]
    click = False

    high_score1 = 0
    high_score2 = 0
    high_score3 = 0

    while True:

        mouse_pos = pygame.mouse.get_pos()

        if current_screen == "menu":
            playbutton, minigamesbutton = menu()
            playbutton_y = playbutton.top_rect.y
            minigamesbutton_y = minigamesbutton.top_rect.y
            
            playbutton.top_color = RED
            minigamesbutton.top_color = RED
            
            current_screen = verify_click(playbutton, mouse_pos, click, current_screen, screens[1]) #game
            current_screen = verify_click(minigamesbutton, mouse_pos, click, current_screen, screens[2]) #minigames

            playbutton.draw()
            minigamesbutton.draw()

        elif current_screen == "game":
            game()

        elif current_screen == "minigames":
            snake1_button, snake2_button, snake3_button = minigames(high_score1, high_score2, high_score3)

            current_screen = verify_click(snake1_button, mouse_pos, click, current_screen, screens[3]) #snake
            current_screen = verify_click(snake2_button, mouse_pos, click, current_screen, screens[4]) #snake
            current_screen = verify_click(snake3_button, mouse_pos, click, current_screen, screens[5]) #snake

            snake1_button.draw()
            snake2_button.draw()

        elif current_screen == "snake1":
            points = snake_game(screen, 1)
            if points > high_score1: high_score1 = points

            current_screen = screens[2]

        elif current_screen == "snake2":
            points = snake_game(screen, 2)
            if points > high_score2: high_score2 = points

            current_screen = screens[2]

        elif current_screen == "snake3":
            points = snake_game(screen, 3)
            if points > high_score3: high_score3 = points

            current_screen = screens[2]

        # Eventos
        click = False
        for event in pygame.event.get():

            if event == QUIT:
                pygame.quit()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    if current_screen == "menu":
                        running = False     
                        pygame.quit()                   

                    else:
                        #whoosh.play()
                        current_screen = "menu"

        pygame.display.update()

        clock.tick(60)

main()