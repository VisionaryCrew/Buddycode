# backend/model_api.py

import requests
from config import API_KEY, MODEL

OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# 🧠 Strict interpreter prompt
SYSTEM_PROMPT = """
You are BuddyCode — a strict Python logic interpreter.

Your mission:
1. Read the user's logic exactly as described.
2. If the logic is incomplete, ambiguous, or intention-based:
   ✅ DO NOT guess.
   ✅ DO NOT assume defaults.
   ✍️ DO NOT write speculative code.
   ❌ DO NOT add behavior not explicitly described.

   Return this instead:
    BuddyCode needs your logic, not just your goal.
   Please describe how you'd like to solve the problem step-by-step.
   BuddyCode is not a chatbot — it's a logic-to-code interpreter.
   

3. If logic is clear, return in this format:
---
## 🧠 Reasoning:
[Explain the interpretation of user's logic]

## 💻 Python Code:
```python
# Python code
```

## ⚠️ Edge Cases:
[List edge cases based strictly on user's logic]
"""

def extract_section(text, section_title):
    if section_title not in text:
        return ""
    parts = text.split(section_title)
    rest = parts[1] if len(parts) > 1 else ""

    stop_titles = ["## 🧠 Reasoning:", "## 💻 Python Code:", "## ⚠️ Edge Cases:"]
    stop_titles.remove(section_title)

    for stop in stop_titles:
        if stop in rest:
            rest = rest.split(stop)[0]

    return rest.strip()

def is_goal_only(user_input):
    user_input = user_input.strip().lower()
    # Basic detection of goal/intention prompts
    goal_keywords = [
        "i want", "give me", "find the", "how do i", "check if", "what is the code",
        "print", "sort", "generate", "get the", "return the", "create a function to"
    ]
    logic_verbs = ["loop", "iterate", "filter", "compare", "check each", "go through"]

    if any(k in user_input for k in goal_keywords) and not any(k in user_input for k in logic_verbs):
        return True
    return False

def is_ambiguous(user_input):
    # Reject only vague generalizations, not valid thresholds
    ambiguous_phrases = [
        "good scores", "high scores", "top marks", "good students", "eligible ones",
        "better ones", "valid ones", "invalid entries"
    ]
    for phrase in ambiguous_phrases:
        if phrase in user_input.lower():
            return True
    return False

def generate_code(user_logic):
    if is_goal_only(user_logic):
        return {
            "reasoning": "⚠️ Your input seems to be a request or goal, not logic.\nPlease describe your approach or the steps to solve it.",
            "code": "No code provided.",
            "edge_cases": "No edge cases identified."
        }

    if is_ambiguous(user_logic):
        return {
            "reasoning": "⚠️ Ambiguous logic or assumptions detected. Please clarify.",
            "code": "No code generated due to unclear logic.",
            "edge_cases": "None."
        }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_logic}
        ]
    }

    try:
        response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            content = response.json()["choices"][0]["message"]["content"]

            return {
                "reasoning": extract_section(content, "## 🧠 Reasoning:"),
                "code": extract_section(content, "## 💻 Python Code:"),
                "edge_cases": extract_section(content, "## ⚠️ Edge Cases:")
            }
        else:
            return {
                "reasoning": "",
                "code": f"❌ API error: {response.status_code}\nDetails: {response.text}",
                "edge_cases": ""
            }

    except Exception as e:
        return {
            "reasoning": "",
            "code": f"❌ Request failed: {str(e)}",
            "edge_cases": ""
        }
