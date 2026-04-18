import pygame
import random

class Cloud:
    """Individual cloud"""
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.speed = random.uniform(0.3, 0.8)
        
    def update(self, screen_width):
        self.x -= self.speed
        if self.x < -100:
            self.x = screen_width + 50
            
    def draw(self, screen):
        # White fluffy cloud
        color = (255, 255, 255, 180)
        surface = pygame.Surface((self.size * 2, self.size), pygame.SRCALPHA)
        
        # Draw cloud circles
        pygame.draw.circle(surface, color, (self.size // 2, self.size // 2), self.size // 2)
        pygame.draw.circle(surface, color, (self.size, self.size // 2), self.size // 3)
        pygame.draw.circle(surface, color, (self.size * 1.5, self.size // 2), self.size // 2)
        
        screen.blit(surface, (int(self.x), int(self.y)))


class Ground:
    """Scrolling ground"""
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.height = 112
        self.y = screen_height - self.height
        
        self.x1 = 0
        self.x2 = screen_width
        self.speed = 3
        
    def update(self):
        self.x1 -= self.speed
        self.x2 -= self.speed
        
        if self.x1 + self.screen_width <= 0:
            self.x1 = self.x2 + self.screen_width
        if self.x2 + self.screen_width <= 0:
            self.x2 = self.x1 + self.screen_width
    
    def draw(self, screen):
        # Ground color - tan/brown
        ground_color = (222, 216, 149)
        grass_color = (125, 186, 66)
        
        # Draw ground rectangles
        pygame.draw.rect(screen, ground_color, (self.x1, self.y, self.screen_width, self.height))
        pygame.draw.rect(screen, ground_color, (self.x2, self.y, self.screen_width, self.height))
        
        # Grass strip
        pygame.draw.rect(screen, grass_color, (self.x1, self.y, self.screen_width, 15))
        pygame.draw.rect(screen, grass_color, (self.x2, self.y, self.screen_width, 15))


class ScrollingBackground:
    """Beautiful gradient background with clouds and ground"""
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Create gradient background
        self.background = pygame.Surface((screen_width, screen_height))
        self.create_gradient()
        
        # Create clouds
        self.clouds = []
        for i in range(5):
            x = random.randint(0, screen_width)
            y = random.randint(50, 250)
            size = random.randint(30, 50)
            self.clouds.append(Cloud(x, y, size))
        
        # Create ground
        self.ground = Ground(screen_width, screen_height)
        
        self.loaded = True
        print("✓ Beautiful gradient background created")
        
    def create_gradient(self):
        """Create sky gradient - light blue to darker blue"""
        for y in range(self.screen_height):
            # Gradient from light sky blue to deeper blue
            progress = y / self.screen_height
            
            # Top color: Light sky blue (135, 206, 235)
            # Bottom color: Deeper blue (70, 130, 180)
            r = int(135 - (135 - 70) * progress)
            g = int(206 - (206 - 130) * progress)
            b = int(235 - (235 - 180) * progress)
            
            pygame.draw.line(self.background, (r, g, b), (0, y), (self.screen_width, y))
        
    def update(self):
        """Update clouds and ground"""
        for cloud in self.clouds:
            cloud.update(self.screen_width)
        self.ground.update()
    
    def draw(self, screen):
        """Draw background, clouds, and ground"""
        # Draw gradient
        screen.blit(self.background, (0, 0))
        
        # Draw clouds
        for cloud in self.clouds:
            cloud.draw(screen)
        
        # Draw ground
        self.ground.draw(screen)