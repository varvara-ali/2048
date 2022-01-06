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
            self.cells = self.cells = [[Cell(initial_table[i * 4 + j]) for j in range(4)] for i in range(4)]
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


if __name__ == '__main__':
    t = Table([2, 2, 4, 4, 16, 16, 32, 32, 128, 128, 512, 512, 1024, 2048, 2, 2])
    print(t)
    pg.init()
    size = 800, 1000
    screen = pg.display.set_mode(size)
    clock = pg.time.Clock()
    running = True

    while running:  # Основной игровой цикл
        # обработка событий
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_x, click_y = event.pos
        # обновление экрана
        screen.fill(pg.Color('#ffffff'))

        t.draw(screen)
        pg.display.flip()
        clock.tick(60)

    # закрытие игры
    pg.quit()
