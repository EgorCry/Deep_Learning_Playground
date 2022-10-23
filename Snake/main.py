import pygame
import time


pygame.init()

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.update()
pygame.display.set_caption('Snake')

blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

x1 = dis_width / 2
y1 = dis_height / 2

snake_block = 10

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()
FPS = 30

font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])


game_over = False

if __name__ == '__main__':
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0
            print(event)

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True
        
        x1 += x1_change
        y1 += y1_change

        dis.fill(white)

        pygame.draw.rect(dis, blue, [x1, y1, 10, 10])

        pygame.display.update()

        clock.tick(30)
        
    message('You lost', red)
    pygame.display.update()
    time.sleep(2)

    pygame.quit()
    quit()
