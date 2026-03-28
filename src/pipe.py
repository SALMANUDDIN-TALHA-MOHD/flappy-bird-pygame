import pygame

class Pipe:
    """
    Pipe class - handles individual pipe obstacles
    """
    def __init__(self, x, gap_y, gap_size=150):
        """
        Initialize a pipe pair
        x: horizontal position
        gap_y: vertical position of gap center
        gap_size: height of the gap between pipes
        """
        self.x = x
        self.gap_y = gap_y
        self.gap_size = gap_size
        
        # Pipe dimensions
        self.width = 70
        self.top_height = gap_y - gap_size // 2
        self.bottom_y = gap_y + gap_size // 2
        
        # Pipe colors (placeholder - will use sprites later)
        self.pipe_color = (34, 139, 34)  # Green
        self.cap_color = (46, 125, 50)   # Dark green
        
        # Movement
        self.speed = 3
        
    def update(self):
        """Move pipe to the left"""
        self.x -= self.speed
        
    def draw(self, screen):
        """Draw the pipe pair"""
        screen_height = screen.get_height()
        
        # Draw top pipe
        # Pipe body
        pygame.draw.rect(screen, self.pipe_color, 
                        (self.x, 0, self.width, self.top_height))
        # Pipe cap
        pygame.draw.rect(screen, self.cap_color,
                        (self.x - 5, self.top_height - 20, self.width + 10, 20))
        
        # Draw bottom pipe
        # Pipe body
        pygame.draw.rect(screen, self.pipe_color,
                        (self.x, self.bottom_y, self.width, screen_height - self.bottom_y))
        # Pipe cap
        pygame.draw.rect(screen, self.cap_color,
                        (self.x - 5, self.bottom_y, self.width + 10, 20))
        
    def is_off_screen(self):
        """Check if pipe has moved off the left side of screen"""
        return self.x + self.width < 0