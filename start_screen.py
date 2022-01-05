import pygame
WIDTH = 800
HEIGHT = 1000


class Start_screen:
    def __init__(self, screen):
        self.screen = screen

    def hello(self):
        intro_text = ["",
                      "Правила игры",
                      "Управление стрелками на клавиатуре",
                      "цель набрать 2048 очков"]
        self.screen.fill(pygame.Color("#faf8ef"))
        font = pygame.font.Font(None, 50)
        self.screen.blit(font.render('2048', 1, pygame.Color('#550000')), (10, 50))

        font = pygame.font.Font(None, 30)
        text_coord = 70
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('#776e65'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            self.screen.blit(string_rendered, intro_rect)

    def new_game(self):
        pass

    def show_leaders(self):
        pass

    def continue_game(self):
        pass