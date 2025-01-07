import pygame
import sys

class Button:
    def __init__(self, x, y, width, height, color, text, font_size=24):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.Font(None, font_size)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        screen.blit(text_surface, text_surface.get_rect(center=self.rect.center))
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)