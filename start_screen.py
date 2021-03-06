import pygame
from input_box import InputBox, Button


WIDTH = 800
HEIGHT = 1000


def show_text(screen: pygame.Surface,
              text: list,
              x: int, y: int,
              font_size: int = 30,
              font_color: pygame.Color = pygame.Color('#776e65')):
    """
    Функция, умеющая выводить текст. Очень удобно
    :param screen: pygame.Surface
    :param text: list
    :param x: int
    :param y: int
    :param font_size: 30
    :param font_color: pygame.Color('#776e65')
    :return:
    """
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
    def __init__(self, screen, name):
        self.screen = screen
        self.name = InputBox(270, 300, 140, 32, name)
        self.start_button = Button(270, 350, 140, 32, 'Играть')

    def hello(self):
        """
        Стартовый текст
        :return:
        """
        header = ['2048']
        intro_text = ["",
                      "Правила игры",
                      "Управление стрелками на клавиатуре",
                      "цель набрать 2048 очков"]
        name_input = ['Введите имя:']
        self.screen.fill(pygame.Color("#faf8ef"))
        show_text(self.screen, header, 50, 10, 70, pygame.Color('#550000'))
        show_text(self.screen, intro_text, 50, 60)
        show_text(self.screen, name_input, 80, 300, 30, pygame.Color('#550055'))

    def show_leaders(self, list_leaders):
        """
        Вывод таблицы рекордов
        :param list_leaders: list
        :return:
        """
        show_text(self.screen, ['Таблица рекордов'], 150, 450, 50, pygame.Color('#550000'))
        if len(list_leaders) == 0:
            show_text(self.screen, ['Рекордов нет'], 50, 500, 30)
            return
        names = [list_leader[0] for list_leader in list_leaders]
        records = [str(list_leader[1]) for list_leader in list_leaders]
        dates = [list_leader[2][:19] for list_leader in list_leaders]
        show_text(self.screen, names, 50, 500, 30)
        show_text(self.screen, records, 250, 500, 30)
        show_text(self.screen, dates, 450, 500, 30)

