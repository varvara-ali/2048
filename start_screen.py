import pygame
from input_box import InputBox, Button

WIDTH = 800
HEIGHT = 1000


def show_text(screen: pygame.Surface,
              text: list,
              x: int, y: int,
              font_size: int = 30,
              font_color: pygame.Color = pygame.Color('#776e65')):
    font = pygame.font.Font(None, font_size)
    text_coord = y
    for line in text:
        string_rendered = font.render(line, True, font_color)
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = x
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)


class Start_screen:
    def __init__(self, screen):
        self.screen = screen
        self.name = InputBox(270, 300, 140, 32, 'Варвара')
        self.start_button = Button(270, 350, 140, 32, 'Новая игра')



    def hello(self):
        header = ['2048']
        intro_text = ["",
                      "Правила игры",
                      "Управление стрелками на клавиатуре",
                      "цель набрать 2048 очков"]
        name_input = ['Введите имя:']
        self.screen.fill(pygame.Color("#faf8ef"))
        show_text(self.screen, header, 50, 10, 50, pygame.Color('#550000'))
        show_text(self.screen, intro_text, 50, 60)
        show_text(self.screen, name_input, 80, 300, 30, pygame.Color('#550055'))

    def show_leaders(self):
        leaders = [()]

    def continue_game(self):
        pass
