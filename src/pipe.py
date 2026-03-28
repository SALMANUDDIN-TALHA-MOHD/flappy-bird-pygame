import pygame
import random

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
    
    @staticmethod
    def generate_random_gap_y(screen_height):
        """Generate random gap position with safe boundaries"""
        # Keep gap away from top and bottom (100px margins)
        min_gap_y = 150
        max_gap_y = screen_height - 150
        return random.randint(min_gap_y, max_gap_y)
    
class PipeManager:
    """
    Manages multiple pipes - spawning, updating, removing
    """
    def __init__(self, screen_width, screen_height):
        """Initialize pipe manager"""
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.pipes = []
        
        # Spawning settings
        self.spawn_distance = 400  # Distance between pipes
        self.next_spawn_x = screen_width + 200  # First pipe position
        
    def update(self):
        """Update all pipes"""
        # Move all pipes
        for pipe in self.pipes:
            pipe.update()
        
        # Remove pipes that are off-screen
        self.pipes = [pipe for pipe in self.pipes if not pipe.is_off_screen()]
        
        # Spawn new pipe if needed
        if len(self.pipes) == 0 or self.pipes[-1].x < self.next_spawn_x:
            self.spawn_pipe()
            
    def spawn_pipe(self):
        """Create a new pipe at the right edge"""
        gap_y = Pipe.generate_random_gap_y(self.screen_height)
        new_pipe = Pipe(self.screen_width, gap_y)
        self.pipes.append(new_pipe)
        self.next_spawn_x = new_pipe.x + self.spawn_distance
        
    def draw(self, screen):
        """Draw all pipes"""
        for pipe in self.pipes:
            pipe.draw(screen)
            
    def get_pipes(self):
        """Return list of all active pipes"""
        return self.pipes