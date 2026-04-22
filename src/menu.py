import pygame

class GameState:
    """Enumeration for game states"""
    START = "start"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"


class MenuManager:
    """Manages game menus and state transitions"""
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.state = GameState.START
        
        pygame.font.init()
        self.title_font = pygame.font.Font(None, 64)
        self.large_font = pygame.font.Font(None, 56)
        self.medium_font = pygame.font.Font(None, 42)
        self.small_font = pygame.font.Font(None, 32)
        self.tiny_font = pygame.font.Font(None, 24)
        
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.yellow = (255, 255, 0)
        self.green = (50, 200, 50)
        
    def draw_start_screen(self, screen):
        """Draw professional start screen"""
        # Title
        title_text = self.title_font.render('FLAPPY BIRD', True, (255, 215, 0))
        title_rect = title_text.get_rect(center=(self.screen_width // 2, 150))
        
        shadow = self.title_font.render('FLAPPY BIRD', True, (0, 0, 0))
        shadow_rect = shadow.get_rect(center=(self.screen_width // 2 + 2, 152))
        screen.blit(shadow, shadow_rect)
        screen.blit(title_text, title_rect)
        
        # Get Ready
        ready_text = self.large_font.render('GET READY', True, (255, 140, 0))
        ready_rect = ready_text.get_rect(center=(self.screen_width // 2, 280))
        screen.blit(ready_text, ready_rect)
        
        # TAP instruction
        tap_text = self.title_font.render('TAP', True, (255, 69, 0))
        tap_rect = tap_text.get_rect(center=(self.screen_width // 2, 380))
        screen.blit(tap_text, tap_rect)
        
        # Instructions
        inst1 = self.small_font.render('Press SPACE to Start', True, self.white)
        inst1_rect = inst1.get_rect(center=(self.screen_width // 2, 480))
        screen.blit(inst1, inst1_rect)
        
        inst2 = self.small_font.render('SPACE to Flap', True, self.white)
        inst2_rect = inst2.get_rect(center=(self.screen_width // 2, 520))
        screen.blit(inst2, inst2_rect)
        
        inst3 = self.small_font.render('Avoid the Pipes!', True, self.white)
        inst3_rect = inst3.get_rect(center=(self.screen_width // 2, 560))
        screen.blit(inst3, inst3_rect)
        
    def draw_game_over_screen(self, screen, score, high_score):
        """Draw professional game over screen with team credits"""
        panel_width = 350
        panel_height = 180
        panel_x = (self.screen_width - panel_width) // 2
        panel_y = 200
        
        panel_color = (170, 215, 170)
        border_color = (80, 120, 80)
        
        # Panel
        pygame.draw.rect(screen, border_color, 
                        (panel_x - 4, panel_y - 4, panel_width + 8, panel_height + 8))
        pygame.draw.rect(screen, panel_color,
                        (panel_x, panel_y, panel_width, panel_height))
        
        # Game Over text
        game_over_text = self.large_font.render('GAME OVER', True, (255, 140, 0))
        game_over_rect = game_over_text.get_rect(center=(self.screen_width // 2, 140))
        
        shadow = self.large_font.render('GAME OVER', True, (0, 0, 0))
        shadow_rect = shadow.get_rect(center=(self.screen_width // 2 + 2, 142))
        screen.blit(shadow, shadow_rect)
        screen.blit(game_over_text, game_over_rect)
        
        # Score
        score_label = self.small_font.render('SCORE', True, (100, 140, 100))
        score_label_rect = score_label.get_rect(center=(panel_x + 90, panel_y + 45))
        screen.blit(score_label, score_label_rect)
        
        score_value = self.medium_font.render(str(score), True, (0, 0, 0))
        score_value_rect = score_value.get_rect(center=(panel_x + 260, panel_y + 45))
        screen.blit(score_value, score_value_rect)
        
        # High Score
        high_label = self.small_font.render('HIGH SCORE', True, (100, 140, 100))
        high_label_rect = high_label.get_rect(center=(panel_x + 90, panel_y + 115))
        screen.blit(high_label, high_label_rect)
        
        high_value = self.medium_font.render(str(high_score), True, (0, 0, 0))
        high_value_rect = high_value.get_rect(center=(panel_x + 260, panel_y + 115))
        screen.blit(high_value, high_value_rect)
        
        # Buttons
        button_y = panel_y + panel_height + 50
        
        # Play button
        play_button_rect = pygame.Rect(self.screen_width // 2 - 160, button_y, 130, 45)
        pygame.draw.rect(screen, self.green, play_button_rect)
        pygame.draw.rect(screen, (0, 0, 0), play_button_rect, 3)
        
        play_text = self.medium_font.render('PLAY', True, self.white)
        play_text_rect = play_text.get_rect(center=play_button_rect.center)
        screen.blit(play_text, play_text_rect)
        
        # Share button
        share_button_rect = pygame.Rect(self.screen_width // 2 + 30, button_y, 130, 45)
        pygame.draw.rect(screen, self.green, share_button_rect)
        pygame.draw.rect(screen, (0, 0, 0), share_button_rect, 3)
        
        share_text = self.medium_font.render('SHARE', True, self.white)
        share_text_rect = share_text.get_rect(center=share_button_rect.center)
        screen.blit(share_text, share_text_rect)
        
        # TEAM CREDITS - "Built by SALMAN, AMAAN, SOHAIL"
        credit_text = self.tiny_font.render('Built by SALMAN, AMAAN, SOHAIL', True, (20, 20, 20))
        credit_rect = credit_text.get_rect(center=(self.screen_width // 2, self.screen_height - 50))
        screen.blit(credit_text, credit_rect)
        
        # Instruction
        restart_text = self.small_font.render('Press R or SPACE to Play Again', True, self.white)
        restart_rect = restart_text.get_rect(center=(self.screen_width // 2, button_y + 75))
        screen.blit(restart_text, restart_rect)

        
        # Store button rectangles for click detection
        self.play_button_rect = play_button_rect
        self.share_button_rect = share_button_rect
        
    def check_button_click(self, mouse_pos):
        """Check if a button was clicked - returns 'play', 'share', or None"""
        if self.state == GameState.GAME_OVER:
            if hasattr(self, 'play_button_rect') and self.play_button_rect.collidepoint(mouse_pos):
                return 'play'
            if hasattr(self, 'share_button_rect') and self.share_button_rect.collidepoint(mouse_pos):
                return 'share'
        return None
        
    def set_state(self, new_state):
        self.state = new_state
        
    def get_state(self):
        return self.state