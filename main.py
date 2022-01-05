import pygame
import copy
from start_screen import Start_screen

class Cell:
    def __init__(self, size, index_x, index_y, start_x, start_y):
        self.size = size
        self.x = index_x
        self.y = index_y
        self.start_x = start_x
        self.start_y = start_y
        self.background_color = 'black'
        self.border_color = 'white'
        self.alive = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.background_color, (self.start_x, self.start_y, self.size, self.size), 0)
        pygame.draw.rect(screen, self.border_color, (self.start_x, self.start_y, self.size, self.size), 2)

    def on_click(self):
        self.change_state()

    def change_state(self):
        if not self.alive:
            self.background_color = 'green'
            self.alive = True
        elif self.alive:
            self.background_color = 'black'
            self.alive = False

    def check_neighbours(self):
        pass


class Board:
    def __init__(self, cells_x, cells_y):
        self.cells_x = cells_x
        self.cells_y = cells_y
        self.cell_size = 20  # размер клетки
        self.margin_x = 50
        self.margin_y = 50
        self.cells = [[Cell(self.cell_size, x, y, self.margin_x + x * self.cell_size, self.margin_y + y * self.cell_size)
                       for x in range(self.cells_x)] for y in range(self.cells_y)]

    def draw(self, screen):
        for cells_row in self.cells:
            for cell in cells_row:
                cell.draw(screen)

    def is_coords_within(self, x: int, y: int) -> bool:
        if self.margin_x <= x <= self.margin_x + (self.cells_x * self.cell_size) and \
                self.margin_y <= y <= self.margin_y + (self.cells_y * self.cell_size):
            return True
        else:
            return False

    def get_cell_index_by_coords(self, x, y) -> tuple:
        cell_by_x = (x - self.margin_x) // self.cell_size
        cell_by_y = (y - self.margin_y) // self.cell_size
        return cell_by_x, cell_by_y

    def on_click(self, cell_x, cell_y):
        self.cells[cell_y][cell_x].on_click()

    def evolve(self):
        current_state = copy.deepcopy(self.cells)
        new_state = copy.deepcopy(self.cells)
        # сама эволюция
        for y in range(self.cells_y):
            for x in range(self.cells_x):
                neighbours = 0
                for diff_y in [-1, 0, 1]:
                    for diff_x in [-1, 0, 1]:
                        if not (diff_x == 0 and diff_y == 0):
                            if x + diff_x in range(self.cells_x) and y + diff_y in range(self.cells_y) and current_state[y + diff_y][x + diff_x].alive:
                                neighbours += 1
                if not new_state[y][x].alive and neighbours == 3:
                    new_state[y][x].change_state()
                elif new_state[y][x].alive and neighbours not in (2, 3):
                    new_state[y][x].change_state()
        self.cells = copy.deepcopy(new_state)
        if new_state == current_state:
            pygame.quit()


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    background_color = 'black'
    fps = 60

    start_screen = Start_screen(screen)
    start_screen.hello()

    running = True
    evolution_going = False
    start_screen_flag = True
    

    while running:  # Основной игровой цикл
        # обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click_x, click_y = event.pos

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                   pass


        # обновление экрана
        #screen.fill(background_color)


        pygame.display.flip()
        clock.tick(fps)

    # закрытие игры
    pygame.quit()