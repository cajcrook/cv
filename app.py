import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chris Crook's CV")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Character properties
character_width = 50
character_height = 50
character_x = 64
character_y = HEIGHT // 2 - character_height // 2
character_speed = 100

# Buttons
start_button_rect = pygame.Rect(100, 600, 100, 50)
next_button_rect = pygame.Rect(100, 600, 100, 50)
reset_button_rect = pygame.Rect(1100, 600, 100, 50)

# Next Button Clicks
next_clicks = 0  # Counter to track how many times the Next button has been clicked
max_next_clicks = 10  # Maximum number of Next button clicks allowed

# Clock to control frame rate
clock = pygame.time.Clock()

# List to store circle positions
circles = []

# Game state
running = True
move_character = False
show_start_button = True
show_next_button = False
show_reset_button = False

# Function to draw buttons
def draw_buttons():
    if show_start_button:
        pygame.draw.rect(screen, RED, start_button_rect)
        start_text = pygame.font.Font(None, 24).render("Start", True, WHITE)
        screen.blit(start_text, start_text.get_rect(center=start_button_rect.center))

    if show_next_button:
        pygame.draw.rect(screen, RED, next_button_rect)
        next_text = pygame.font.Font(None, 24).render("Next", True, WHITE)
        screen.blit(next_text, next_text.get_rect(center=next_button_rect.center))

    if show_reset_button:
        pygame.draw.rect(screen, RED, reset_button_rect)
        reset_text = pygame.font.Font(None, 24).render("Reset", True, WHITE)
        screen.blit(reset_text, reset_text.get_rect(center=reset_button_rect.center))

# Function to reset the game state
def reset_game():
    global character_x, circles, move_character, show_start_button, show_next_button, show_reset_button, next_clicks
    character_x = 100
    circles = []
    move_character = False
    show_start_button = True
    show_next_button = False  # Reset "Next" button visibility
    show_reset_button = False
    next_clicks = 0  # Reset the click counter so it can be used again

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if show_start_button and start_button_rect.collidepoint(event.pos):
                # When Start is clicked:
                move_character = False  # Keep character still initially
                show_start_button = False
                show_next_button = True  # Show the "Next" button after start
                show_reset_button = True  # Show the reset button after start

            if show_next_button and next_button_rect.collidepoint(event.pos):
                if next_clicks < max_next_clicks:
                    next_clicks += 1  # Increment the counter

                    if not move_character:
                        # First time clicking Next, show the circle and move character
                        move_character = True  # Now we can start moving the character
                        character_x += character_speed  # Move the character
                        circle_x = character_x + character_width // 2
                        circle_y = character_y - 30  # Circle appears above the character
                        circles.append((circle_x, circle_y))  # Add the first circle

                    else:
                        # Subsequent clicks of "Next" will move both the character and the circle
                        character_x += character_speed  # Move the character
                        if character_x > WIDTH - character_width:
                            character_x = WIDTH - character_width  # Prevent going off-screen
                        # Add a new circle above the new position of the character
                        circle_x = character_x + character_width // 2
                        circle_y = character_y - 30  # Circle appears above the character
                        circles.append((circle_x, circle_y))  # Add the new circle

                else:
                    # If the counter has reached the limit, stop further movement
                    print("Maximum Next clicks reached!")

                # After the click, check if the maximum number of Next clicks has been reached
                if next_clicks >= max_next_clicks:
                    show_next_button = False  # Hide the Next button after 10 clicks

            if show_reset_button and reset_button_rect.collidepoint(event.pos):
                reset_game()  # Call the reset function

    # Drawing
    screen.fill(WHITE)  # Clear the screen

    if move_character:  # Only draw the square if it should be visible
        # Draw the character (blue square)
        pygame.draw.rect(screen, BLUE, (character_x, character_y, character_width, character_height))

    # Draw the circles if any exist
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