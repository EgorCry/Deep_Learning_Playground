import pygame


class Mine:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.rect = pygame.Rect((10, 10), (10, 10))

        pygame.screen.fill((255, 255, 255))

        self.x = float()

    def blit_me(self):
        self.screen.blit(self.rect)
