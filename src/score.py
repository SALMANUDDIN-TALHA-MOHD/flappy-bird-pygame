import pygame

class ScoreManager:
    """
    Manages game scoring system
    """
    def __init__(self):
        """Initialize score manager"""
        self.score = 0
        self.passed_pipes = set()  # Track which pipes have been scored
        
        # Font for score display
        pygame.font.init()
        self.font = pygame.font.Font(None, 72)
        self.font_color = (255, 255, 255)  # White
        
    def update(self, bird, pipes):
        """
        Update score based on bird passing pipes
        bird: Bird object
        pipes: List of Pipe objects
        """
        bird_x = bird.x + bird.width
        
        for pipe in pipes:
            # Check if bird has passed this pipe
            pipe_id = id(pipe)  # Unique identifier for this pipe
            
            # Bird passed pipe if bird's right edge is past pipe's right edge
            if bird_x > pipe.x + pipe.width and pipe_id not in self.passed_pipes:
                self.score += 1
                self.passed_pipes.add(pipe_id)
                print(f"Score: {self.score}")
    
    def draw(self, screen):
        """Draw the score on screen"""
        score_text = self.font.render(str(self.score), True, self.font_color)
        score_rect = score_text.get_rect(center=(screen.get_width() // 2, 50))
        screen.blit(score_text, score_rect)
    
    def reset(self):
        """Reset score to zero"""
        self.score = 0
        self.passed_pipes.clear()
    
    def get_score(self):
        """Get current score"""
        return self.score