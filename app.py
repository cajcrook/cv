import pygame
import sys
from button import Button
from character import Character
from shapes import Shape

class Game:
    def __init__(self):
        pygame.init()
        self.WIDTH, self.HEIGHT = 1280, 720
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Chris Crook's CV")
        
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Initialize buttons
        self.start_button = Button(100, 600, 100, 50, (255, 0, 0), "Start")
        self.next_button = Button(100, 600, 100, 50, (255, 0, 0), "Next")
        self.reset_button = Button(1100, 600, 100, 50, (255, 0, 0), "Reset")
        
        # Initialize player character
        self.character = Character(200, self.HEIGHT // 2)

        # Initialize game variables
        self.shapes = []
        self.move_character = False
        self.show_start_button = True
        self.show_next_button = False
        self.show_reset_button = False
        self.next_clicks = 0
        self.max_next_clicks = 10
        self.shape_types = ['circle_orange', 'circle_red', 
                            'rectangle_yellow', 'triangle_green',
                            'circle_yellow', 'rectangle_green', 
                            'triangle_red', 'circle_green', 
                            'rectangle_red', 'triangle_yellow']
        self.shape_index = 0

    def reset_game(self):
        self.character.x = 100
        self.shapes = []
        self.move_character = False
        self.show_start_button = True
        self.show_next_button = False
        self.show_reset_button = False
        self.next_clicks = 0
        self.shape_index = 0

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
                    self.move_character = False
                    self.show_start_button = False
                    self.show_next_button = True
                    self.show_reset_button = True
                    
                if self.show_next_button and self.next_button.is_clicked(event.pos):
                    if self.next_clicks < self.max_next_clicks:
                        self.next_clicks += 1
                        if not self.move_character:
                            self.move_character = True
                            self.character.move()
                            # Create shape above the character
                            shape = Shape(self.character.x, self.character.y - 150, self.shape_types[self.shape_index])
                            self.shapes.append(shape)
                        else:
                            self.character.move()
                            # Create shape above the character
                            shape = Shape(self.character.x, self.character.y - 150, self.shape_types[self.shape_index])
                            self.shapes.append(shape)
                        
                        # Update the shape index to cycle through
                        self.shape_index = (self.shape_index + 1) % len(self.shape_types)
                    else:
                        print("Maximum Next clicks reached!")
                    if self.next_clicks >= self.max_next_clicks:
                        self.show_next_button = False
                if self.show_reset_button and self.reset_button.is_clicked(event.pos):
                    self.reset_game()

    def run(self):
        while self.running:
            self.handle_events()

            # Drawing
            self.screen.fill((255, 255, 255))  # Clear the screen

            # Draw the character (stick man)
            if self.move_character:
                self.character.create_shape(self.screen)

            # Draw the shapes above the character
            for shape in self.shapes:
                shape.draw(self.screen)

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
