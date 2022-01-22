import pygame
from start_screen import show_text
from input_box import Button
from game import Table


class Main_screen:
    def __init__(self, screen, name, data, score=0, max_score=0):
        self.board = Table(data, score)
        self.victory_state = 0
        self.name = name
        self.score = score
        self.max_score = max_score
        self.screen = screen
        self.start_button = Button(565, 100, 140, 32, 'Новая игра')
        self.game_over = False

    def content(self):
        """
        Вывод всего текста игры. Интро, правила, экран побуды и поражения
        :return: text
        """
        header = ['2048']
        intro_text = ["",
                      "Соединяйте числа, чтобы получить",
                      "плитку с номером 2048"]
        rules = ["Используйте стрелки, чтобы перемещать плитки.",
                 "Две плитки с одинаковым номером сливаются в одну."]
        self.screen.fill(pygame.Color("#faf8ef"))
        show_text(self.screen, header, 50, 10, 70, pygame.Color('#550000'))
        show_text(self.screen, intro_text, 50, 60)
        show_text(self.screen, rules, 50, 850)
        self.score = self.board.score

        pygame.draw.rect(self.screen, pygame.Color('#776e65'), (425, 10, 130, 60), 0)
        pygame.draw.rect(self.screen, pygame.Color('#776e65'), (575, 10, 130, 60), 0)
        show_text(self.screen, ['Текущий счет'], 440, 5, 20, pygame.Color('#eee4da'))
        show_text(self.screen, ['Рекордный счет'], 590, 5, 20, pygame.Color('#eee4da'))
        show_text(self.screen, [f'{self.score}'], 440, 30, 40, pygame.Color('#ffffff'))
        show_text(self.screen, [f'{self.max_score if self.score < self.max_score else self.score}'],
                  590, 30, 40,
                  pygame.Color('#ffffff'))
        self.start_button.draw(self.screen)
        self.board.draw(self.screen)

        if self.game_over:
            s = pygame.Surface((700, 200))  # the size of your rect
            s.set_alpha(130)  # alpha level

            show_text(s, ['Игра окончена'], 170, 50, 80, pygame.Color('red'))
            self.screen.blit(s, (50, 400))  # (0,0) are the top-left coordinates

        if self.victory_state == 1:

            s = pygame.Surface((700, 200))  # the size of your rect
            s.set_alpha(130)  # alpha level

            show_text(s, ['Победа!'], 170, 50, 80, pygame.Color('red'))
            self.screen.blit(s, (50, 400))  # (0,0) are the top-left coordinates

    def handle_event(self, event):
        """
        :param event: проверяются события победы и поражения ждя дальнейшей обработки
        :return:
        0 - ничего не надо делать
        1 - конец игры
        2 - новая игра
        """

        move_result = self.board.handle_event(event)
        if self.victory_state == 0 and self.board.victory:
            self.victory_state = 1
        elif self.victory_state == 1 and self.board.victory and event.type == pygame.KEYDOWN:
            self.victory_state = 2
        if not self.game_over and not move_result:
            self.game_over = True
            return 1
        if self.start_button.handle_event(event):
            return 2
        return 0

    def export_state(self):
        """
        Нужно для продолжения игры
        :return: ник и состояние поля
        """
        return self.name, *self.board.export_state()
