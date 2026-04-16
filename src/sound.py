import pygame
import os

class SoundManager:
    """
    Manages all game sound effects
    """
    def __init__(self):
        """Initialize sound manager"""
        pygame.mixer.init()
        self.sounds_loaded = False
        self.load_sounds()
        
    def load_sounds(self):
        """Load sound effects"""
        sounds_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'sounds')
        
        try:
            # Load the actual sound files from your assets
            jump_file = 'driken5482-retro-jump-3-236683 (2).mp3'
            score_file = 'driken5482-retro-select-236670.mp3'
            hit_file = 'driken5482-retro-blip-236676.mp3'
            
            self.jump_sound = pygame.mixer.Sound(os.path.join(sounds_path, jump_file))
            self.score_sound = pygame.mixer.Sound(os.path.join(sounds_path, score_file))
            self.hit_sound = pygame.mixer.Sound(os.path.join(sounds_path, hit_file))
            
            # Set volumes
            self.jump_sound.set_volume(0.4)
            self.score_sound.set_volume(0.5)
            self.hit_sound.set_volume(0.6)
            
            self.sounds_loaded = True
            print("✓ All sound effects loaded successfully")
            
        except Exception as e:
            print(f"✗ Could not load sound files: {e}")
            self.sounds_loaded = False
    
    def play_jump(self):
        """Play jump sound"""
        if self.sounds_loaded:
            self.jump_sound.play()
    
    def play_score(self):
        """Play score sound"""
        if self.sounds_loaded:
            self.score_sound.play()
    
    def play_hit(self):
        """Play collision sound"""
        if self.sounds_loaded:
            self.hit_sound.play()