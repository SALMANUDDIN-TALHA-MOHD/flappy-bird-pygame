import pygame

class Ground:
    """
    Scrolling ground element for visual effect
    """
    def __init__(self, screen_width, screen_height):
        """Initialize ground"""
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Ground properties
        self.height = 100
        self.y = screen_height - self.height
        
        # Scrolling
        self.x1 = 0
        self.x2 = screen_width
        self.speed = 3
        
        # Color
        self.color = (222, 184, 135)  # Tan/brown
        self.grass_color = (34, 139, 34)  # Green
        
    def update(self):
        """Update ground scrolling"""
        self.x1 -= self.speed
        self.x2 -= self.speed
        
        # Loop ground
        if self.x1 + self.screen_width < 0:
            self.x1 = self.x2 + self.screen_width
        if self.x2 + self.screen_width < 0:
            self.x2 = self.x1 + self.screen_width
    
    def draw(self, screen):
        """Draw the ground"""
        # Draw two ground rectangles for seamless scrolling
        pygame.draw.rect(screen, self.color,
                        (self.x1, self.y, self.screen_width, self.height))
        pygame.draw.rect(screen, self.color,
                        (self.x2, self.y, self.screen_width, self.height))
        
        # Draw grass on top
        pygame.draw.rect(screen, self.grass_color,
                        (self.x1, self.y, self.screen_width, 10))
        pygame.draw.rect(screen, self.grass_color,
                        (self.x2, self.y, self.screen_width, 10))