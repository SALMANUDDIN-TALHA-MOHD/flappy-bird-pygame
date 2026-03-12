"""
Flappy Bird Game Launcher
Run this file to start the game
"""
import sys
import os

# Add src directory to path so we can import from it
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import and run main
from main import main

if __name__ == "__main__":
    main()