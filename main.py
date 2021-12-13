#menu e botões que chamam as funções
import pygame, sys
from pygame import draw
from pygame import font
from pygame import mixer
from pygame.locals import *

sys.path.append("src/")
from snake import *

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

screens = ["menu", "game", "minigames", "snake", "ending"]

#converter a criação de botões p classes (fazer animado)
#configurar git bash p fazer o push inicial

clock = pygame.time.Clock()

width, height = 800, 600

pygame.init()
pygame.display.set_caption('CalouCIn')
screen = pygame.display.set_mode((width, height))

whoosh = mixer.Sound(r"src\audio\whoosh.ogg")
whoosh.set_volume(0.15)

font_normal = pygame.font.SysFont(None, 30)
font_big = pygame.font.SysFont(None, 50)

logo_cin = pygame.image.load(r"src\img\cin-logo.png") #128x108

BLACK = (0, 0, 0)
WHITE = "#f2ebeb"
RED = (200, 0, 0)
DARK_RED = (158, 0, 16)
GRAY = (128, 128, 128)

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
    snake_game()

    """screen.fill(WHITE)
    write("telinha totosa do game", font_big, RED, screen, (width/2, 90))"""

def minigames():
    screen.fill(WHITE)
    write("telinha totosa dos minigames", font_big, RED, screen, (width/2, 90))

def main():
    current_screen = screens[0]
    click = False

    running = True

    while running:

        mouse_pos = pygame.mouse.get_pos()

        if current_screen == "menu":
            playbutton, minigamesbutton = menu()
            playbutton_y = playbutton.top_rect.y
            minigamesbutton_y = minigamesbutton.top_rect.y
            
            playbutton.top_color = RED
            minigamesbutton.top_color = RED
            
            if playbutton.top_rect.collidepoint(mouse_pos):
                playbutton.top_color = DARK_RED

                if click:
                    whoosh.play()
                    
                    current_screen = screens[1] #game
            
            elif minigamesbutton.top_rect.collidepoint(mouse_pos):
                minigamesbutton.top_color = DARK_RED
                
                if click:
                    whoosh.play()

                    current_screen = screens[2] #minigames

            playbutton.draw()
            minigamesbutton.draw()

        elif current_screen == "game":
            game()

        elif current_screen == "minigames":
            minigames()

        click = False
        for event in pygame.event.get():

            if event == QUIT:
                running = False
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
                        whoosh.play()
                        current_screen = "menu"

        pygame.display.update()
        clock.tick(60)

main()