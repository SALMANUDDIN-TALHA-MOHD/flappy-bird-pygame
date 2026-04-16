import pygame
import os

class ScrollingBackground:
    """
    Scrolling background with high quality
    """
    def __init__(self, screen_width, screen_height):
        """Initialize scrolling background"""
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Load background with SMOOTH SCALING
        bg_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'images', 'backgrounds', 'background.jpg')
        
        try:
            # Load original
            original_bg = pygame.image.load(bg_path).convert()
            
            # Use SMOOTHSCALE for better quality
            self.background = pygame.transform.smoothscale(original_bg, (screen_width, screen_height))
            self.loaded = True
            print("✓ High quality background loaded")
        except Exception as e:
            print(f"✗ Background load error: {e}")
            self.loaded = False
            self.background = None
        
        # Scrolling positions
        self.x1 = 0
        self.x2 = screen_width
        self.speed = 1
        
    def update(self):
        """Update background scrolling"""
        if not self.loaded:
            return
            
        self.x1 -= self.speed
        self.x2 -= self.speed
        
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
            screen.fill((135, 206, 235))