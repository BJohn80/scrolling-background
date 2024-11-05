import pygame
import math

pygame.init()

clock = pygame.time.Clock()
FPS = 60

screen_width = 864
screen_height = 936

#game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Chicken Game")

#load image
bg = pygame.image.load('bg1.jpg').convert()
bg_width = bg.get_width()

#define game variables
scroll = 0
tiles = math.ceil(screen_width / bg_width) + 1

#game loop
run = True
while run:

    clock.tick(FPS)
    # draw the scrolling bg
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))

    #scroll bg
    scroll -= 5

    #reset scroll
    if abs(scroll) > bg_width:
        scroll = 0
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()