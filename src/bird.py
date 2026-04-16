import pygame
import os

class Bird:
    """
    Bird class - handles the player character with sprite animation
    """
    def __init__(self, x, y):
        """Initialize the bird"""
        self.x = x
        self.y = y
        self.velocity = 0
        
        # Physics constants
        self.gravity = 0.35
        self.max_fall_speed = 8
        self.jump_strength = -8
        
        # Bird size
        self.width = 50
        self.height = 50
        self.rotation = 0
        
        # Game state
        self.active = False
        
        # Animation
        self.current_sprite = 0
        self.animation_time = 0
        self.animation_speed = 5
        
        # Load sprites
        self.load_sprites()
        
    def load_sprites(self):
        """Load bird animation frames"""
        self.sprites = []
        base_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'images', 'bird')
        
        loaded = False
        for i in range(1, 9):
            sprite_path = os.path.join(base_path, f'frame-{i}.png')
            if os.path.exists(sprite_path):
                try:
                    sprite = pygame.image.load(sprite_path).convert_alpha()
                    sprite = pygame.transform.scale(sprite, (self.width, self.height))
                    self.sprites.append(sprite)
                    loaded = True
                except Exception as e:
                    print(f"Error loading {sprite_path}: {e}")
        
        if not loaded or len(self.sprites) == 0:
            print("Warning: Could not load bird sprites, using fallback rectangle")
            surface = pygame.Surface((self.width, self.height))
            surface.fill((255, 255, 0))
            self.sprites.append(surface)
        else:
            print(f"Successfully loaded {len(self.sprites)} bird animation frames")
        
    def update(self, screen_height):
        """Update bird physics and animation"""
        if self.active:
            # Apply gravity
            self.velocity += self.gravity
            
            # Limit fall speed
            if self.velocity > self.max_fall_speed:
                self.velocity = self.max_fall_speed
            
            # Update position
            self.y += self.velocity
            
            # Update rotation based on velocity
            self.rotation = -self.velocity * 3
            if self.rotation > 20:
                self.rotation = 20
            if self.rotation < -90:
                self.rotation = -90
            
            # Keep bird within screen boundaries
            if self.y < 0:
                self.y = 0
                self.velocity = 0
            if self.y > screen_height - self.height:
                self.y = screen_height - self.height
                self.velocity = 0
        else:
            # Gentle hover animation when inactive
            import math
            hover_offset = math.sin(pygame.time.get_ticks() / 200) * 10
            self.y = screen_height // 2 + hover_offset
            self.rotation = 0
        
        # Update animation regardless of active state
        self.animation_time += 1
        if self.animation_time >= self.animation_speed:
            self.animation_time = 0
            self.current_sprite = (self.current_sprite + 1) % len(self.sprites)
        
    def jump(self):
        """Make the bird jump/flap"""
        self.velocity = self.jump_strength
        
    def activate(self):
        """Activate bird (start physics)"""
        self.active = True
    
    def deactivate(self):
        """Deactivate bird (hover mode)"""
        self.active = False
        self.velocity = 0
        
    def draw(self, screen):
        """Draw the bird on screen with rotation and animation"""
        sprite = self.sprites[self.current_sprite]
        
        rotated_sprite = pygame.transform.rotate(sprite, self.rotation)
        rotated_rect = rotated_sprite.get_rect(center=(self.x + self.width // 2, 
                                                        self.y + self.height // 2))
        
        screen.blit(rotated_sprite, rotated_rect)
        
    def get_rect(self):
        """Get collision rectangle for the bird"""
        return pygame.Rect(self.x, self.y, self.width, self.height)