import pygame as pg
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
            2048: pg.Color('#3c3a32')
        }

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
    def __init__(self, initial_table=[]):
        self.background_color = pg.Color('#bbada0')
        self.margin_top = 200
        self.margin_left = 100
        if len(initial_table):
            self.import_state(initial_table)
            return
        self.cells = [[Cell() for _ in range(4)] for _ in range(4)]
        self.new_turn()
        self.new_turn()

    def new_turn(self):
        empty_indexes = []
        for i in range(4):
            for j in range(4):
                if not self.cells[i][j]:
                    empty_indexes.append((i, j))
        new_element_index = choice(empty_indexes)
        self.cells[new_element_index[0]][new_element_index[1]] = Cell(2)
        if len(empty_indexes) == 1:
            return False
        return True

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
        state = []
        for i in range(4):
            for j in range(4):
                state.append(self.cells[i][j].value)
        return state

    def import_state(self, state):
        self.cells = self.cells = [[Cell(state[i * 4 + j]) for j in range(4)] for i in range(4)]

    def check_possible_turn(self):
        state = self.export_state()
        if t.up():
            self.import_state(state)
            return True
        if t.down():
            self.import_state(state)
            return True
        if t.left():
            self.import_state(state)
            return True
        if t.right():
            self.import_state(state)
            return True
        return False


if __name__ == '__main__':

    t = Table([0 if i % 4 else 2 for i in range(16)])
    print(t)
    pg.init()
    size = 800, 1000
    screen = pg.display.set_mode(size)
    clock = pg.time.Clock()
    running = True
    # is_arrows = False
    # was_move = False
    # was_move = t.left()
    # if was_move:
    #     t.new_turn()
    #
    # exit()

    while running:  # Основной игровой цикл
        # обработка событий
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                is_arrows = False
                was_move = False
                if event.key == pg.K_UP:
                    is_arrows = True
                    was_move = t.up()
                if event.key == pg.K_DOWN:
                    is_arrows = True
                    was_move = t.down()
                if event.key == pg.K_LEFT:
                    is_arrows = True
                    was_move = t.left()
                if event.key == pg.K_RIGHT:
                    is_arrows = True
                    was_move = t.right()
                print(was_move)
                # if is_arrows and not was_move:
                #     state = t.export_state()
                #     if t.up():
                #         t.import_state(state)
                #         continue
                #     if t.down():
                #         t.import_state(state)
                #         continue
                #     if t.left():
                #         t.import_state(state)
                #         continue
                #     if t.right():
                #         t.import_state(state)
                #         continue
                #     print('Game over')
                if was_move:
                    new_turn_result = t.new_turn()
                    print(new_turn_result)
                    if not new_turn_result: #последняя ячейка заполнилась
                        if not t.check_possible_turn():
                            print('game over')
                            running = False



        # обновление экрана
        screen.fill(pg.Color('#ffffff'))

        t.draw(screen)
        pg.display.flip()
        clock.tick(60)

    # закрытие игры

    pg.quit()
