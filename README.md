# Flappy Bird - Pygame Project

A complete Flappy Bird implementation built from scratch using Python and Pygame as an open-source learning project.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.5.2-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)


## Team Members
- Salmanuddin Talha Mohd (Graduate Student)
- Amaan Khan  (Undergraduate)
- Sohail Shaik  (Undergraduate)

## Description
A Flappy Bird-style game built with Python and Pygame. This project implements core game mechanics including physics, collision detection, scoring, and menu systems.

## 📖 Mission Statement

**We created this open-source Flappy Bird game to demonstrate game development fundamentals and serve as an educational resource for students learning Python and Pygame.**

Our goals:
- Build a complete, playable game from scratch
- Practice collaborative software development using Git/GitHub
- Create clean, well-documented code that others can learn from
- Contribute to the open-source community

We believe knowledge grows when shared. This project demonstrates core game development concepts including physics simulation, collision detection, procedural generation, and state management - all applicable to any game project.

---

## ✨ Features

- **60 FPS Gameplay** - Smooth, consistent performance
- **Realistic Physics** - Gravity-based movement with acceleration
- **Smart Collision Detection** - Forgiving hitboxes for fair gameplay  
- **Procedural Generation** - Randomized pipe obstacles
- **Score Tracking** - Real-time scoring with persistent high scores
- **Professional UI** - Polished menus and game over screen
- **Sound Effects** - 5 audio effects (wing, score, hit, fall, game over)
- **Beautiful Graphics** - Gradient sky, animated clouds, scrolling ground
- **Cross-Platform** - Works on macOS, Windows, and Linux

## Installation

### Requirements
- Python 3.8 or higher
- Pygame

### Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/flappy-bird-pygame.git
cd flappy-bird-pygame
```

2. Install dependencies:
```bash
pip3 install -r requirements.txt
```

3. Run the game:
```bash
python3 main.py
```

## Project Structure
```
Flappy Bird Game/
├── src/                 # Source code folder
│   ├── main.py         # Main game loop
│   ├── bird.py         # Bird mechanics
│   ├── pipe.py         # Pipe obstacles
│   ├── collision.py    # Collision detection
│   ├── score.py        # Scoring system
│   └── menu.py         # Menu screens
├── assets/              # Game assets
│   ├── images/          # Sprites and graphics
│   │   ├── bird/       # Bird sprites
│   │   ├── pipes/      # Pipe graphics
│   │   └── backgrounds/ # Background images
│   └── sounds/          # Sound effects
├── run_game.py         # Game launcher (run this!)
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## How to Run
```bash
# From project root directory
python3 run_game.py
```

Or run directly from src:
```bash
cd src
python3 main.py
```
## Development Status
- [x] Project setup and repository creation ✅
- [x] Basic game window ✅
- [x] Bird sprite with 8-frame animation ✅
- [x] Gravity physics ✅
- [x] Jump mechanics ✅
- [x] Screen boundaries ✅
- [x] Sprite rotation ✅
- [x] Pipe obstacles ✅
- [x] Collision detection✅
- [x] Score counting up as you pass pipes ✅
- [x] Game over screen with final score ✅
- [x] Restart functionality (press R) ✅
- [x] Menu screens✅
- [x] Pause functionality (press P)✅
- [x] Game over screen with scores✅
- [x] High score tracking (saves to file)✅
- [x] Sound effects (if sound files available)✅
- [x] Scrolling ground✅
- [x] Score flash effect✅

### Controls
- **SPACE** - Jump/Flap, Start game, Restart
- **R** - Restart after game over

## License
MIT License

## Course Information
Comp 312-01E/412-001, Open Source Computing, Spring 2026  
Loyola University Chicago  
Professor: Peter Dordal
