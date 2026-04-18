import pygame
import random
import os

class Pipe:
    """Pipe class - handles individual pipe obstacles"""
    def __init__(self, x, gap_y, gap_size=150):
        """Initialize a pipe pair"""
        self.x = x
        self.gap_y = gap_y
        self.gap_size = gap_size
        
        # Pipe dimensions
        self.width = 80
        self.top_height = gap_y - gap_size // 1.5
        self.bottom_y = gap_y + gap_size // 1.5
        
        # Pipe colors
        self.pipe_color = (205, 97, 85)  # Red-orange
        self.cap_color = (184, 76, 64)    # Darker red
        
        # Movement
        self.speed = 3
        
        # Scoring flag
        self.scored = False
        
        # Load sprite
        if not hasattr(Pipe, '_sprite_loaded'):
            Pipe._load_sprite()
        
    @classmethod
    def _load_sprite(cls):
        """Load pipe sprite"""
        pipe_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'images', 'pipes', 'pipe.png')
        
        try:
            cls._pipe_sprite = pygame.image.load(pipe_path).convert_alpha()
            cls._sprite_loaded = True
            print("✓ Pipe sprite loaded")
        except:
            cls._pipe_sprite = None
            cls._sprite_loaded = False
        
    def update(self):
        """Move pipe to the left"""
        self.x -= self.speed
        
    def draw(self, screen):
        """Draw the pipe pair"""
        screen_height = screen.get_height()
        
        if Pipe._sprite_loaded and Pipe._pipe_sprite:
            # Top pipe
            if self.top_height > 0:
                top_pipe = pygame.transform.flip(Pipe._pipe_sprite, False, True)
                top_pipe = pygame.transform.scale(top_pipe, (self.width, int(self.top_height)))
                screen.blit(top_pipe, (self.x, 0))
            
            # Bottom pipe
            bottom_height = screen_height - self.bottom_y
            if bottom_height > 0:
                bottom_pipe = pygame.transform.scale(Pipe._pipe_sprite, (self.width, int(bottom_height)))
                screen.blit(bottom_pipe, (self.x, int(self.bottom_y)))
        else:
            # Rectangles
            pygame.draw.rect(screen, self.pipe_color, (self.x, 0, self.width, self.top_height))
            pygame.draw.rect(screen, self.cap_color, (self.x - 5, self.top_height - 20, self.width + 10, 20))
            pygame.draw.rect(screen, self.pipe_color, (self.x, self.bottom_y, self.width, screen_height - self.bottom_y))
            pygame.draw.rect(screen, self.cap_color, (self.x - 5, self.bottom_y, self.width + 10, 20))
        
    def is_off_screen(self):
        """Check if pipe is off screen"""
        return self.x + self.width < 0
    
    @staticmethod
    def generate_random_gap_y(screen_height):
        """Generate random gap position"""
        min_gap_y = 220
        max_gap_y = screen_height - 220
        return random.randint(min_gap_y, max_gap_y)


class PipeManager:
    """Manages multiple pipes"""
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.pipes = []
        self.spawn_distance = 280
        
    def update(self):
        """Update all pipes"""
        for pipe in self.pipes:
            pipe.update()
        
        self.pipes = [pipe for pipe in self.pipes if not pipe.is_off_screen()]
        
        if len(self.pipes) == 0:
            self.spawn_pipe()
        else:
            rightmost_pipe = max(self.pipes, key=lambda p: p.x)
            if rightmost_pipe.x < self.screen_width - self.spawn_distance:
                self.spawn_pipe()
            
    def spawn_pipe(self):
        """Create new pipe"""
        gap_y = Pipe.generate_random_gap_y(self.screen_height)
        
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
        """Get all pipes"""
        return self.pipes