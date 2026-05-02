# Testing Procedures

This document describes our testing methodology for the Flappy Bird game.

---

## Testing Philosophy

We prioritize:
- Systematic verification of all features
- Cross-platform compatibility
- Edge case exploration
- Performance consistency (60 FPS)
- User experience validation

---

## Manual Testing Procedures

### Test Case 1: Basic Gameplay

**Actions:**
1. Run `python3 run_game.py`
2. Press SPACE to start
3. Press SPACE to jump multiple times
4. Navigate through 5 pipes
5. Intentionally collide with pipe

**Expected Results:**
- Game starts smoothly
- Bird jumps on SPACE press
- Score increments by 1 per pipe
- Game over triggers on collision
- Sounds play appropriately

**Verification:**
- ✅ 60 FPS maintained
- ✅ Score displays correctly
- ✅ Collision detected accurately

---

### Test Case 2: Score Tracking

**Actions:**
1. Start game
2. Pass 10 pipes
3. Note score
4. Game over
5. Check game over screen

**Expected Results:**
- Score increments exactly once per pipe
- No double counting
- No missed pipes
- Final score displayed correctly
- High score updates if exceeded

**Verification:**
- ✅ Each pipe counted once
- ✅ Score = 10 after 10 pipes
- ✅ High score persists after restart

---

### Test Case 3: Collision Detection

**Actions:**
1. Start game
2. Fly into top pipe
3. Restart, fly into bottom pipe  
4. Restart, hit ceiling
5. Restart, hit ground

**Expected Results:**
- Game over on all collision types
- Hit sound plays
- Fall sound plays
- Game over sound plays
- Game over screen appears

**Verification:**
- ✅ All collision types detected
- ✅ Forgiving hitboxes work (10px margin)
- ✅ No false positives

---

### Test Case 4: Menu Navigation

**Actions:**
1. Launch game (start screen appears)
2. Press SPACE to start
3. Cause game over
4. Press R to restart
5. Cause game over again
6. Click PLAY button

**Expected Results:**
- Start screen → Playing → Game Over → Start
- All transitions smooth
- Buttons clickable
- Keyboard shortcuts work

**Verification:**
- ✅ State transitions clean
- ✅ No visual glitches
- ✅ Both mouse and keyboard work

---

### Test Case 5: Sound Effects

**Actions:**
1. Start game
2. Jump (listen for wing sound)
3. Pass pipe (listen for point sound)
4. Collide (listen for hit sound)
5. Observe falling (listen for fall sound)
6. Game over screen (listen for game over sound)

**Expected Results:**
- Wing sound on jump
- Point sound on score
- Hit sound on collision
- Fall sound when falling
- Game over sound at end

**Verification:**
- ✅ All 5 sounds play
- ✅ Sounds synchronized with actions
- ✅ No audio glitches

---

### Test Case 6: Performance

**Actions:**
1. Play for 5 minutes continuously
2. Let 10+ pipes accumulate
3. Rapid SPACE key presses (100+ times)
4. Monitor frame rate

**Expected Results:**
- Consistent 60 FPS throughout
- No slowdown with multiple pipes
- Handles rapid input smoothly
- No memory leaks

**Verification:**
- ✅ 60 FPS maintained
- ✅ No performance degradation
- ✅ Responsive to rapid input

---

### Test Case 7: Edge Cases

**Actions:**
1. Immediate collision (hit first pipe)
2. Mash SPACE rapidly
3. Hold SPACE continuously
4. Alt-tab away and return
5. Restart multiple times quickly

**Expected Results:**
- Game over works on first pipe
- Rapid input handled correctly
- No continuous jumping when holding
- Game handles focus loss
- Clean restarts every time

**Verification:**
- ✅ All edge cases handled
- ✅ No crashes or errors
- ✅ Game remains stable

---

## Cross-Platform Testing

### macOS (13.5, Python 3.9)
- ✅ Game launches
- ✅ All features work
- ✅ 60 FPS maintained
- ✅ Sounds play correctly

### Windows 10 (Python 3.10)
- ✅ Game launches  
- ✅ All features work
- ✅ 60 FPS maintained
- ✅ Sounds play correctly (after WAV conversion)

### Linux Ubuntu (24.04, Python 3.11)
- ✅ Game launches
- ✅ All features work
- ✅ 60 FPS maintained
- ✅ Sounds play correctly

---

## Bugs Discovered & Resolved

### Critical Bug: Score Freezing
- **Found by:** Salmanuddin &  Sohail (playtesting)
- **Symptom:** Score stopped at 3, 7, randomly
- **Cause:** Python id() reuse after garbage collection
- **Fix:** Added `pipe.scored` boolean flag
- **Status:** ✅ RESOLVED

### Bug: Premature Game Over
- **Found by:** Sohail (testing)
- **Symptom:** Game over without visible collision
- **Cause:** Hitboxes too strict
- **Fix:** Reduced bird hitbox by 10px
- **Status:** ✅ RESOLVED

### Bug: Sound Format Issues
- **Found by:** Amaan (Windows testing)
- **Symptom:** No sound on Windows
- **Cause:** MP3 format incompatibility
- **Fix:** Converted all to WAV
- **Status:** ✅ RESOLVED

### Bug: Memory Leak
- **Found by:** Salmanuddin (performance testing)
- **Symptom:** Slowdown after long play
- **Cause:** Pipes not removed from list
- **Fix:** Proper cleanup in update()
- **Status:** ✅ RESOLVED

---

## Testing Metrics

- **Test Cases:** 50+
- **Bugs Found:** 15+
- **Testing Hours:** 10+ dedicated
- **Playtesters:** 12 people
- **Platforms:** 3 (macOS, Windows, Linux)
- **Pass Rate:** 100% in final version

---

## Conclusion

Our systematic testing ensured a polished, reliable game. The combination of manual testing, cross-platform verification, and user playtesting 
caught all critical bugs and validated quality.

---
  
**Last Updated:** April 2026
