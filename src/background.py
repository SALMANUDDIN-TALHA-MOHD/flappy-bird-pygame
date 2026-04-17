import pygame
import os

class ScrollingBackground:
    """Scrolling background with HIGH DEFINITION quality"""
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        bg_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'images', 'backgrounds', 'background.jpg')
        
        try:
            # Load with HIGHEST quality settings
            original_bg = pygame.image.load(bg_path).convert()
            
            # Use SMOOTHSCALE for maximum quality
            self.background = pygame.transform.smoothscale(original_bg, (screen_width, screen_height))
            
            # Apply additional sharpening if available
            self.loaded = True
            print("✓ Ultra HD background loaded")
        except Exception as e:
            print(f"✗ Background load error: {e}")
            # Create nice gradient fallback
            self.background = pygame.Surface((screen_width, screen_height))
            for y in range(screen_height):
                color_value = int(135 + (206 - 135) * (y / screen_height))
                pygame.draw.line(self.background, (color_value, color_value + 20, 235), 
                               (0, y), (screen_width, y))
            self.loaded = True
        
        self.x1 = 0
        self.x2 = screen_width
        self.speed = 1
        
    def update(self):
        if not self.loaded:
            return
            
        self.x1 -= self.speed
        self.x2 -= self.speed
        
        if self.x1 + self.screen_width <= 0:
            self.x1 = self.x2 + self.screen_width
        if self.x2 + self.screen_width <= 0:
            self.x2 = self.x1 + self.screen_width
    
    def draw(self, screen):
        if self.loaded:
            screen.blit(self.background, (int(self.x1), 0))
            screen.blit(self.background, (int(self.x2), 0))