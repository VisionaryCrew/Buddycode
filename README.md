🧠 BuddyCode
The Human Logic-to-Code Interpreter
Strict. Minimal. Intentional.
"You give logic. I give code. No assumptions. No magic."
________________________________________
🚀 Overview
Buddy Code is a deterministic, assumption-free code interpreter. It converts user-defined logic — written in natural but explicit language — into structured Python code, with reasoning and edge case awareness.
Built to:
•	Teach logic-first coding practices
•	Prevent unintended behaviour in generative AI
•	Power backend systems that require human-defined logic, not human intent guesses
________________________________________
Features
Capability	Buddy Code Behaviour
Accepts natural language	✅ Yes — but only if logic is explicitly described
Detects vague goals	✅ Flags and rejects them with clear feedback
Identifies ambiguous phrases	✅ Recognizes and asks for clarification
Formats response in sections	✅ Reasoning, Code, Edge Cases
Assumption-free generation	✅ Never guesses or fills gaps in logic
________________________________________
Example Usage
✅ Valid Input
"Loop through the list of students. If marks >= 75, keep the student. Return the filtered list."
Output:
🧠 Reasoning:
User wants to filter students whose marks are 75 or higher.



💻 Python Code:
```python
filtered = [student for student in students if student['marks'] >= 75]
⚠️ Edge Cases:
•	Missing 'marks' key
•	Non-integer marks
•	Empty student list

❌ Ambiguous Input
```text
"Get top students"
Output:
⚠️ BuddyCode needs your logic, not just your goal.
Please describe how you'd like to solve the problem step-by-step.
BuddyCode is not a chatbot — it's a logic-to-code interpreter.
________________________________________
🧬 Core Philosophy
•	Strict Interpretation: Natural language accepted only when logic is unambiguous.
•	No Guessing: If a step is missing, BuddyCode stops and asks — it does not assume.
•	Educational by Design: Encourages clarity and algorithmic thinking.
"BuddyCode won’t write your dream. It will write what you define."
________________________________________
🛠 Architecture
•	Python backend
•	Uses OpenRouter + models like gpt-4o
•	Filters goal-only and ambiguous logic before calling the model
•	Extracts structured sections from output: Reasoning, Code, Edge Cases
________________________________________


🔧 Setup
1.	Clone the repo:
git clone https://github.com/yourusername/buddycode.git
2.	Add your API key:
# config.py
API_KEY = "your-openrouter-api-key"
MODEL = "openai/gpt-4o"
3.	Install dependencies:
pip install -r requirements.txt
4.	Test it:
from backend.model_api import generate_code
print(generate_code("Filter scores > 70, then average and round to 2 decimals"))
________________________________________
📁 Project Structure
buddycode/🧠 BuddyCode
The Human Logic-to-Code Interpreter
Strict. Minimal. Intentional.
"You give logic. I give code. No assumptions. No magic."
________________________________________
🚀 Overview
BuddyCode is a deterministic, assumption-free code interpreter. It converts user-defined logic — written in natural but explicit language — into structured Python code, with reasoning and edge case awareness.
Built to:
•	Teach logic-first coding practices
•	Prevent unintended behavior in generative AI
•	Power backend systems that require human-defined logic, not human intent guesses
________________________________________
✨ Features
Capability	BuddyCode Behavior
Accepts natural language	✅ Yes — but only if logic is explicitly described
Detects vague goals	✅ Flags and rejects them with clear feedback
Identifies ambiguous phrases	✅ Recognizes and asks for clarification
Formats response in sections	✅ Reasoning, Code, Edge Cases
Assumption-free generation	✅ Never guesses or fills gaps in logic
________________________________________
📦 Example Usage
✅ Valid Input
"Loop through the list of students. If marks >= 75, keep the student. Return the filtered list."
Output:
## 🧠 Reasoning:
User wants to filter students whose marks are 75 or higher.

## 💻 Python Code:
```python
filtered = [student for student in students if student['marks'] >= 75]
⚠️ Edge Cases:
•	Missing 'marks' key
•	Non-integer marks
•	Empty student list

### ❌ Ambiguous Input
```text
"Get top students"
Output:
⚠️ BuddyCode needs your logic, not just your goal.
Please describe how you'd like to solve the problem step-by-step.
BuddyCode is not a chatbot — it's a logic-to-code interpreter.
________________________________________
🧬 Core Philosophy
•	Strict Interpretation: Natural language accepted only when logic is unambiguous.
•	No Guessing: If a step is missing, BuddyCode stops and asks — it does not assume.
•	Educational by Design: Encourages clarity and algorithmic thinking.
"BuddyCode won’t write your dream. It will write what you define."
________________________________________
🛠 Architecture
•	Python backend
•	Uses OpenRouter + models like gpt-4o
•	Filters goal-only and ambiguous logic before calling the model
•	Extracts structured sections from output: Reasoning, Code, Edge Cases
________________________________________
🔧 Setup
1.	Clone the repo:
git clone https://github.com/yourusername/buddycode.git
2.	Add your API key:
# config.py
API_KEY = "your-openrouter-api-key"
MODEL = "openai/gpt-4o"
3.	Install dependencies:
pip install -r requirements.txt
4.	Test it:
from backend.model_api import generate_code
print(generate_code("Filter scores > 70, then average and round to 2 decimals"))
________________________________________
📁 Project Structure
buddycode/
├── backend/
│   └── model_api.py     # Core interpreter
├── config.py            # API key & model
├── app.py               # Optional FastAPI UI
├── requirements.txt
└── README.md
________________________________________
📚 License
MIT License. Free for personal and commercial use.
Just don’t make it guess.
________________________________________
👨‍💻 Built By
@blackhole — B.Tech ECE student, drone designer, system builder.
"Jack of all trades, master of one."
Project Philosophy: Think like a compiler. Code like a mirror.

├── backend/
│   └── model_api.py     # Core interpreter
├── config.py            # API key & model
├── app.py               # Optional FastAPI UI
├── requirements.txt
└── README.md
________________________________________
📚 License
MIT License. Free for personal and commercial use.
Just don’t make it guess.
________________________________________
👨‍💻 Built By
@blackhole — B.Tech ECE student, drone designer, system builder.
"Jack of all trades, master of one."
Project Philosophy: Think like a compiler. Code like a mirror.

