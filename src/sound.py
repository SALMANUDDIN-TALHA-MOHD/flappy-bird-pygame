import pygame
import os

class SoundManager:
    """
    Manages all game sound effects and music
    """
    def __init__(self):
        """Initialize sound manager"""
        # Initialize pygame mixer
        pygame.mixer.init()
        
        # Sound effects (we'll use simple tones for now)
        self.sounds_loaded = False
        self.load_sounds()
        
    def load_sounds(self):
        """Load sound effects from files or generate simple ones"""
        sounds_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'sounds')
        
        try:
            # Try to load sound files if they exist
            jump_path = os.path.join(sounds_path, 'jump.wav')
            score_path = os.path.join(sounds_path, 'score.wav')
            hit_path = os.path.join(sounds_path, 'hit.wav')
            
            self.jump_sound = pygame.mixer.Sound(jump_path)
            self.score_sound = pygame.mixer.Sound(score_path)
            self.hit_sound = pygame.mixer.Sound(hit_path)
            
            # Set volumes
            self.jump_sound.set_volume(0.3)
            self.score_sound.set_volume(0.4)
            self.hit_sound.set_volume(0.5)
            
            self.sounds_loaded = True
            print("✓ Sound effects loaded successfully")
            
        except Exception as e:
            print(f"✗ Could not load sound files: {e}")
            print("  Game will run without sound effects")
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