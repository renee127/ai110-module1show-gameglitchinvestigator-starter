# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
Game Glitch Investigator is an interactive Streamlit guessing game designed as an AI debugging exercise, where the player attempts to guess a randomly generated secret integer within a set number of attempts based on selected difficulty levels.
   
- [x] Detail which bugs you found.
1. Reversed higher/lower hints.
2. Difficulty ranges for games incorrect.
3. Scoring incorrect.

- [x] Explain what fixes you applied.
1. Corrected the directional string messages in check_guess and moved the clean numeric comparison logic into logic_utils.py.
2. Removed the str() cast on even attempts so guesses and secrets are strictly compared as integers.
3. Rebalanced get_range_for_difficulty so ranges scale properly (Easy: 1–20, Normal: 1–50, Hard: 1–100).
4. Updated the game-over condition to explicitly display st.session_state.secret in the UI error banner when guesses run out.   


## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

<img width="1280" height="800" alt="image" src="https://github.com/user-attachments/assets/50351fd7-ae9d-4b17-90f8-daeca96dadda" />






1. Started a game on Normal difficulty. Entered guess of 25.
2. 
Entered 3. The game said "Go HIGHER!" and the score went down to -5.
Entered 100. The game said "Go LOWER!" and the score went down to -10.
Entered 100 again (an even attempt). The game still said "Go LOWER!", so the hint stayed correct, but the score went up by 5 to -5. This is a scoring bug I did not fix.
Entered 80. The game said "Go HIGHER!" and the score went back down to -10.
Entered 97. The game showed "Correct!" and the round ended with a win Final score: 20<!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Describe this step -->
6. <!-- Add more steps as needed -->

<img width="1280" height="800" alt="Screenshot 2026-10-07 at 10 58 17 PM" src="https://github.com/user-attachments/assets/0f8fd8f6-479b-4e39-ae8d-477b842f2366" />


# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
