import json
from pathlib import Path
from typing import Any

from app.prompts import SYSTEM_PROMPT

MEMORY_PATH = Path("data/conversation_memory.json")
MAX_HISTORY_MESSAGES = 20

def default_memory() -> list[dict[str, Any]]:
    return [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

def load_memory() -> list[dict[str, Any]]:
    if not MEMORY_PATH.exists():
        return default_memory()

    try:
        with open(MEMORY_PATH, "r", encoding="utf-8") as file:
            messages = json.load(file)

        if not isinstance(messages, list):
            return default_memory()

        if not messages or messages[0].get("role") != "system":
            return default_memory()

        return messages
    
    except Exception:
        return default_memory()

def save_memory(messages: list[dict[str, Any]]) -> None:
    MEMORY_PATH.parent.mkdir(parents=True, exist_ok=True)

    limited_messages = apply_memory_limit(messages)

    with open(MEMORY_PATH, "w", encoding="utf-8") as file:
        json.dump(limited_messages, file, indent=2, ensure_ascii=False)

def reset_memory() -> list[dict[str, Any]]:
    messages = default_memory()
    save_memory(messages)
    return messages

def apply_memory_limit(messages: list[dict[str, Any]]) -> list[dict[str, Any]]:
    if not messages:
        return default_memory()

    system_message = messages[0]
    history = messages[1:]

    if len(history) <= MAX_HISTORY_MESSAGES:
        return messages

    return [system_message] + history[-MAX_HISTORY_MESSAGES:]