import pygame

class GameState:
    """Enumeration for game states"""
    START = "start"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"


class MenuManager:
    """
    Manages game menus and state transitions
    """
    def __init__(self, screen_width, screen_height):
        """Initialize menu manager"""
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.state = GameState.START
        
        # Initialize fonts
        pygame.font.init()
        self.title_font = pygame.font.Font(None, 72)
        self.large_font = pygame.font.Font(None, 64)
        self.medium_font = pygame.font.Font(None, 48)
        self.small_font = pygame.font.Font(None, 36)
        
        # Colors
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.yellow = (255, 255, 0)
        
    def draw_start_screen(self, screen):
        """Draw the start menu"""
        # Semi-transparent overlay
        overlay = pygame.Surface((self.screen_width, self.screen_height))
        overlay.set_alpha(180)
        overlay.fill(self.black)
        screen.blit(overlay, (0, 0))
        
        # Title
        title_text = self.title_font.render('FLAPPY BIRD', True, self.yellow)
        title_rect = title_text.get_rect(center=(self.screen_width // 2, 150))
        screen.blit(title_text, title_rect)
        
        # Instructions
        instruction1 = self.medium_font.render('Press SPACE to Start', True, self.white)
        instruction1_rect = instruction1.get_rect(center=(self.screen_width // 2, 280))
        screen.blit(instruction1, instruction1_rect)
        
        instruction2 = self.small_font.render('Press SPACE to Flap', True, self.white)
        instruction2_rect = instruction2.get_rect(center=(self.screen_width // 2, 340))
        screen.blit(instruction2, instruction2_rect)
        
        instruction3 = self.small_font.render('Avoid the Pipes!', True, self.white)
        instruction3_rect = instruction3.get_rect(center=(self.screen_width // 2, 390))
        screen.blit(instruction3, instruction3_rect)
        
    def draw_pause_screen(self, screen):
        """Draw the pause menu"""
        # Semi-transparent overlay
        overlay = pygame.Surface((self.screen_width, self.screen_height))
        overlay.set_alpha(128)
        overlay.fill(self.black)
        screen.blit(overlay, (0, 0))
        
        # Pause text
        pause_text = self.large_font.render('PAUSED', True, self.white)
        pause_rect = pause_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 50))
        screen.blit(pause_text, pause_rect)
        
        # Resume instruction
        resume_text = self.small_font.render('Press P to Resume', True, self.white)
        resume_rect = resume_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 20))
        screen.blit(resume_text, resume_rect)
        
    def draw_game_over_screen(self, screen, score, high_score):
        """Draw the game over screen"""
        # Semi-transparent overlay
        overlay = pygame.Surface((self.screen_width, self.screen_height))
        overlay.set_alpha(150)
        overlay.fill(self.black)
        screen.blit(overlay, (0, 0))
        
        # Game Over text
        game_over_text = self.large_font.render('GAME OVER', True, self.red)
        game_over_rect = game_over_text.get_rect(center=(self.screen_width // 2, 150))
        screen.blit(game_over_text, game_over_rect)
        
        # Score
        score_text = self.medium_font.render(f'Score: {score}', True, self.white)
        score_rect = score_text.get_rect(center=(self.screen_width // 2, 240))
        screen.blit(score_text, score_rect)
        
        # High Score
        high_score_text = self.small_font.render(f'High Score: {high_score}', True, self.yellow)
        high_score_rect = high_score_text.get_rect(center=(self.screen_width // 2, 300))
        screen.blit(high_score_text, high_score_rect)
        
        # Restart instruction
        restart_text = self.medium_font.render('Press R to Restart', True, self.white)
        restart_rect = restart_text.get_rect(center=(self.screen_width // 2, 380))
        screen.blit(restart_text, restart_rect)
        
    def set_state(self, new_state):
        """Change game state"""
        self.state = new_state
        
    def get_state(self):
        """Get current game state"""
        return self.state
    
def draw_start_screen(self, screen):
        """Draw professional start screen"""
        # No overlay - show game in background
        
        # Title with retro pixel font style
        title_text = self.title_font.render('FLAPPY BIRD', True, (255, 215, 0))  # Gold color
        title_rect = title_text.get_rect(center=(self.screen_width // 2, 120))
        
        # Add shadow for title
        shadow = self.title_font.render('FLAPPY BIRD', True, (0, 0, 0))
        shadow_rect = shadow.get_rect(center=(self.screen_width // 2 + 3, 123))
        screen.blit(shadow, shadow_rect)
        screen.blit(title_text, title_rect)
        
        # Get Ready text
        ready_text = self.medium_font.render('GET READY', True, (255, 140, 0))  # Orange
        ready_rect = ready_text.get_rect(center=(self.screen_width // 2, 220))
        screen.blit(ready_text, ready_rect)
        
        # Tap instruction with hand icon style
        tap_text = self.large_font.render('TAP', True, (255, 69, 0))  # Red-orange
        tap_rect = tap_text.get_rect(center=(self.screen_width // 2, 300))
        screen.blit(tap_text, tap_rect)
        
        # Instruction
        inst_text = self.small_font.render('Press SPACE to Start', True, self.white)
        inst_rect = inst_text.get_rect(center=(self.screen_width // 2, 370))
        screen.blit(inst_text, inst_rect)