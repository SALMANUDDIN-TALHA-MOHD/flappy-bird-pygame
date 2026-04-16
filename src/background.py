import pygame
import os

class ScrollingBackground:
    """
    Scrolling background for parallax effect
    """
    def __init__(self, screen_width, screen_height):
        """Initialize scrolling background"""
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Load background
        bg_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'images', 'backgrounds', 'background.jpg')
        
        try:
            self.background = pygame.image.load(bg_path).convert()
            self.background = pygame.transform.scale(self.background, (screen_width, screen_height))
            self.loaded = True
        except:
            self.loaded = False
            self.background = None
        
        # Scrolling positions
        self.x1 = 0
        self.x2 = screen_width
        self.speed = 1  # Slow scroll speed
        
    def update(self):
        """Update background scrolling"""
        if not self.loaded:
            return
            
        self.x1 -= self.speed
        self.x2 -= self.speed
        
        # Loop background
        if self.x1 + self.screen_width <= 0:
            self.x1 = self.x2 + self.screen_width
        if self.x2 + self.screen_width <= 0:
            self.x2 = self.x1 + self.screen_width
    
    def draw(self, screen):
        """Draw scrolling background"""
        if self.loaded:
            screen.blit(self.background, (int(self.x1), 0))
            screen.blit(self.background, (int(self.x2), 0))
        else:
            screen.fill((135, 206, 235))  # Sky blue fallback