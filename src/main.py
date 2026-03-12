import pygame
import sys

# Initialize Pygame
pygame.init()

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
    running = True
    
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Fill background
        screen.fill(SKY_BLUE)
        
        # Update display
        pygame.display.flip()
        
        # Maintain frame rate
        clock.tick(FPS)
    
    # Quit game
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()