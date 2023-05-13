import pygame
import time
import random
from os import system

# Clear console
system("cls")

# Initialize Pygame
pygame.init()

system("echo Loading..")

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Set the width and height of the game window
window_width = 800
window_height = 600
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

# Set the speed of the snake and the clock
snake_speed = 15
clock = pygame.time.Clock()

# Set the size of the snake's body part
snake_block_size = 20

# Set the font style and size
font_style = pygame.font.SysFont(None, 50)

# Function to display the score on the screen
def score(score_val):
    value = font_style.render("Score: " + str(score_val), True, white)
    game_window.blit(value, [10, 10])

# Function to draw the snake on the screen
def snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_window, green, [x[0], x[1], snake_block_size, snake_block_size])

# Main game function
def game():
    game_over = False
    game_close = False

    # Initial position and direction of the snake
    x1 = window_width / 2
    y1 = window_height / 2
    x1_change = 0
    y1_change = 0

    # Initial score and length of the snake
    score_val = 0
    snake_list = []
    length_of_snake = 1

    # Randomly generate the position of the food
    foodx = round(random.randrange(0, window_width - snake_block_size) / 20) * 20
    foody = round(random.randrange(0, window_height - snake_block_size) / 20) * 20

    while not game_over:

        while game_close:
            # Display game over message and the final score
            game_window.fill(black)
            game_over_msg = font_style.render("Game Over!", True, red)
            game_over_keys = font_style.render("Press R to restart and Q to quit", True, white)
            game_window.blit(game_over_msg, [window_width / 2.5, window_height / 3])
            game_window.blit(game_over_keys, [window_width / 4.8, window_height / 2])
            score(length_of_snake - 1)
            pygame.display.update()


            # Wait for the player to choose to play again or quit
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game()

        # Respond to events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0

                elif event.key == pygame.K_a:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = snake_block_size
                    x1_change = 0

        # Check if the snake hits the boundaries of the window
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        # Update the position of the snake
        x1 += x1_change
        y1 += y1_change

        # Fill the game window with black color
        game_window.fill(black)

        # Draw the food on the screen
        pygame.draw.rect(game_window, red, [foodx, foody, snake_block_size, snake_block_size])

        # Update the snake's body
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if the snake hits itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw the snake on the screen
        snake(snake_block_size, snake_list)

        # Update the score
        score(length_of_snake - 1)

        # Update the display
        pygame.display.update()

        # Check if the snake eats the food
        if x1 == foodx and y1 == foody:
            # Generate new food
            foodx = round(random.randrange(0, window_width - snake_block_size) / 20) * 20
            foody = round(random.randrange(0, window_height - snake_block_size) / 20) * 20
            # Increase the length of the snake
            length_of_snake += 1
            # Send message to console
            system("echo Collected Food!")

        # Set the speed of the game
        clock.tick(snake_speed)

    # Quit Pygame and exit the program
    pygame.quit()
    quit()


# "Console"
system("cls")
system("echo Welcome to DarkDev's Snake Game!")

# Start the game
game()