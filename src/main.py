import pygame
import sys
from bird import Bird
from pipe import PipeManager
from collision import CollisionDetector
from score import ScoreManager

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
    # Create bird object
    bird = Bird(100, SCREEN_HEIGHT // 2)
    
    # Create pipe manager
    pipe_manager = PipeManager(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    # Create collision detector
    collision_detector = CollisionDetector()
    
    # Game state
    game_over = False
    
    # Create score manager
    score_manager = ScoreManager()
    
    # Debug font
    debug_font = pygame.font.Font(None, 36)
    game_over_font = pygame.font.Font(None, 64)
    
    running = True
    
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Jump when spacebar pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    bird.jump()
                # Restart game on 'R' key
                if event.key == pygame.K_r and game_over:
                    # Reset everything
                    bird = Bird(100, SCREEN_HEIGHT // 2)
                    pipe_manager = PipeManager(SCREEN_WIDTH, SCREEN_HEIGHT)
                    score_manager.reset()
                    game_over = False
                    print("Game restarted!")
        
        # Fill background
        screen.fill(SKY_BLUE)
        
       # Only update if game is not over
        if not game_over:
            # Update bird physics
            bird.update(SCREEN_HEIGHT)
            
            # Update pipes
            pipe_manager.update()
            
            # Update score
            score_manager.update(bird, pipe_manager.get_pipes())
            
            # Check for collisions
            if collision_detector.check_collision(bird, pipe_manager.get_pipes(), SCREEN_HEIGHT):
                game_over = True
                print("Game Over!")
        
        # Draw pipes
        pipe_manager.draw(screen)
        
        # Draw bird
        bird.draw(screen)
        
        # Draw score
        score_manager.draw(screen)
        
        # Draw debug info
        pipe_count = len(pipe_manager.get_pipes())
        debug_text = debug_font.render(f'Pipes: {pipe_count}', True, (255, 255, 255))
        screen.blit(debug_text, (10, 10))
        
        # Draw game over screen
        if game_over:
            # Semi-transparent overlay
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(128)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))
            
            # Game over text
            game_over_text = game_over_font.render('GAME OVER', True, (255, 0, 0))
            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
            screen.blit(game_over_text, game_over_rect)
            
            # Final score
            final_score_text = debug_font.render(f'Score: {score_manager.get_score()}', True, (255, 255, 255))
            final_score_rect = final_score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
            screen.blit(final_score_text, final_score_rect)
            
            # Restart instruction
            restart_text = debug_font.render('Press R to Restart', True, (255, 255, 255))
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80))
            screen.blit(restart_text, restart_rect)
        
        # Update display
        pygame.display.flip()
        
        # Maintain frame rate
        clock.tick(FPS)
    
    # Quit game
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()