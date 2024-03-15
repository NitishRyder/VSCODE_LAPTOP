import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the screen dimensions
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Set the font for the scoreboard
font = pygame.font.SysFont('calibri', 25)

# Set the ball dimensions
BALL_WIDTH = 15
BALL_HEIGHT = 15

# Set the paddle dimensions
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 70

# Set the paddles' speeds
PADDLE_SPEED = 5

# Set the ball's speed and initial direction
BALL_X_SPEED = 5
BALL_Y_SPEED = 5

# Create the ball
ball = pygame.Rect(SCREEN_WIDTH/2 - BALL_WIDTH/2, SCREEN_HEIGHT/2 - BALL_HEIGHT/2, BALL_WIDTH, BALL_HEIGHT)

# Create the paddles
left_paddle = pygame.Rect(50, SCREEN_HEIGHT/2 - PADDLE_HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(SCREEN_WIDTH - 50 - PADDLE_WIDTH, SCREEN_HEIGHT/2 - PADDLE_HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Set the initial scores
left_score = 0
right_score = 0

# Set the game loop
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Move the paddles according to the key presses
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and left_paddle.y > 0:
        left_paddle.y -= PADDLE_SPEED

    if keys[pygame.K_s] and left_paddle.y < SCREEN_HEIGHT - PADDLE_HEIGHT:
        left_paddle.y += PADDLE_SPEED

    if keys[pygame.K_UP] and right_paddle.y > 0:
        right_paddle.y -= PADDLE_SPEED

    if keys[pygame.K_DOWN] and right_paddle.y < SCREEN_HEIGHT - PADDLE_HEIGHT:
        right_paddle.y += PADDLE_SPEED

    # Move the ball
    ball.x += BALL_X_SPEED
    ball.y += BALL_Y_SPEED

    # Bounce the ball off the top and bottom walls
    if ball.y <= 0 or ball.y >= SCREEN_HEIGHT - BALL_HEIGHT:
        BALL_Y_SPEED = -BALL_Y_SPEED

    # Check if the ball collides with the paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        BALL_X_SPEED = -BALL_X_SPEED

    # Check if the ball goes out of bounds
    if ball.x <= 0:
        right_score += 1
        ball.x = SCREEN_WIDTH/2 - BALL_WIDTH/2
        ball.y = SCREEN_HEIGHT/2 - BALL_HEIGHT/2
        BALL_X_SPEED = -BALL_X_SPEED
    elif ball.x >= SCREEN_WIDTH - BALL_WIDTH:
        left_score += 1
        ball.x = SCREEN_WIDTH/2 - BALL_WIDTH/2
        ball.y = SCREEN_HEIGHT/2 - BALL_HEIGHT/2
        BALL_X_SPEED = -BALL_X_SPEED

    # Update the screen
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle,screen, WHITE, right_paddle)
pygame.draw.ellipse(screen, WHITE, ball)
left_text = font.render(str(left_score), True, WHITE)
right_text = font.render(str(right_score), True, WHITE)
screen.blit(left_text, (50, 10))
screen.blit(right_text, (SCREEN_WIDTH - 50 - right_text.get_width(), 10))
pygame.display.update()
pygame.quit()