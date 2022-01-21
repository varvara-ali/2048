import pygame as pg

COLOR_INACTIVE = pg.Color('#776e65')
COLOR_ACTIVE = pg.Color('#faf8ef')


class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = pg.font.Font(None, 32).render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        """
        проверка всевозможных событий
        :param event:
        :return:
        """
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:

            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    return True
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif len(self.text) > 20:
                    return False
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = pg.font.Font(None, 32).render(self.text, True, self.color)
        return False

    def update(self):
        """
        ограничение длины поля ввода
        :return:
        """
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)


class Button(InputBox):
    def __init__(self, x, y, w, h, text=''):
        super(Button, self).__init__(x, y, w, h, text)
        self.txt_surface = pg.font.Font(None, 32).render(text, True, COLOR_ACTIVE)

    def handle_event(self, event):
        """
        если игрок кликнул в полу ввода, то оно изменит цвет
        :param event:
        :return: True or False
        """
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.color = COLOR_ACTIVE
                return True
        return False

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
