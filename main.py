import pygame
from start_screen import Start_screen, WIDTH, HEIGHT
from db import Statistic
from main_screen import Main_screen

if __name__ == '__main__':
    pygame.mixer.init()
    pygame.mixer.music.load('music_fone.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.8)
    pygame.init()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    background_color = 'white'
    fps = 60

    stat = Statistic()
    start_name, start_board, start_score = stat.load_session()
    start_screen = Start_screen(screen, start_name)

    running = True
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

    # start_board = [0,0,0,0,1024,1024,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    while True:
        game = Main_screen(screen,
                           name=start_screen.name.text,
                           data=start_board,
                           score=start_score,
                           max_score=stat.get_record())
        running = True
        while running:  # Основной игровой цикл
            # обработка событий
            for event in pygame.event.get():
                state = game.handle_event(event)
                # новая игра
                if state == 2:
                    if not game.game_over:
                        stat.save_leader(game.name, game.score)
                    start_score = 0
                    start_board = []
                    running = False
                if state == 1:
                    stat.save_leader(game.name, game.score)
                if event.type == pygame.QUIT:
                    stat.save_leader(game.name, game.score)
                    stat.save_session(*game.export_state())
                    pygame.quit()

            # обновление экрана
            screen.fill(pygame.Color("#faf8ef"))
            game.content()
            pygame.display.flip()
            clock.tick(fps)
