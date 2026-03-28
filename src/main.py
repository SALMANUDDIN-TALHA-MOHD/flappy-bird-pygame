import pygame
import sys
from bird import Bird
from pipe import PipeManager

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
    
    # Debug font
    debug_font = pygame.font.Font(None, 36)
    
    running = True
    
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Jump when spacebar pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()
        
        # Fill background
        screen.fill(SKY_BLUE)
        
        # Update bird physics
        bird.update(SCREEN_HEIGHT)
        
        # Update pipes
        pipe_manager.update()
        
        # Draw pipes
        pipe_manager.draw(screen)
        
        # Draw bird
        bird.draw(screen)
        
        # Draw debug info
        pipe_count = len(pipe_manager.get_pipes())
        debug_text = debug_font.render(f'Pipes: {pipe_count}', True, (255, 255, 255))
        screen.blit(debug_text, (10, 10))
        
        # Update display
        pygame.display.flip()
        
        # Maintain frame rate
        clock.tick(FPS)
    
    # Quit game
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()