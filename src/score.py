import pygame

class ScoreManager:
    """Manages game scoring - FIXED VERSION"""
    def __init__(self):
        self.score = 0
        self.flash_timer = 0
        
        pygame.font.init()
        self.font = pygame.font.Font(None, 72)
        self.font_color = (255, 255, 255)
    
    def update(self, bird, pipes):
        """Update score - COMPLETELY FIXED"""
        if not bird.active:
            return
        
        # Check each pipe
        for pipe in pipes:
            # Bird passed pipe if bird's RIGHT edge is past pipe's RIGHT edge
            bird_right = bird.x + bird.width
            pipe_right = pipe.x + pipe.width
            
            # Score when bird passes AND pipe hasn't been scored yet
            if bird_right > pipe_right and not pipe.scored:
                pipe.scored = True
                self.score += 1
                self.flash_timer = 10
                print(f"✓ SCORED! Total: {self.score}")
    
    def draw(self, screen):
        """Draw score with flash effect"""
        if self.flash_timer > 0:
            self.flash_timer -= 1
            color = (255, 255, 0)
        else:
            color = self.font_color
        
        score_text = self.font.render(str(self.score), True, color)
        score_rect = score_text.get_rect(center=(screen.get_width() // 2, 80))
        screen.blit(score_text, score_rect)
    
    def reset(self):
        """Reset score"""
        self.score = 0
        self.flash_timer = 0
    
    def get_score(self):
        return self.score


class HighScoreManager:
    """Manages high score"""
    def __init__(self, filename='high_score.txt'):
        import os
        self.filepath = os.path.join(os.path.dirname(__file__), '..', filename)
        self.high_score = self.load_high_score()
        
    def load_high_score(self):
        try:
            with open(self.filepath, 'r') as f:
                return int(f.read().strip())
        except:
            return 0
    
    def save_high_score(self, score):
        if score > self.high_score:
            self.high_score = score
            try:
                with open(self.filepath, 'w') as f:
                    f.write(str(score))
                return True
            except:
                return False
        return False
    
    def get_high_score(self):
        return self.high_score