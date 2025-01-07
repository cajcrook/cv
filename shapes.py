import pygame
import sys

class Shape:
    def __init__(self, x, y, shape_type):
        self.x = x
        self.y = y
        self.shape_type = shape_type
        self.orange = (255, 165, 0)
        self.red = (255, 0, 0)
        self.yellow = (255, 255, 0)
        self.green = (0, 255, 0)
        
        

    def draw(self, screen):
        if self.shape_type == 'circle_orange':
            pygame.draw.circle(screen, self.orange, (self.x, self.y), 20)
        elif self.shape_type == 'circle_red':
            pygame.draw.circle(screen, self.red, (self.x, self.y), 20)
        elif self.shape_type == 'rectangle_yellow':
            pygame.draw.rect(screen, self.yellow, (self.x - 20, self.y - 20, 40, 40))
        elif self.shape_type == 'triangle_green':
            pygame.draw.polygon(screen, self.green, [(self.x, self.y - 20), (self.x - 20, self.y + 20), (self.x + 20, self.y + 20)])
        elif self.shape_type == 'circle_yellow':
            pygame.draw.circle(screen, self.yellow, (self.x, self.y), 20)
        elif self.shape_type == 'rectangle_green':
            pygame.draw.rect(screen, self.green, (self.x - 20, self.y - 20, 40, 40))
        elif self.shape_type == 'triangle_red':
            pygame.draw.polygon(screen, self.red, [(self.x, self.y - 20), (self.x - 20, self.y + 20), (self.x + 20, self.y + 20)])
        elif self.shape_type == 'circle_green':
            pygame.draw.circle(screen, self.green, (self.x, self.y), 20)
        elif self.shape_type == 'rectangle_red':
            pygame.draw.rect(screen, self.red, (self.x - 20, self.y - 20, 40, 40))
        elif self.shape_type == 'triangle_yellow':
            pygame.draw.polygon(screen, self.yellow, [(self.x, self.y - 20), (self.x - 20, self.y + 20), (self.x + 20, self.y + 20)])

    