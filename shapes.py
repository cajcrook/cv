import pygame

class Shape:
    def __init__(self, x, y, shape_type):
        self.x = x
        self.y = y
        self.shape_type = shape_type
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)

        self.shape_data = {
            'text_1': ("Hi, I'm Chris", self.white),
            'text_2': ("Formerly an operations manager, now building a new career in Software Engineering", self.white),
            'text_3': ("Fueled by a love of technology…", self.white),
            'text_4': ("I completed a Software Engineering Bootcamp at Makers Academy, gaining expertise in…", self.white),
            'text_5': ("Front End, Back End and Mobile development, applying Object-Oriented Programming and Test-Driven Development", self.white),
            'text_6': ("In my previous career I established a Wholesale Operations Department, implemented scalable processes, including system upgrades, enhancing efficiency and the user experience.", self.white),
            'text_7': ("I’m passionate about continuous learning, collaboration, and leveraging past experience to create impactful digital solutions!", self.white),
            'text_8': ("Thank you for checking out my fun side project, my CV contains a lot more information. I look forward to hearing from you!", self.white),
            'text_9': ("(this game is still a WIP)", self.white)
        }

    def draw(self, screen):
        font_normal = pygame.font.SysFont("Arial", 16)  # Set font to Arial
        max_width = 300  # Set a max width for text wrapping
        padding = 20  # Extra padding for better spacing

        if self.shape_type in self.shape_data:
            text, color = self.shape_data[self.shape_type]

            # Dynamically wrap text based on actual font size
            words = text.split()
            wrapped_lines = []
            line = ""
            for word in words:
                test_line = line + word + " "
                test_width, _ = font_normal.size(test_line)
                if test_width > max_width:
                    wrapped_lines.append(line)
                    line = word + " "
                else:
                    line = test_line
            wrapped_lines.append(line)  # Add last line

            # Calculate total height of the text block
            line_height = font_normal.get_height()
            total_text_height = len(wrapped_lines) * line_height

            # Find the actual widest line (based on pixel width)
            text_width = max(font_normal.size(line)[0] for line in wrapped_lines)

            # Determine the size of the rectangle dynamically
            rect_width = text_width + padding * 2  # Add horizontal padding
            rect_height = total_text_height + padding  # Add vertical padding

            # Draw the background rectangle
            pygame.draw.rect(
                screen, color,
                (self.x - rect_width // 2, self.y - rect_height // 2, rect_width, rect_height),
                border_radius=10  # Rounded corners
            )

            # Center the text block inside the rectangle
            start_y = self.y - total_text_height // 2  

            # Render and center each line
            for i, line in enumerate(wrapped_lines):
                text_rendered = font_normal.render(line, True, (0, 0, 0))
                text_rect = text_rendered.get_rect(center=(self.x, start_y + i * line_height))
                screen.blit(text_rendered, text_rect)
