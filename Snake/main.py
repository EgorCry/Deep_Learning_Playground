import pygame


pygame.init()
dis = pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.display.set_caption('Snake')
game_over = False

if __name__ == '__main__':
    while not game_over:
        for event in pygame.event.get():
            print(event)

    pygame.quit()
    quit()
