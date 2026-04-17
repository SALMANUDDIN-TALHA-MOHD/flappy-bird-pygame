import pygame

class CollisionDetector:
    """Handles all collision detection"""
    def __init__(self):
        pass
    
    def check_pipe_collision(self, bird, pipes):
        """Check if bird collides with any pipe"""
        # Make collision slightly more forgiving
        bird_rect = pygame.Rect(bird.x + 5, bird.y + 5, bird.width - 10, bird.height - 10)
        
        for pipe in pipes:
            # Get pipe rectangles
            top_pipe_rect = pygame.Rect(pipe.x, 0, pipe.width, pipe.top_height)
            bottom_pipe_rect = pygame.Rect(pipe.x, pipe.bottom_y, pipe.width, 700 - pipe.bottom_y)
            
            # Check collision
            if bird_rect.colliderect(top_pipe_rect) or bird_rect.colliderect(bottom_pipe_rect):
                return True
        
        return False
    
    def check_boundary_collision(self, bird, screen_height):
        """Check if bird hit top or bottom of screen"""
        if bird.y + bird.height >= screen_height:
            return True
        if bird.y <= 0:
            return True
        return False
    
    def check_collision(self, bird, pipes, screen_height):
        """Check all collision types"""
        if not bird.active:
            return False
            
        if self.check_pipe_collision(bird, pipes):
            return True
        
        if self.check_boundary_collision(bird, screen_height):
            return True
        
        return False