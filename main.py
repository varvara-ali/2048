import pygame
from start_screen import Start_screen, WIDTH, HEIGHT
from db import Statistic

if __name__ == '__main__':
    pygame.init()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    background_color = 'black'
    fps = 60

    start_screen = Start_screen(screen)
    stat = Statistic()
    # start_screen.hello()
    stat.create_db()

    running = True
    evolution_going = False
    start_screen_flag = True

    while start_screen_flag:  # цикл стартового экрана
        # обработка событий
        for event in pygame.event.get():
            if start_screen.name.handle_event(event) or start_screen.start_button.handle_event(event):
                start_screen_flag = False
            if event.type == pygame.QUIT:
                pygame.quit()

            start_screen.name.update()
            start_screen.hello()
            start_screen.name.draw(screen)
            start_screen.start_button.draw(screen)
            start_screen.show_leaders(stat.get_leaders())

        pygame.display.flip()
        clock.tick(fps)

    print("основной цикл")
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
        # screen.fill(background_color)

        pygame.display.flip()
        clock.tick(fps)

    # закрытие игры
    pygame.quit()
