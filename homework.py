import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Custom Event Example")
clock = pygame.time.Clock()

sprite1 = pygame.Rect(100, 100, 60, 60)
sprite2 = pygame.Rect(300, 300, 60, 60)

color1 = (255, 0, 0)
color2 = (0, 255, 0)

CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 2000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == CHANGE_COLOR:
            color1 = (0, 0, 255) if color1 == (255, 0, 0) else (255, 0, 0)
            color2 = (255, 255, 0) if color2 == (0, 255, 0) else (0, 255, 0)

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color1, sprite1)
    pygame.draw.rect(screen, color2, sprite2)
    pygame.display.flip()
    clock.tick(60)
