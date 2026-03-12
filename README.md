# Flappy Bird - Pygame Project

Open Source Computing Course Project COMP 312/412 - Spring 2026

## Team Members
- Salmanuddin Talha Mohd (Graduate Student)
- Amaan Khan  (Undergraduate)
- Sohail Shaik  (Undergraduate)

## Description
A Flappy Bird-style game built with Python and Pygame. This project implements core game mechanics including physics, collision detection, scoring, and menu systems.

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

## License
MIT License

## Course Information
Comp 312-01E/412-001, Open Source Computing, Spring 2026  
Loyola University Chicago  
Professor: Peter Dordal
