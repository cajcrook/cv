import pygame

class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 0
        self.width = 60  
        self.height = 50  
        self.image = pygame.image.load('assets/character.png')  
        self.image = pygame.transform.scale(self.image, (50, 100))  

    def create_shape(self, screen):
        screen.blit(self.image, (self.x - self.image.get_width() // 2, self.y - self.image.get_height() // 2))
        
    def move(self):
        self.x += self.speed
        if self.x > 1280 - self.width:
            self.x = 1280 - self.width  # Prevent going off-screen









#  Old stick man code
# class Character:
    # def __init__(self, x, y):
    #     self.x = 1280 // 10 
    #     self.y = y + 50
    #     self.width = 60  
    #     self.height = 50  
    #     self.speed = 100

    # def create_shape(self, screen):
    # # Head
    #     head_radius = 20
    #     pygame.draw.circle(screen, (0, 0, 255), (self.x, self.y), head_radius)
    # # Body
    #     body_length = 40
    #     pygame.draw.line(screen, (0, 0, 255), (self.x, self.y + head_radius), (self.x, self.y + head_radius + body_length), 5)
    # # Arms
    #     arm_length = 30
    #     pygame.draw.line(screen, (0, 0, 255), (self.x - arm_length, self.y + head_radius + 10), (self.x + arm_length, self.y + head_radius + 10), 5) 
    # # Left Legs
    #     leg_length = 30
    #     pygame.draw.line(screen, (0, 0, 255), (self.x, self.y + head_radius + body_length), (self.x - leg_length, self.y + head_radius + body_length + leg_length), 5)
    # # Right Legs
    #     pygame.draw.line(screen, (0, 0, 255), (self.x, self.y + head_radius + body_length), (self.x + leg_length, self.y + head_radius + body_length + leg_length), 5)