# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- Hints were backwards. When the actual number was lower, it suggested higher and vice versa.
- Difficulty categories were wrong. Medium was harder (guess a number between 1-100) than the hard category (guess a number between 1-50).
- Scoring system didn't make any sense. Sometimes it was - 7 and othertimes it was - 35.


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

|  Input | Expected Behavior | Actual Behavior | Console Output / Error |
|--------|-------------------|-----------------|------------------------|
|  50    |  Go Lower         |  Go Higher      | Wrong Hint             |
| Medium | # between 1-50    | # between 1-100 | Wrong category.        |
| Guesses| Sensical scoring. | nonsensical     | No logic to score |

---

## 2. How did you use AI as a teammate?

- Claude Code
- Claude suggested fixing the inverted hints in check-guess to fix the higher/lower problem. I tested the game manually.

- The initial recommendation fixed the lower/higher, but it wouldn't display the secret number if the person never guessed it. I worked with Claude to modify the code via a Q & A session. I tested it manually. 

---

## 3. Debugging and testing your fixes

- I checked with developer inspection and also game playthroughs. 
- I played through tests sessions across all three play difficulties. .
- It explained how odd/even attempt counters were manipulating variable types in the background. 

---

## 4. What did you learn about Streamlit and state?

- Streamlit executes Python scripts from top to bottom every single time the user interacts but it keeps session info (like the secret number or attempt count) in a st.session_state.

---
 
## 5. Looking ahead: your developer habits

- I will use the FIXME trick to mark code i suspect is a problem in the future. 
  - I will keep using github desktop. This workflow flows well
- Before applying any AI code suggestion, I will check the user experience and edge-case handling
- The generated code may still contain errors, so it is important to understand what it is actually doing. It seems like breaking each issue into a separate chat helps keep the focus, but it may cause some problems if the fix for problem A causes new problems with problem B.
