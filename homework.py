import pygame
import sys


pygame.init()


WINDOW_WIDTH, WINDOW_HEIGHT = 500, 500
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My first game screen")


background_color = (58, 58, 58)


image = pygame.image.load("your_image.png")
image = pygame.transform.scale(image, (300, 300))


image_rect = image.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))


running = True
while running:
    screen.fill(background_color)
    screen.blit(image, image_rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
sys.exit()
