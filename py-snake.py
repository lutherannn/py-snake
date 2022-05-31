# importing packages
import pygame, random

pygame.init()
back = (20, 20, 20)
gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
randPos = [random.randrange(1, 800), random.randrange(1, 600)]
apple = pygame.Rect(randPos[0], randPos[1], 10, 10)
snakePos = [385, 285]
snakeLen = 0
snake = pygame.Rect(snakePos[0], snakePos[1], 15, 15)

vel = 5


def drawNewApple():
    newRandPos = [random.randrange(1, 800), random.randrange(1, 600)]
    newApple = pygame.Rect(randPos[0], randPos[1], 10, 10)
    pygame.draw.rect(gameDisplay, (255, 0, 0), newApple)


running = True

gameDisplay.fill(back)
pygame.draw.rect(gameDisplay, (255, 0, 0), apple)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)
    pygame.draw.rect(gameDisplay, (52, 235, 70), snake)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        snake.y -= vel
    if keys[pygame.K_DOWN]:
        snake.y += vel
    if keys[pygame.K_RIGHT]:
        snake.x += vel
    if keys[pygame.K_LEFT]:
        snake.x -= vel
    if snake.colliderect(apple):
        drawNewApple()
    pygame.display.update()
pygame.quit()
quit()
