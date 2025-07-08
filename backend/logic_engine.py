# backend/logic_engine.py

import re

# Keywords that indicate actual logical steps
LOGIC_KEYWORDS = [
    "if", "check", "compare", "store", "loop", "repeat", "count",
    "calculate", "print", "return", "ask", "input", "validate", "sort",
    "reverse", "remove", "append", "multiply", "divide"
]

def validate_logic(text):
    """
    Checks if the user's logic contains clear, actionable operations.
    This is a soft validation — not full NLP.
    """

    # Check if text is too short
    if len(text.strip().split()) < 5:
        return False

    # Check for keywords that suggest logic is actually described
    keyword_hits = sum(1 for word in LOGIC_KEYWORDS if word in text.lower())

    if keyword_hits >= 2:
        return True

    # If user is vague like "do something cool"
    vague_patterns = [
        r"\b(something|anything|stuff|thing)\b",
        r"\b(cool|awesome|nice|random|some logic)\b",
        r"\b(make|build|create)\b.*\b(something|anything)?\b"
    ]

    for pattern in vague_patterns:
        if re.search(pattern, text.lower()):
            return False

    return False  # Default to rejection if unsure
