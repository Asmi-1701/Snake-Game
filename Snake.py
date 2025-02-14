import pygame

# Initialize pygame
pygame.init()

# Set game window dimensions
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Snake settings
snake_size = 20  
snake_x = WIDTH // 2
snake_y = HEIGHT // 2
snake_dx = 0  
snake_dy = 0  
speed = 10  

# Game loop
running = True
clock = pygame.time.Clock()

import random  # Import random for food placement

# Food settings
food_size = 20  
food_x = random.randint(0, (WIDTH - food_size) // food_size) * food_size
food_y = random.randint(0, (HEIGHT - food_size) // food_size) * food_size
RED = (255, 0, 0)  # Food color

# Snake body (list of segments)
snake_body = [(snake_x, snake_y)]

# Font settings
font = pygame.font.Font(None, 30)  # Default pygame font, size 30
score = 0  # Initialize score

def draw_text(text, x, y, color):
    """Function to draw text on screen."""
    text_surface = font.render(text, True, color)
    win.blit(text_surface, (x, y))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Detect key presses to move the snake
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -snake_size
                snake_dy = 0
            elif event.key == pygame.K_RIGHT:
                snake_dx = snake_size
                snake_dy = 0
            elif event.key == pygame.K_UP:
                snake_dx = 0
                snake_dy = -snake_size
            elif event.key == pygame.K_DOWN:
                snake_dx = 0
                snake_dy = snake_size

    # Update snake position
    snake_x += snake_dx
    snake_y += snake_dy

    # Check if the snake hits the wall
    if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
        running = False  # End the game

   # Check if the snake eats the food
    if snake_x == food_x and snake_y == food_y:
        food_x = random.randint(0, (WIDTH - food_size) // food_size) * food_size
        food_y = random.randint(0, (HEIGHT - food_size) // food_size) * food_size
        snake_body.append((snake_x, snake_y))  # Add new segment
        score += 1  # Increase score



    # Move the snake body
    snake_body.insert(0, (snake_x, snake_y))  # Insert new head
    if len(snake_body) > 1:
        snake_body.pop()  # Remove last segment if not eating

    # Check if the snake hits itself
    if (snake_x, snake_y) in snake_body[1:]:
        running = False  # End the game

    # Fill screen
    win.fill(BLACK)

    # Draw the food
    pygame.draw.rect(win, RED, (food_x, food_y, food_size, food_size))

    # Draw the snake
    for segment in snake_body:
        pygame.draw.rect(win, GREEN, (segment[0], segment[1], snake_size, snake_size))

    # Display Score
    draw_text(f"Score: {score}", 10, 10, (255, 255, 255))  # White text at top left

    pygame.display.update()
    clock.tick(speed)

# Show Game Over message
win.fill(BLACK)
draw_text("Game Over!", WIDTH // 2 - 60, HEIGHT // 2 - 20, (255, 0, 0))  # Red text in center
draw_text(f"Final Score: {score}", WIDTH // 2 - 70, HEIGHT // 2 + 10, (255, 255, 255))  # White text
pygame.display.update()

# Wait before closing
pygame.time.delay(2000)  # Pause for 2 seconds
pygame.quit()

pygame.quit()
