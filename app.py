import pygame
import sys
from settings import Settings


# Initialize Pygame
def __init__(self):
    pygame.init()
    self.settings = Settings()
    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))


# Screen dimensions
# WIDTH, HEIGHT = 1280, 720
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chris Crook's CV")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)

# Character properties
character_width = 50
character_height = 50
character_x = 64
character_y = HEIGHT // 2 - character_height // 2
character_speed = 100

# Buttons

# Button class
class Button:
    def __init__(self, x, y, width, height, color, text, font_size=24):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.Font(None, font_size)
    
    def draw(self, screen):
        # Draw button
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, WHITE)
        screen.blit(text_surface, text_surface.get_rect(center=self.rect.center))
    
    def is_clicked(self, pos):
        # Check if mouse click is inside the button
        return self.rect.collidepoint(pos)

# Next Button Clicks
next_clicks = 0  # Counter to track how many times the Next button has been clicked
max_next_clicks = 10  # Maximum number of Next button clicks allowed

# Clock to control frame rate
clock = pygame.time.Clock()

# List to store shapes (position, shape_type)
shapes = []  # This will store shape information (position and type)

# Game state
running = True
move_character = False
show_start_button = True
show_next_button = False
show_reset_button = False

# Shape types
shape_types = ['circle_orange', 'circle_red', 'circle_blue', 'circle_green',
               'rectangle_red', 'rectangle_blue', 'rectangle_green', 
               'triangle_red', 'triangle_blue', 'triangle_green']  # List of shapes to cycle through
shape_index = 0  # Keeps track of which shape to draw

# Create buttons
start_button = Button(100, 600, 100, 50, RED, "Start")
next_button = Button(100, 600, 100, 50, RED, "Next")
reset_button = Button(1100, 600, 100, 50, RED, "Reset")

# Function to reset the game state
def reset_game():
    global character_x, shapes, move_character, show_start_button, show_next_button, show_reset_button, next_clicks, shape_index
    character_x = 100
    shapes = []
    move_character = False
    show_start_button = True
    show_next_button = False  # Reset "Next" button visibility
    show_reset_button = False
    next_clicks = 0  # Reset the click counter so it can be used again
    shape_index = 0  # Reset the shape index to start with a circle

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if show_start_button and start_button.is_clicked(event.pos):
                # When Start is clicked:
                move_character = False  # Keep character still initially
                show_start_button = False
                show_next_button = True  # Show the "Next" button after start
                show_reset_button = True  # Show the reset button after start

            if show_next_button and next_button.is_clicked(event.pos):
                if next_clicks < max_next_clicks:
                    next_clicks += 1  # Increment the counter

                    if not move_character:
                        # First time clicking Next, show the circle and move character
                        move_character = True  # Now we can start moving the character
                        character_x += character_speed  # Move the character
                        shape_x = character_x + character_width // 2
                        shape_y = character_y - 30  # Shape appears above the character
                        shapes.append((shape_x, shape_y, shape_types[shape_index]))  # Add the first shape

                    else:
                        # Subsequent clicks of "Next" will move both the character and the shape
                        character_x += character_speed  # Move the character
                        if character_x > WIDTH - character_width:
                            character_x = WIDTH - character_width  # Prevent going off-screen
                        # Add a new shape above the new position of the character
                        shape_x = character_x + character_width // 2
                        shape_y = character_y - 30  # Shape appears above the character
                        shapes.append((shape_x, shape_y, shape_types[shape_index]))  # Add the new shape

                        # Cycle through the shape types
                        shape_index = (shape_index + 1) % len(shape_types)

                else:
                    # If the counter has reached the limit, stop further movement
                    print("Maximum Next clicks reached!")

                # After the click, check if the maximum number of Next clicks has been reached
                if next_clicks >= max_next_clicks:
                    show_next_button = False  # Hide the Next button after 10 clicks

            if show_reset_button and reset_button.is_clicked(event.pos):
                reset_game()  # Call the reset function

    # Drawing
    screen.fill(WHITE)  # Clear the screen

    if move_character:  # Only draw the square if it should be visible
        # Draw the character (blue square)
        pygame.draw.rect(screen, BLUE, (character_x, character_y, character_width, character_height))

    # Draw the shapes if any exist
    for shape_pos in shapes:
        x, y, shape_type = shape_pos
        if shape_type == 'circle_orange':
            pygame.draw.circle(screen, ORANGE, (x, y), 20)  # Draw circle
        elif shape_type == 'circle_red':
            pygame.draw.circle(screen, RED, (x, y), 20)  # Draw circle  
        elif shape_type == 'rectangle_blue':
            pygame.draw.rect(screen, BLUE, (x - 20, y - 20, 40, 40))  # Draw rectangle
        elif shape_type == 'triangle_green':
            pygame.draw.polygon(screen, GREEN, [(x, y - 20), (x - 20, y + 20), (x + 20, y + 20)])  # Draw triangle
        elif shape_type == 'circle_blue':
            pygame.draw.circle(screen, BLUE, (x, y), 20)  # Draw circle  
        elif shape_type == 'rectangle_green':
            pygame.draw.rect(screen, GREEN, (x - 20, y - 20, 40, 40))  # Draw rectangle
        elif shape_type == 'triangle_red':
            pygame.draw.polygon(screen, RED, [(x, y - 20), (x - 20, y + 20), (x + 20, y + 20)])  # Draw triangle
        elif shape_type == 'circle_green':
            pygame.draw.circle(screen, GREEN, (x, y), 20)  # Draw circle  
        elif shape_type == 'rectangle_red':
            pygame.draw.rect(screen, RED, (x - 20, y - 20, 40, 40))  # Draw rectangle
        elif shape_type == 'triangle_blue':
            pygame.draw.polygon(screen, BLUE, [(x, y - 20), (x - 20, y + 20), (x + 20, y + 20)])  # Draw triangle
       
    # Draw buttons
    if show_start_button:
        start_button.draw(screen)
    if show_next_button:
        next_button.draw(screen)
    if show_reset_button:
        reset_button.draw(screen)

    # Update the screen
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
