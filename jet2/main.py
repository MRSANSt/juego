import pygame
import os
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Jetpack Joyride")

jetpack_image = pygame.image.load(os.path.join('images/boy.png'))
obstacle_image = pygame.image.load(os.path.join('images/jetpack_2-removebg-preview (1).png'))
background_image = pygame.image.load(os.path.join('images/B21rglpIUAEAa4Z.jpg'))
game_over_image = pygame.image.load(os.path.join('images/1258544.jpg'))
jetpack_x=10
jetpack_y = 10
jetpack_width = 100
jetpack_height = 100
obstacle_x = 800
obstacle_y = random.randint(100, 400)
obstacle_width = 100
obstacle_height = 100


scaled_image = pygame.transform.scale(background_image, (800, 600))
scaled_image2 = pygame.transform.scale(game_over_image, (800, 600))

screen.blit(scaled_image, (0, 0))

clock = pygame.time.Clock()
score = 0
running = True

gravity = 5

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        jetpack_y -= 10
    if keys[pygame.K_RIGHT]:
        jetpack_y += 10
    if keys[pygame.K_UP]:
        jetpack_x -= 10


    screen.blit(scaled_image, (0, 0))

    obstacle_x -= 5
    if obstacle_x + obstacle_width < 0:
        obstacle_x = 800
        obstacle_y = random.randint(100, 500)

    jetpack_x += gravity
    if jetpack_x + jetpack_image.get_height() > 600:
        jetpack_x = 600 - jetpack_image.get_height()

    screen.blit(obstacle_image, (obstacle_x, obstacle_y))
    screen.blit(jetpack_image, (jetpack_y, jetpack_x))

    if (jetpack_y + jetpack_image.get_width() > obstacle_x and
        jetpack_y < obstacle_x + obstacle_width and
        jetpack_x + jetpack_image.get_height() > obstacle_y and
        jetpack_x < obstacle_y + obstacle_height):
        screen.blit(scaled_image2, (0, 0))
        pygame.display.flip()

        pygame.time.delay(3000)
        running = False

    pygame.display.flip()


pygame.quit()
