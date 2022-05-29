#importing packages
import pygame, random
pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snake Game")
gameDisplay.fill((20, 20, 20))

clock = pygame.time.Clock()

randPos = [random.randrange(1, 800), random.randrange(1, 600)]
apple = pygame.Rect(randPos[0], randPos[1], 10, 10)
snakePos = [385, 285]
snake = pygame.Rect(snakePos[0], snakePos[1], 15, 15)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)
    pygame.draw.rect(gameDisplay, (52, 235, 70), snake)
    pygame.draw.rect(gameDisplay, (255, 0, 0), apple)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        snake.y -= 1
        print("up")
    if keys[pygame.K_DOWN]:
        snake.y += 1
    if keys[pygame.K_RIGHT]:
        snake.x += 1
    if keys[pygame.K_LEFT]:
        snake.x -= 1
    pygame.display.update()
pygame.quit()
quit()
