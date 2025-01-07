import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Character Movement with Thought Circles")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Character properties
character_width = 50
character_height = 50
character_x = 100
character_y = HEIGHT // 2 - character_height // 2
character_speed = 10

# Buttons
start_button_rect = pygame.Rect(50, 500, 100, 50)
next_button_rect = pygame.Rect(200, 500, 100, 50)
restart_button_rect = pygame.Rect(600, 500, 100, 50)

# Clock to control frame rate
clock = pygame.time.Clock()

# List to store circle positions
circles = []

# Game state
running = True
move_character = False
show_start_button = True
show_restart_button = False

# Function to draw buttons
def draw_buttons():
    if show_start_button:
        pygame.draw.rect(screen, RED, start_button_rect)
        start_text = pygame.font.Font(None, 24).render("Start", True, WHITE)
        screen.blit(start_text, start_text.get_rect(center=start_button_rect.center))
    
    pygame.draw.rect(screen, RED, next_button_rect)
    next_text = pygame.font.Font(None, 24).render("Next", True, WHITE)
    screen.blit(next_text, next_text.get_rect(center=next_button_rect.center))

    if show_restart_button:
        pygame.draw.rect(screen, RED, restart_button_rect)
        restart_text = pygame.font.Font(None, 24).render("Restart", True, WHITE)
        screen.blit(restart_text, restart_text.get_rect(center=restart_button_rect.center))

# Function to restart the game state
def restart_game():
    global character_x, circles, move_character, show_start_button, show_restart_button
    character_x = 100
    circles = []
    move_character = False
    show_start_button = True
    show_restart_button = False

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if show_start_button and start_button_rect.collidepoint(event.pos):
                move_character = True
                show_start_button = False
                show_restart_button = True

                # Move the character and add the first circle
                character_x += character_speed
                circle_x = character_x + character_width // 2
                circle_y = character_y - 30  # Circle appears above the character
                circles.append((circle_x, circle_y))

            if next_button_rect.collidepoint(event.pos) and move_character:
                # Move the character to the right
                character_x += character_speed

                # Prevent the character from going off-screen
                if character_x > WIDTH - character_width:
                    character_x = WIDTH - character_width

                # Add a circle with information above the character's new position
                circle_x = character_x + character_width // 2
                circle_y = character_y - 30  # Circle appears above the character
                circles.append((circle_x, circle_y))

            if show_restart_button and restart_button_rect.collidepoint(event.pos):
                restart_game()

    # Drawing
    screen.fill(WHITE)  # Clear the screen

    # Draw the character
    pygame.draw.rect(screen, BLUE, (character_x, character_y, character_width, character_height))

    # Draw the circles
    for circle_pos in circles:
        x, y = circle_pos
        pygame.draw.circle(screen, RED, (x, y), 20)  # Draw circle

    # Draw buttons
    draw_buttons()

    # Update the screen
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
