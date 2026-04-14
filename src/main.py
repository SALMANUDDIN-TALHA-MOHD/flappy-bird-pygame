import pygame
import sys
from bird import Bird
from pipe import PipeManager
from collision import CollisionDetector
from score import ScoreManager, HighScoreManager
from menu import MenuManager, GameState
from sound import SoundManager
from ground import Ground

# Initialize Pygame
pygame.init()
pygame.font.init()

# Game window settings
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird - Team Project")

# Colors
SKY_BLUE = (135, 206, 235)

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
    
    # Add this line:
    ground = Ground(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    # Debug font
    debug_font = pygame.font.Font(None, 36)
    
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
                        # Reset game
                        bird = Bird(100, SCREEN_HEIGHT // 2)
                        pipe_manager = PipeManager(SCREEN_WIDTH, SCREEN_HEIGHT)
                        score_manager.reset()
                        print("Game Started!")
                        
                        # Reset game
                        bird = Bird(100, SCREEN_HEIGHT // 2)
                        pipe_manager = PipeManager(SCREEN_WIDTH, SCREEN_HEIGHT)
                        score_manager.reset()
                
                # Playing state
                elif current_state == GameState.PLAYING:
                    if event.key == pygame.K_SPACE:
                        bird.jump()
                        sound_manager.play_jump()
                    if event.key == pygame.K_p:
                        menu_manager.set_state(GameState.PAUSED)
                
                # Paused state
                elif current_state == GameState.PAUSED:
                    if event.key == pygame.K_p:
                        menu_manager.set_state(GameState.PLAYING)
                
                # Game over state
                elif current_state == GameState.GAME_OVER:
                    if event.key == pygame.K_r:
                        menu_manager.set_state(GameState.START)
        
        # Update game (only when playing)
        if menu_manager.get_state() == GameState.PLAYING:
            # Update bird physics
            bird.update(SCREEN_HEIGHT)
            
            # Update pipes
            pipe_manager.update()
            
            # Add this line:
            ground.update()
            
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
                # Save high score
                high_score_manager.save_high_score(score_manager.get_score())
        
        # Draw everything
        screen.fill(SKY_BLUE)
        
        # Draw game elements
        pipe_manager.draw(screen)
        ground.draw(screen)
        bird.draw(screen)
        
        # Draw score (only when playing)
        if menu_manager.get_state() == GameState.PLAYING:
            score_manager.draw(screen)
        
        # Draw debug info
        pipe_count = len(pipe_manager.get_pipes())
        debug_text = debug_font.render(f'Pipes: {pipe_count}', True, (255, 255, 255))
        screen.blit(debug_text, (10, 10))
        
        # Draw appropriate menu overlay
        if menu_manager.get_state() == GameState.START:
            menu_manager.draw_start_screen(screen)
            # Show high score on start screen
            high_score_text = debug_font.render(f'High Score: {high_score_manager.get_high_score()}', 
                                               True, (255, 255, 0))
            high_score_rect = high_score_text.get_rect(center=(SCREEN_WIDTH // 2, 420))
            screen.blit(high_score_text, high_score_rect)
        
        # Update display
        pygame.display.flip()
        
        # Maintain frame rate
        clock.tick(FPS)
    
    # Quit game
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()