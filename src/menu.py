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
        self.title_font = pygame.font.Font(None, 72)
        self.large_font = pygame.font.Font(None, 64)
        self.medium_font = pygame.font.Font(None, 48)
        self.small_font = pygame.font.Font(None, 36)
        
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.yellow = (255, 255, 0)
        
    def draw_start_screen(self, screen):
        """Draw professional start screen"""
        title_text = self.title_font.render('FLAPPY BIRD', True, (255, 215, 0))
        title_rect = title_text.get_rect(center=(self.screen_width // 2, 120))
        
        shadow = self.title_font.render('FLAPPY BIRD', True, (0, 0, 0))
        shadow_rect = shadow.get_rect(center=(self.screen_width // 2 + 3, 123))
        screen.blit(shadow, shadow_rect)
        screen.blit(title_text, title_rect)
        
        ready_text = self.medium_font.render('GET READY', True, (255, 140, 0))
        ready_rect = ready_text.get_rect(center=(self.screen_width // 2, 220))
        screen.blit(ready_text, ready_rect)
        
        tap_text = self.large_font.render('TAP', True, (255, 69, 0))
        tap_rect = tap_text.get_rect(center=(self.screen_width // 2, 300))
        screen.blit(tap_text, tap_rect)
        
        inst_text = self.small_font.render('Press SPACE to Start', True, self.white)
        inst_rect = inst_text.get_rect(center=(self.screen_width // 2, 370))
        screen.blit(inst_text, inst_rect)
        
    def draw_game_over_screen(self, screen, score, high_score):
        """Draw professional game over screen"""
        panel_width = 400
        panel_height = 200
        panel_x = (self.screen_width - panel_width) // 2
        panel_y = 150
        
        panel_color = (170, 215, 170)
        border_color = (80, 120, 80)
        
        pygame.draw.rect(screen, border_color, 
                        (panel_x - 4, panel_y - 4, panel_width + 8, panel_height + 8))
        pygame.draw.rect(screen, panel_color,
                        (panel_x, panel_y, panel_width, panel_height))
        
        game_over_text = self.large_font.render('GAME OVER', True, (255, 140, 0))
        game_over_rect = game_over_text.get_rect(center=(self.screen_width // 2, 100))
        
        shadow = self.large_font.render('GAME OVER', True, (0, 0, 0))
        shadow_rect = shadow.get_rect(center=(self.screen_width // 2 + 2, 102))
        screen.blit(shadow, shadow_rect)
        screen.blit(game_over_text, game_over_rect)
        
        score_label = self.small_font.render('SCORE', True, (100, 140, 100))
        score_label_rect = score_label.get_rect(center=(panel_x + 100, panel_y + 50))
        screen.blit(score_label, score_label_rect)
        
        score_value = self.medium_font.render(str(score), True, (0, 0, 0))
        score_value_rect = score_value.get_rect(center=(panel_x + 300, panel_y + 50))
        screen.blit(score_value, score_value_rect)
        
        high_label = self.small_font.render('HIGH SCORE', True, (100, 140, 100))
        high_label_rect = high_label.get_rect(center=(panel_x + 100, panel_y + 120))
        screen.blit(high_label, high_label_rect)
        
        high_value = self.medium_font.render(str(high_score), True, (0, 0, 0))
        high_value_rect = high_value.get_rect(center=(panel_x + 300, panel_y + 120))
        screen.blit(high_value, high_value_rect)
        
        button_y = panel_y + panel_height + 40
        
        play_button_rect = pygame.Rect(self.screen_width // 2 - 180, button_y, 140, 50)
        pygame.draw.rect(screen, (50, 200, 50), play_button_rect)
        pygame.draw.rect(screen, (0, 0, 0), play_button_rect, 3)
        
        play_text = self.medium_font.render('PLAY', True, self.white)
        play_text_rect = play_text.get_rect(center=play_button_rect.center)
        screen.blit(play_text, play_text_rect)
        
        share_button_rect = pygame.Rect(self.screen_width // 2 + 40, button_y, 140, 50)
        pygame.draw.rect(screen, (50, 200, 50), share_button_rect)
        pygame.draw.rect(screen, (0, 0, 0), share_button_rect, 3)
        
        share_text = self.medium_font.render('SHARE', True, self.white)
        share_text_rect = share_text.get_rect(center=share_button_rect.center)
        screen.blit(share_text, share_text_rect)
        
        restart_text = self.small_font.render('Press R or SPACE to Play Again', True, self.white)
        restart_rect = restart_text.get_rect(center=(self.screen_width // 2, button_y + 80))
        screen.blit(restart_text, restart_rect)
        
    def set_state(self, new_state):
        self.state = new_state
        
    def get_state(self):
        return self.state