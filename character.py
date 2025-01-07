import pygame

class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50  # This is not needed anymore for stickman but kept for compatibility
        self.height = 50  # Same as width
        self.speed = 100

    def create_shape(self, screen):
        # Head
        head_radius = 20
        pygame.draw.circle(screen, (0, 0, 255), (self.x, self.y), head_radius)  # Draw head (circle)
        # Body
        body_length = 40
        pygame.draw.line(screen, (0, 0, 255), (self.x, self.y + head_radius), (self.x, self.y + head_radius + body_length), 5)  # Body (line)
        # Arms
        arm_length = 30
        pygame.draw.line(screen, (0, 0, 255), (self.x - arm_length, self.y + head_radius + 10), (self.x + arm_length, self.y + head_radius + 10), 5)  # Arms (line)
        # Legs
        leg_length = 30
        pygame.draw.line(screen, (0, 0, 255), (self.x, self.y + head_radius + body_length), (self.x - leg_length, self.y + head_radius + body_length + leg_length), 5)  # Left leg (line)
        pygame.draw.line(screen, (0, 0, 255), (self.x, self.y + head_radius + body_length), (self.x + leg_length, self.y + head_radius + body_length + leg_length), 5)  # Right leg (line)

    def move(self):
        self.x += self.speed
        if self.x > 1280 - self.width:
            self.x = 1280 - self.width  # Prevent going off-screen
