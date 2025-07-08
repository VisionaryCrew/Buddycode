import requests
from config import API_KEY, MODEL

OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# 🧠 Strict interpreter prompt
SYSTEM_PROMPT = """
You are BuddyCode — a strict Python logic interpreter.

Your mission is:
1. Read the user's logic exactly as it is.
2. If the logic is incomplete, ambiguous, or unclear:
   ✅ DO NOT guess.
   ✅ DO NOT assume defaults.
   ✅ DO NOT write speculative code.
   ❌ DO NOT add behavior not described.
3. Simply return:
"⚠️ Your logic seems incomplete or ambiguous. Please define the steps clearly."

If logic is clear, return:

## 🧠 Reasoning:
[Explain how you’ll implement the described logic]

## 💻 Python Code:
```python
# code here
"""

def generate_code(user_logic):
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
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"❌ API error: {response.status_code}\nDetails: {response.text}"
    except Exception as e:
        return f"❌ Request failed: {str(e)}"