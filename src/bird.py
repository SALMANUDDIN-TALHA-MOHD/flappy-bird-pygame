import pygame

class Bird:
    """
    Bird class - handles the player character
    """
    def __init__(self, x, y):
        """Initialize the bird"""
        self.x = x
        self.y = y
        self.velocity = 0
        
        # Bird appearance
        self.width = 34
        self.height = 24
        self.color = (255, 255, 0)  # Yellow (temporary)
        
    def draw(self, screen):
        """Draw the bird on screen"""
        pygame.draw.ellipse(screen, self.color, 
                          (self.x, self.y, self.width, self.height))