import pygame
import sys
import os
from bird import Bird
from pipe import PipeManager
from collision import CollisionDetector
from score import ScoreManager, HighScoreManager
from menu import MenuManager, GameState
from sound import SoundManager
from background import ScrollingBackground

# Initialize Pygame
pygame.init()
pygame.font.init()

# Game window settings
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird - Team Project")

# Game clock for FPS control
clock = pygame.time.Clock()
FPS = 60

def main():
    """Main game loop"""
    # Create game objects
    bird = Bird(100, SCREEN_HEIGHT // 2)
    pipe_manager = PipeManager(SCREEN_WIDTH, SCREEN_HEIGHT)
    collision_detector = CollisionDetector()
    score_manager = ScoreManager()
    high_score_manager = HighScoreManager()
    menu_manager = MenuManager(SCREEN_WIDTH, SCREEN_HEIGHT)
    sound_manager = SoundManager()
    scrolling_bg = ScrollingBackground(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    running = True
    
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN:
                current_state = menu_manager.get_state()
                
                # Start screen
                if current_state == GameState.START:
                    if event.key == pygame.K_SPACE:
                        menu_manager.set_state(GameState.PLAYING)
                        # Reset and activate bird
                        bird = Bird(100, SCREEN_HEIGHT // 2)
                        bird.activate()
                        pipe_manager = PipeManager(SCREEN_WIDTH, SCREEN_HEIGHT)
                        score_manager.reset()
                        print("Game Started!")
                
                # Playing state
                elif current_state == GameState.PLAYING:
                    if event.key == pygame.K_SPACE:
                        if not bird.active:
                            bird.activate()
                        bird.jump()
                        sound_manager.play_jump()
                
                # Game over state
                elif current_state == GameState.GAME_OVER:
                    if event.key == pygame.K_r or event.key == pygame.K_SPACE:
                        menu_manager.set_state(GameState.START)
                        # Reset everything
                        bird = Bird(100, SCREEN_HEIGHT // 2)
                        pipe_manager = PipeManager(SCREEN_WIDTH, SCREEN_HEIGHT)
                        score_manager.reset()
        
        # Update game (only when playing)
        if menu_manager.get_state() == GameState.PLAYING:
            # Update scrolling background
            scrolling_bg.update()
            
            # Update bird physics
            bird.update(SCREEN_HEIGHT)
            
            # Update pipes
            pipe_manager.update()
            
            # Update score
            old_score = score_manager.get_score()
            score_manager.update(bird, pipe_manager.get_pipes())
            new_score = score_manager.get_score()
            
            # Play score sound if score increased
            if new_score > old_score:
                sound_manager.play_score()
            
            # Check for collisions
            if collision_detector.check_collision(bird, pipe_manager.get_pipes(), SCREEN_HEIGHT):
                menu_manager.set_state(GameState.GAME_OVER)
                sound_manager.play_hit()
                high_score_manager.save_high_score(score_manager.get_score())
                print(f"Game Over! Final Score: {score_manager.get_score()}")
        
        # Draw scrolling background
        scrolling_bg.draw(screen)
        
        # Draw game elements
        pipe_manager.draw(screen)
        bird.draw(screen)
        
        # Draw score (only when playing)
        if menu_manager.get_state() == GameState.PLAYING:
            score_manager.draw(screen)
        
        # Draw appropriate menu overlay
        if menu_manager.get_state() == GameState.START:
            menu_manager.draw_start_screen(screen)
        elif menu_manager.get_state() == GameState.GAME_OVER:
            menu_manager.draw_game_over_screen(screen, 
                                               score_manager.get_score(),
                                               high_score_manager.get_high_score())
        
        # Update display
        pygame.display.flip()
        
        # Maintain frame rate
        clock.tick(FPS)
    
    # Quit game
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()