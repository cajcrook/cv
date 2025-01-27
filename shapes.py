import pygame
import sys

class Shape:
    def __init__(self, x, y, shape_type):
        self.x = x
        self.y = y
        self.shape_type = shape_type
        self.blue = (173, 216, 230)
        # self.orange = (255, 165, 0)
        # self.red = (255, 0, 0)
        # self.yellow = (255, 255, 0)
        # self.green = (0, 255, 0)
        
        
    def draw(self, screen):
        font_small = pygame.font.Font(None, 16)  
        font_normal = pygame.font.Font(None, 24)  
        
        if self.shape_type == 'rectangle_blue':
            pygame.draw.rect(screen, self.blue, (self.x - 20, self.y - 20, 80, 40))
            text = font_normal.render("Text", True, (0, 0, 0))  
            text_rect = text.get_rect(center=(self.x, self.y))  
            screen.blit(text, text_rect)  

        elif self.shape_type == 'rectangle_blue':
            pygame.draw.rect(screen, self.blue, (self.x - 20, self.y - 20, 80, 40))
            text = font_normal.render("Text", True, (0, 0, 0))  
            text_rect = text.get_rect(center=(self.x, self.y))  
            screen.blit(text, text_rect)  

        elif self.shape_type == 'rectangle_blue':
            pygame.draw.rect(screen, self.blue, (self.x - 20, self.y - 20, 80, 40))
            text = font_normal.render("Text", True, (0, 0, 0))  
            text_rect = text.get_rect(center=(self.x, self.y))  
            screen.blit(text, text_rect)  

        elif self.shape_type == 'rectangle_blue':
            pygame.draw.rect(screen, self.blue, (self.x - 20, self.y - 20, 80, 40))
            text = font_normal.render("Text", True, (0, 0, 0))  
            text_rect = text.get_rect(center=(self.x, self.y))  
            screen.blit(text, text_rect)  


        elif self.shape_type == 'rectangle_blue':
            pygame.draw.rect(screen, self.blue, (self.x - 20, self.y - 20, 80, 40))
            text = font_normal.render("Text", True, (0, 0, 0))  
            text_rect = text.get_rect(center=(self.x, self.y))  
            screen.blit(text, text_rect)  

        elif self.shape_type == 'rectangle_blue':
            pygame.draw.rect(screen, self.blue, (self.x - 20, self.y - 20, 80, 40))
            text = font_normal.render("Text", True, (0, 0, 0))  
            text_rect = text.get_rect(center=(self.x, self.y))  
            screen.blit(text, text_rect)  

        elif self.shape_type == 'rectangle_blue':
            pygame.draw.rect(screen, self.blue, (self.x - 20, self.y - 20, 80, 40))
            text = font_normal.render("Text", True, (0, 0, 0))  
            text_rect = text.get_rect(center=(self.x, self.y))  
            screen.blit(text, text_rect)  

        elif self.shape_type == 'rectangle_blue':
            pygame.draw.rect(screen, self.blue, (self.x - 20, self.y - 20, 80, 40))
            text = font_normal.render("Text", True, (0, 0, 0))  
            text_rect = text.get_rect(center=(self.x, self.y))  
            screen.blit(text, text_rect)  


        elif self.shape_type == 'rectangle_blue':
            pygame.draw.rect(screen, self.blue, (self.x - 20, self.y - 20, 80, 40))
            text = font_normal.render("Text", True, (0, 0, 0))  
            text_rect = text.get_rect(center=(self.x, self.y))  
            screen.blit(text, text_rect)  

        elif self.shape_type == 'rectangle_blue':
            pygame.draw.rect(screen, self.blue, (self.x - 20, self.y - 20, 80, 40))
            text = font_normal.render("Text", True, (0, 0, 0))  
            text_rect = text.get_rect(center=(self.x, self.y))  
            screen.blit(text, text_rect)  

        elif self.shape_type == 'rectangle_blue':
            pygame.draw.rect(screen, self.blue, (self.x - 20, self.y - 20, 80, 40))
            text = font_normal.render("Text", True, (0, 0, 0))  
            text_rect = text.get_rect(center=(self.x, self.y))  
            screen.blit(text, text_rect)  


        # elif self.shape_type == 'circle_green':
        #     pygame.draw.circle(screen, self.green, (self.x, self.y), 20)
        
        # elif self.shape_type == 'rectangle_red':
        #     pygame.draw.rect(screen, self.red, (self.x - 20, self.y - 20, 40, 40))
        
        # elif self.shape_type == 'triangle_yellow':
        #     pygame.draw.polygon(screen, self.yellow, [(self.x, self.y - 20), (self.x - 20, self.y + 20), (self.x + 20, self.y + 20)])

    