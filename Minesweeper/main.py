import pygame
import sys
from mine import Mine


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((640, 360))
        pygame.display.set_caption('Minesweeper')

        self.mine = Mine(self)

    def run_game(self):
        while True:
            self._check_events()

            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print('ESC printed')

    def _update_screen(self):
        self.screen.fill((0, 0, 0))

        pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run_game()

# pygame.init()
# size = (640, 360)
# screen = pygame.display.set_mode(size)
# clock = pygame.time.Clock()
#
# color = (0, 0, 0)
# forward = True
#
# pygame.display.flip()
# screen.fill(color)
#
# while True:
#     clock.tick(120)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#     if forward:
#         if color[0] < 255:
#             color = (color[0] + 1, color[1], color[2])
#         elif color[1] < 255:
#             color = (color[0], color[1] + 1, color[2])
#         elif color[2] < 255:
#             color = (color[0], color[1], color[2] + 1)
#         else:
#             forward = False
#     else:
#         if color[0] > 0:
#             color = (color[0] - 1, color[1], color[2])
#         elif color[1] > 0:
#             color = (color[0], color[1] - 1, color[2])
#         elif color[2] > 0:
#             color = (color[0], color[1], color[2] - 1)
#         else:
#             forward = True
#     screen.fill(color)
#     pygame.display.flip()
