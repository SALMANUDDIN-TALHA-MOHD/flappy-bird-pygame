import pygame
import random
import os

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
        
        # Pipe colors (fallback)
        self.pipe_color = (34, 139, 34)  # Green
        self.cap_color = (46, 125, 50)   # Dark green
        
        # Movement
        self.speed = 3
        
        # Load sprite once per class (shared across all instances)
        if not hasattr(Pipe, '_sprite_loaded'):
            Pipe._load_sprite()
        
    @classmethod
    def _load_sprite(cls):
        """Load pipe sprite (class method - called once)"""
        pipe_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'images', 'pipes', 'pipe.png')
        
        try:
            cls._pipe_sprite = pygame.image.load(pipe_path).convert_alpha()
            cls._sprite_loaded = True
            print("✓ Pipe sprite loaded successfully")
        except Exception as e:
            print(f"✗ Could not load pipe sprite: {e}")
            cls._pipe_sprite = None
            cls._sprite_loaded = False
        
    def update(self):
        """Move pipe to the left"""
        self.x -= self.speed
        
    def draw(self, screen):
        """Draw the pipe pair"""
        screen_height = screen.get_height()
        
        if Pipe._sprite_loaded and Pipe._pipe_sprite:
            # Draw using sprites
            
            # Top pipe (flipped upside down)
            if self.top_height > 0:
                top_pipe = pygame.transform.flip(Pipe._pipe_sprite, False, True)
                top_pipe = pygame.transform.scale(top_pipe, (self.width, int(self.top_height)))
                screen.blit(top_pipe, (self.x, 0))
            
            # Bottom pipe (normal orientation)
            bottom_height = screen_height - self.bottom_y
            if bottom_height > 0:
                bottom_pipe = pygame.transform.scale(Pipe._pipe_sprite, (self.width, int(bottom_height)))
                screen.blit(bottom_pipe, (self.x, int(self.bottom_y)))
        else:
            # Fallback: Draw rectangles
            # Top pipe
            pygame.draw.rect(screen, self.pipe_color, 
                            (self.x, 0, self.width, self.top_height))
            pygame.draw.rect(screen, self.cap_color,
                            (self.x - 5, self.top_height - 20, self.width + 10, 20))
            
            # Bottom pipe
            pygame.draw.rect(screen, self.pipe_color,
                            (self.x, self.bottom_y, self.width, screen_height - self.bottom_y))
            pygame.draw.rect(screen, self.cap_color,
                            (self.x - 5, self.bottom_y, self.width + 10, 20))
        
    def is_off_screen(self):
        """Check if pipe has moved off the left side of screen"""
        return self.x + self.width < 0
    
    def get_rects(self):
        """Get collision rectangles for top and bottom pipes"""
        top_rect = pygame.Rect(self.x, 0, self.width, self.top_height)
        bottom_rect = pygame.Rect(self.x, self.bottom_y, self.width, 500 - self.bottom_y)
        return top_rect, bottom_rect
    
    @staticmethod
    def generate_random_gap_y(screen_height):
        """Generate random gap position with safe boundaries"""
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
        self.spawn_distance = 350  # Distance between pipes
        self.last_pipe_x = screen_width  # Track last pipe position
        
    def update(self):
        """Update all pipes"""
        # Move all pipes
        for pipe in self.pipes:
            pipe.update()
        
        # Remove pipes that are off-screen
        self.pipes = [pipe for pipe in self.pipes if not pipe.is_off_screen()]
        
        # Spawn new pipe if needed
        if len(self.pipes) == 0:
            # First pipe
            self.spawn_pipe()
        else:
            # Check if we need to spawn another pipe
            rightmost_pipe = max(self.pipes, key=lambda p: p.x)
            if rightmost_pipe.x < self.screen_width - self.spawn_distance:
                self.spawn_pipe()
            
    def spawn_pipe(self):
        """Create a new pipe at the right edge"""
        gap_y = Pipe.generate_random_gap_y(self.screen_height)
        
        # Calculate spawn position
        if len(self.pipes) == 0:
            spawn_x = self.screen_width + 100
        else:
            rightmost_pipe = max(self.pipes, key=lambda p: p.x)
            spawn_x = rightmost_pipe.x + self.spawn_distance
        
        new_pipe = Pipe(spawn_x, gap_y)
        self.pipes.append(new_pipe)
        
    def draw(self, screen):
        """Draw all pipes"""
        for pipe in self.pipes:
            pipe.draw(screen)
            
    def get_pipes(self):
        """Return list of all active pipes"""
        return self.pipes