import pygame

class CollisionDetector:
    """
    Handles all collision detection in the game
    """
    def __init__(self):
        """Initialize collision detector"""
        pass
    
    def check_pipe_collision(self, bird, pipes):
        """
        Check if bird collides with any pipe
        Returns: True if collision detected, False otherwise
        """
        bird_rect = bird.get_rect()
        
        for pipe in pipes:
            # Get pipe rectangles
            top_pipe_rect = pygame.Rect(pipe.x, 0, pipe.width, pipe.top_height)
            bottom_pipe_rect = pygame.Rect(pipe.x, pipe.bottom_y, pipe.width, 500 - pipe.bottom_y)
            
            # Check collision with top pipe
            if bird_rect.colliderect(top_pipe_rect):
                return True
            
            # Check collision with bottom pipe
            if bird_rect.colliderect(bottom_pipe_rect):
                return True
        
        return False
    
    def check_boundary_collision(self, bird, screen_height):
        """
        Check if bird hit top or bottom of screen
        Returns: True if collision detected, False otherwise
        """
        # Check if bird hit the ground
        if bird.y + bird.height >= screen_height:
            return True
        
        # Check if bird hit the ceiling
        if bird.y <= 0:
            return True
        
        return False
    
    def check_collision(self, bird, pipes, screen_height):
        """
        Check all collision types
        Returns: True if any collision detected, False otherwise
        """
        # Check pipe collisions
        if self.check_pipe_collision(bird, pipes):
            return True
        
        # Check boundary collisions
        if self.check_boundary_collision(bird, screen_height):
            return True
        
        return False