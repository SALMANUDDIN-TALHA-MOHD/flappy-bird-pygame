import pygame

class ScoreManager:
    """
    Manages game scoring system
    """
    def __init__(self):
        """Initialize score manager"""
        self.score = 0
        self.passed_pipes = set()
        self.flash_timer = 0
        
        pygame.font.init()
        self.font = pygame.font.Font(None, 72)
        self.font_color = (255, 255, 255)
    
    def update(self, bird, pipes):
        """Update score based on bird passing pipes"""
        if not bird.active:
            return
            
        bird_center_x = bird.x + bird.width // 2
        
        for pipe in pipes:
            pipe_id = id(pipe)
            pipe_center_x = pipe.x + pipe.width // 2
            
            if bird_center_x > pipe_center_x and pipe_id not in self.passed_pipes:
                self.score += 1
                self.passed_pipes.add(pipe_id)
                self.flash_timer = 10
                print(f"Score: {self.score}")
                return
    
    def draw(self, screen):
        """Draw the score on screen with flash effect"""
        if self.flash_timer > 0:
            self.flash_timer -= 1
            color = (255, 255, 0)
        else:
            color = self.font_color
        
        score_text = self.font.render(str(self.score), True, color)
        score_rect = score_text.get_rect(center=(screen.get_width() // 2, 50))
        screen.blit(score_text, score_rect)
    
    def reset(self):
        """Reset score to zero"""
        self.score = 0
        self.passed_pipes.clear()
        self.flash_timer = 0
    
    def get_score(self):
        """Get current score"""
        return self.score


class HighScoreManager:
    """Manages high score persistence"""
    def __init__(self, filename='high_score.txt'):
        import os
        self.filepath = os.path.join(os.path.dirname(__file__), '..', filename)
        self.high_score = self.load_high_score()
        
    def load_high_score(self):
        try:
            with open(self.filepath, 'r') as f:
                return int(f.read().strip())
        except (FileNotFoundError, ValueError):
            return 0
    
    def save_high_score(self, score):
        if score > self.high_score:
            self.high_score = score
            try:
                with open(self.filepath, 'w') as f:
                    f.write(str(score))
                print(f"New High Score: {score}!")
                return True
            except Exception as e:
                print(f"Could not save high score: {e}")
                return False
        return False
    
    def get_high_score(self):
        return self.high_score