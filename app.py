import pygame
import sys
from button import Button
from character import Character
from shapes import Shape
from settings import Settings

class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Chris Crook's CV")
        
        self.clock = pygame.time.Clock()
        self.running = True
                
        # Load background image
        self.background = pygame.image.load('assets/background.jpg')  # Replace with your image path
        self.background = pygame.transform.scale(self.background, (2728, 915))  # Scale the background to fit the screen
        self.background_width = self.background.get_width()  # Get the width of the scaled background
        self.background_height = self.background.get_height()  # Get the height of the scaled background
        
        # Initialize buttons
        self.start_button = Button(100, 600, 100, 50, (255, 0, 0), "Start")
        self.next_button = Button(100, 600, 100, 50, (255, 0, 0), "Next")
        self.reset_button = Button(1100, 600, 100, 50, (255, 0, 0), "Reset")
        
        # Initialize player character
        self.character = Character(200, 450)

        # Initialize game variables
        self.shapes = []
        self.move_character = False 
        self.show_start_button = True
        self.show_next_button = False
        self.show_reset_button = False
        self.next_clicks = 0
        self.max_next_clicks = 9
        self.shape_index = 0

        # Background scrolling position
        self.bg_x = 0  # The initial x-position of the background

        # Pre-determined positions for the character (x, y)
        self.character_positions = [
            (160, 500),  # Position 1
                (280, 450),  # Position 2
                    (400, 400),  # Position 3
                        (520, 350),  # Position 4
                            (640, 300),  # Position 5
                        (760, 350),  # Position 6
                    (880, 400),  # Position 7
                (1000, 450),  # Position 8
            (1120, 500),  # Position 9
        ]
        self.current_position_index = 0  # Track the current index of the character's position

    def reset_game(self):
        # Reset to the first position in the predefined list
        self.character.x, self.character.y = self.character_positions[0]
        self.shapes = []
        self.move_character = False
        self.show_start_button = True
        self.show_next_button = False
        self.show_reset_button = False
        self.next_clicks = 0
        self.shape_index = 0
        self.bg_x = 0  # Reset the background position when resetting the game
        self.current_position_index = 0  # Track the current index of the character's position


    def draw_buttons(self):
        if self.show_start_button:
            self.start_button.draw(self.screen)
        if self.show_next_button:
            self.next_button.draw(self.screen)
        if self.show_reset_button:
            self.reset_button.draw(self.screen)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.show_start_button and self.start_button.is_clicked(event.pos):
                    # Place character at the first position
                    self.character.x, self.character.y = self.character_positions[0]
                    self.move_character = False
                    self.show_start_button = False
                    self.show_next_button = True
                    self.show_reset_button = True

                if self.show_next_button and self.next_button.is_clicked(event.pos):
                    if self.next_clicks < self.max_next_clicks:
                        self.next_clicks += 1

                        # Hide character and shapes before moving
                        self.move_character = False

                        # Remove old shapes
                        self.shapes = []

                        # Update character's position to the next one in the list
                        self.character.x, self.character.y = self.character_positions[self.current_position_index]

                        # Create a new shape above the character at the new position
                        if not self.move_character:
                            self.move_character = True
                            self.character.move()  # Move the character to the next position
                            shape = Shape(self.character.x, self.character.y - 150, self.settings.shape_types[self.shape_index])
                            self.shapes.append(shape)
                        else:
                            self.character.move()
                            shape = Shape(self.character.x, self.character.y - 150, self.settings.shape_types[self.shape_index])
                            self.shapes.append(shape)

                        # Debug the created shape
                        print(f"Shape created: {self.settings.shape_types[self.shape_index]} at position ({self.character.x}, {self.character.y - 150})")

                        # Cycle the shape index
                        self.shape_index = (self.shape_index + 1) % len(self.settings.shape_types)

                        # Scroll the background
                        self.bg_x -= 50
                        if self.bg_x <= -self.background_width:
                            self.bg_x = 0

                        # Move to next position in predefined positions
                        self.current_position_index = (self.current_position_index + 1) % len(self.character_positions)

                    else:
                        # Maximum "Next" clicks reached
                        if self.next_clicks >= self.max_next_clicks:
                            self.show_next_button = False
                    
                if self.show_reset_button and self.reset_button.is_clicked(event.pos):
                    self.reset_game()

    def run(self):
        while self.running:
            self.handle_events()

            # Scroll the background
            self.screen.blit(self.background, (self.bg_x, -100))
            if self.bg_x < 0:
                self.screen.blit(self.background, (self.bg_x + self.background_width, 0))

            # Draw the character and shapes only when they are set to move
            if self.move_character:
                self.character.create_shape(self.screen)

            # Draw all shapes
            for shape in self.shapes:
                shape.draw(self.screen)  # Draw each shape in the list

            # Draw buttons
            self.draw_buttons()

            # Update the screen
            pygame.display.flip()

            # Control the frame rate
            self.clock.tick(60)

        pygame.quit()
        sys.exit()



if __name__ == "__main__":
    game = Game()
    game.run()
