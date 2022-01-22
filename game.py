import pygame as pg
import pygame.mixer
from os import path

from start_screen import show_text
from random import choice, randint

BORDER = 5
SIZE = 600
CELL_SIZE = SIZE // 4


class Cell:
    def __init__(self, value=0):
        self.value = value
        self.colors = {
            0: pg.Color('#776e65'),
            2: pg.Color('#eee4da'),
            4: pg.Color('#ede0c8'),
            8: pg.Color('#f2b179'),
            16: pg.Color('#f59563'),
            32: pg.Color('#f67c5f'),
            64: pg.Color('#f65e3b'),
            128: pg.Color('#edcf72'),
            256: pg.Color('#edcc61'),
            512: pg.Color('#edc850'),
            1024: pg.Color('#edc53f'),
            2048: pg.Color('#3c3a32'),
            4096: pg.Color('#3c3a32'),
            8192: pg.Color('#3c3a32'),
            16384: pg.Color('#3c3a32'),
            32768: pg.Color('#3c3a32')
        }
    # переопределение нескольких базовых функций

    def __bool__(self):
        if self.value == 0:
            return False
        else:
            return True

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return f'{self.value}'

    def __mul__(self, other):
        self.value = self.value * other

    def draw(self, screen, x, y):
        """
        отрисовка
        :param screen: pygame.Surface
        :param x: int
        :param y: int
        :return:
        """
        fontsize = 70
        pg.draw.rect(screen,
                     self.colors[self.value],
                     (x + BORDER, y + BORDER, CELL_SIZE - 2 * BORDER, CELL_SIZE - 2 * BORDER),
                     0)
        if self.value:
            show_text(screen,
                      [str(self.value)],
                      x + BORDER + (CELL_SIZE - 2 * BORDER) // 2 - 14 * len(str(self.value)),
                      y + BORDER + (CELL_SIZE - 2 * BORDER) // 2 - fontsize // 2,
                      fontsize
                      )


class Table:
    def __init__(self, initial_table, score=0):
        snd_dir = path.join(path.dirname(__file__))
        self.sound = pygame.mixer.Sound(path.join(snd_dir, 'pew.mp3'))
        self.sound.set_volume(0.4)
        self.score = score
        self.background_color = pg.Color('#bbada0')
        self.margin_top = 200
        self.victory = False
        self.margin_left = 100
        if len(initial_table):
            self.import_state(initial_table, score)
            return
        self.cells = [[Cell() for _ in range(4)] for _ in range(4)]
        self.new_turn()
        self.new_turn()

    def new_turn(self):
        """
        Каждый раз на новом шаге создает квадратик с 2 или 4 (шанс последней 10%)
        :return: True или False смотря сколько пустых ячеек осталось
        """
        empty_indexes = []
        for i in range(4):
            for j in range(4):
                if not self.cells[i][j]:
                    empty_indexes.append((i, j))
        new_element_index = choice(empty_indexes)
        self.cells[new_element_index[0]][new_element_index[1]] = Cell(2) if randint(1, 10) <= 9 else Cell(4)
        if len(empty_indexes) == 1:
            return False
        return True

    # обработка движения стрелок
    def up(self):
        is_move = False
        for i in range(3):
            for j in range(4):
                while not self.cells[i][j]:
                    is_any_not_null = False
                    for k in range(i, 3):
                        self.cells[k][j] = self.cells[k + 1][j]
                        self.cells[k + 1][j] = Cell(0)
                        is_any_not_null = is_any_not_null or bool(self.cells[k][j])
                    if not is_any_not_null:
                        break
                    is_move = True
        for i in range(3):
            for j in range(4):
                if self.cells[i][j] == self.cells[i + 1][j] and self.cells[i][j]:
                    is_move = True
                    self.cells[i][j].value *= 2
                    self.sound.play()
                    self.score += self.cells[i][j].value
                    for k in range(i + 1, 3):
                        self.cells[k][j] = self.cells[k + 1][j]
                    self.cells[3][j] = Cell(0)
        return is_move

    def down(self):
        is_move = False
        for i in range(3, 0, -1):
            for j in range(4):
                while not self.cells[i][j]:
                    is_any_not_null = False
                    for k in range(i, 0, -1):
                        self.cells[k][j] = self.cells[k - 1][j]
                        self.cells[k - 1][j] = Cell(0)
                        is_any_not_null = is_any_not_null or bool(self.cells[k][j])
                    if not is_any_not_null:
                        break
                    is_move = True
        for i in range(3, 0, -1):
            for j in range(4):
                if self.cells[i][j] == self.cells[i - 1][j] and self.cells[i][j]:
                    is_move = True
                    self.cells[i][j].value *= 2
                    self.sound.play()
                    self.score += self.cells[i][j].value
                    for k in range(i - 1, 0, - 1):
                        self.cells[k][j] = self.cells[k - 1][j]
                    self.cells[0][j] = Cell(0)
        return is_move

    def left(self):
        is_move = False
        for j in range(3):
            for i in range(4):
                while not self.cells[i][j]:
                    is_any_not_null = False
                    for k in range(j, 3):
                        self.cells[i][k] = self.cells[i][k + 1]
                        self.cells[i][k + 1] = Cell(0)
                        is_any_not_null = is_any_not_null or bool(self.cells[i][k])
                    if not is_any_not_null:
                        break
                    is_move = True

        for j in range(3):
            for i in range(4):
                if self.cells[i][j] == self.cells[i][j + 1] and self.cells[i][j]:
                    is_move = True
                    self.cells[i][j].value *= 2
                    self.sound.play()
                    self.score += self.cells[i][j].value
                    for k in range(j + 1, 3):
                        self.cells[i][k] = self.cells[i][k + 1]
                    self.cells[i][3] = Cell(0)
        return is_move

    def right(self):
        is_move = False
        for j in range(3, 0, -1):
            for i in range(4):
                while not self.cells[i][j]:
                    is_any_not_null = False
                    for k in range(j, 0, -1):
                        self.cells[i][k] = self.cells[i][k - 1]
                        self.cells[i][k - 1] = Cell(0)
                        is_any_not_null = is_any_not_null or bool(self.cells[i][k])
                    if not is_any_not_null:
                        break
                    is_move = True

        for j in range(3, 0, -1):
            for i in range(4):
                if self.cells[i][j] == self.cells[i][j - 1] and self.cells[i][j]:
                    is_move = True
                    self.cells[i][j].value *= 2
                    self.sound.play()
                    self.score += self.cells[i][j].value
                    for k in range(j - 1, 0, -1):
                        self.cells[i][k] = self.cells[i][k - 1]
                    self.cells[i][0] = Cell(0)
        return is_move

    def __str__(self):
        s = ''
        for i in range(4):
            for j in range(4):
                s += f'{self.cells[i][j]} '
            s += '\n'
        return s

    def draw(self, screen):
        pg.draw.rect(screen,
                     self.background_color,
                     pg.Rect(self.margin_left - BORDER, self.margin_top - BORDER, SIZE + 2 * BORDER, SIZE + 2 * BORDER),
                     0)
        for i in range(4):
            for j in range(4):
                self.cells[i][j].draw(screen, self.margin_left + j * CELL_SIZE, self.margin_top + i * CELL_SIZE)

    def export_state(self):
        """
        сохраняем текущюю таблицу и счет
        :return:
        """
        state = []
        for i in range(4):
            for j in range(4):
                state.append(self.cells[i][j].value)
        return state, self.score

    def import_state(self, state, score):
        """
        вставляем текущую таблицу и счет
        :param state: [ [] ]
        :param score: int
        :return:
        """
        self.cells = self.cells = [[Cell(state[i * 4 + j]) for j in range(4)] for i in range(4)]
        self.score = score

    def check_possible_turn(self):
        """
        проверяем возможен ли следующий ход
        :return:
        """
        state = self.export_state()
        if self.up():
            self.import_state(*state)
            return True
        if self.down():
            self.import_state(*state)
            return True
        if self.left():
            self.import_state(*state)
            return True
        if self.right():
            self.import_state(*state)
            return True
        return False

    def check_victory(self):
        """
        проверяем выиграл ли игрок
        :return: True or False
        """
        for i in range(4):
            for j in range(4):
                if self.cells[i][j].value == 2048:
                    return True
        return False

    def handle_event(self, event):
        """
        обработка всевозможных событий
        :param event: тип события
        :return: True or False
        """
        if event.type != pg.KEYDOWN:
            return True
        was_move = False
        if event.key == pg.K_UP:
            was_move = self.up()
        if event.key == pg.K_DOWN:
            was_move = self.down()
        if event.key == pg.K_LEFT:
            was_move = self.left()
        if event.key == pg.K_RIGHT:
            was_move = self.right()
        if was_move:
            if not self.victory:
                self.victory = self.check_victory()
            if not self.new_turn():  # последняя ячейка заполнилась
                if not self.check_possible_turn():
                    return False
        return True


if __name__ == '__main__':

    t = Table([2 ** ((i % 4) + 1) for i in range(16)])
    print(t)
    pg.init()
    size = 800, 1000
    screen = pg.display.set_mode(size)
    clock = pg.time.Clock()
    running = True

    while running:  # Основной игровой цикл
        # обработка событий
        for event in pg.event.get():
            running = t.handle_event(event)
            if event.type == pg.QUIT:
                running = False
        # обновление экрана
        screen.fill(pg.Color('#ffffff'))

        t.draw(screen)
        pg.display.flip()
        clock.tick(60)

    # закрытие игры

    pg.quit()
