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
| Guesses| Sensical scoring. | nonsensical     | No logic to score      |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
