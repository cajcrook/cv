import pygame

class Shape:
    def __init__(self, x, y, shape_type):
        self.x = x
        self.y = y
        self.shape_type = shape_type
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)

        # Define texts and associated colors in a dictionary for better structure
        self.shape_data = {
            'text_1': ("Mushroom", self.red),
            'text_2': ("You're a...", self.white),
            'text_3': ("BOB", self.red),
            'text_4': ("Yeh", self.white),
            'text_5': ("You", self.red),
            'text_6': ("BOB", self.white),
            'text_7': ("Mushroom", self.red),
            'text_8': ("Love", self.white),
            'text_9': ("You", self.red)
        }

    def draw(self, screen):
        font_normal = pygame.font.Font(None, 24)  

        # Use the shape_data dictionary to access text and color dynamically
        if self.shape_type in self.shape_data:
            text, color = self.shape_data[self.shape_type]
            
            # Render the text and get the width and height of the rendered text
            text_rendered = font_normal.render(text, True, (0, 0, 0))  
            text_rect = text_rendered.get_rect(center=(self.x, self.y))
            
            # Calculate the width of the rectangle based on the width of the text
            rect_width = text_rect.width + 40  # Add padding around the text
            rect_height = text_rect.height + 20  # Add some padding vertically

            # Draw the rectangle with dynamic size
            pygame.draw.rect(screen, color, (self.x - rect_width // 2, self.y - rect_height // 2, rect_width, rect_height))
            
            # Draw the text
            screen.blit(text_rendered, text_rect)
 





# different shapes
        # elif self.shape_type == 'circle_green':
        #     pygame.draw.circle(screen, self.green, (self.x, self.y), 20)
        
        # elif self.shape_type == 'rectangle_red':
        #     pygame.draw.rect(screen, self.red, (self.x - 20, self.y - 20, 40, 40))
        
        # elif self.shape_type == 'triangle_yellow':
        #     pygame.draw.polygon(screen, self.yellow, [(self.x, self.y - 20), (self.x - 20, self.y + 20), (self.x + 20, self.y + 20)])

    
      # self.blue = (173, 216, 230)
        # self.orange = (255, 165, 0)
        # self.red = (255, 0, 0)
        # self.yellow = (255, 255, 0)
        # self.green = (0, 255, 0)