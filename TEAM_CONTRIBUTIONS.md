# Team Contributions

This document details who worked on what for the Flappy Bird game project.

---

## Team Overview

**Duration:** 8 weeks (Spring 2026)  
**Commits:** 40+  
**Code:** 1,200+ lines  
**Team:** 3 members

---

## Salmanuddin Talha Mohd - Lead Developer

**Role:** Graduate Student  
**Contribution:** ~85% of codebase

### Code Written:
- `main.py` - Complete game loop, state management
- `bird.py` - Physics engine, animation, collision boxes
- `pipe.py` - Pipe generation, spawning algorithm
- `collision.py` - Collision detection system
- `score.py` - Scoring logic
- `menu.py` - UI screens, state transitions
- `background.py` - Procedural graphics (gradient, clouds, ground)

### Key Implementations:
- Game architecture design (modular, single-responsibility)
- Physics system (gravity: 0.35, jump: -8, max fall: 8)
- Pipe spawning with random safe gaps
- Collision detection with forgiving hitboxes
- Fixed critical scoring bug (id() → pipe.scored flag)
- Procedural gradient background with clouds
- Complete game loop (60 FPS)

### Project Management:
- GitHub repository setup
- Code reviews
- Git workflow management
- Integration of all components

**Time:** ~60 hours

---

## Amaan Khan - Asset Manager

**Role:** Undergraduate Student  
**Contribution:** All visual/audio assets

### Assets Sourced:
- Bird animation sprites (8 frames)
- Pipe graphics
- 5 sound effects:
  - `wing.wav` - Wing flap
  - `point.wav` - Score sound
  - `hit.wav` - Collision
  - `fall.wav` - Falling
  - `gameover.wav` - Game over

### Technical Work:
- Sprite integration into Pygame
- Cross-platform asset testing
- Sound format conversion (MP3 → WAV)
- Asset folder organization
- Visual design feedback

### Testing:
- Windows 10 compatibility verification
- Sound system testing
- Visual quality assurance

**Time:** ~40 hours

---

## Sohail Shaik - Quality Assurance Lead

**Role:** Undergraduate Student  
**Contribution:** Testing & documentation

### Testing:
- Developed comprehensive test strategy
- 50+ manual test cases
- 10+ hours dedicated playtesting
- Cross-platform testing (Linux, macOS, Windows)
- 15+ bugs discovered and reported

### Critical Bug Discovery:
1. **Score Freezing** - Detailed reproduction steps led to fix
2. **Premature Game Over** - Identified hitbox issues
3. **Memory Leak** - Found performance degradation
4. **Sound Issues** - Discovered Windows incompatibility

### Code:
- High score persistence system in `score.py`
- File I/O with error handling
- Cross-platform path compatibility

### Documentation:
- TESTING.md
- Progress reports (1-8)
- Testing sections of final report
- Bug tracking and reporting

**Time:** ~45 hours

---

## Collaborative Work

### Weekly Meetings (8 total):
- Progress reviews
- Design decisions
- Priority planning
- Integration coordination

### Communication:
- Daily group chat updates
- Code reviews
- Collaborative debugging
- Resource sharing

### Shared Decisions:
- MIT License selection
- Technology stack (Python/Pygame)
- Game dimensions (600x700)
- Physics constants
- Visual design choices

---

## Feature Ownership

| Feature | Lead | Support |
|---------|------|---------|
| Game Loop | Salmanuddin | Amaan & Sohail |
| Physics | Salmanuddin | Sohail (testing) |
| Pipes | Salmanuddin | Sohail (testing) |
| Collision | Salmanuddin | Amaan & Sohail (bug discovery) |
| Scoring | Salmanuddin | Sohail (bug fix) |
| High Score | Sohail | Salmanuddin (integration) |
| Menus | Salmanuddin | Amaan (design) |
| Background | Salmanuddin | Amaan (feedback) |
| Sounds | Amaan (assets) | Salmanuddin |
| Sprites | Amaan (assets) | Salmanuddin |
| Testing | Sohail | All |
| Documentation | All |

---

**Total:** ~145 hours over 8 weeks

---

## Conclusion

All three members contributed significantly. While Salmanuddin wrote most code, Amaan's assets made it beautiful, and Sohail's testing ensured 
reliability. Success required all three.

---

**Prepared by:** Salmanuddin Talha Mohd, Amaan Khan, Sohail Shaik  
**Last Updated:** April 2026
