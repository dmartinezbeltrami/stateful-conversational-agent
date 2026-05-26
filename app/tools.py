import json
import math
from datetime import datetime, timedelta

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Safely evaluate a mathematical expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Mathematical expression to evaluate"
                    }
                },
                "required": ["expression"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Get the current local date and time.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "add_time",
            "description": "Add a duration to a base ISO datetime.",
            "parameters": {
                "type": "object",
                "properties": {
                    "base_iso": {
                        "type": "string",
                        "description": "Base datetime in ISO format, for example 2026-05-23T00:00:20"
                    },
                    "days": {
                        "type": "integer",
                        "description": "Number of days to add"
                    },
                    "hours": {
                        "type": "integer",
                        "description": "Number of hours to add"
                    },
                    "minutes": {
                        "type": "integer",
                        "description": "Number of minutes to add"
                    },
                    "seconds": {
                        "type": "integer",
                        "description": "Number of seconds to add"
                    }
                },
                "required": ["base_iso"]
            }
        }
    }
]

def calculator(expression: str) -> str:
    allowed_names = {
        "sqrt": math.sqrt,
        "pow": pow,
        "abs": abs,
        "round": round,
    }

    try:
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return str(result)
    except Exception as e:
        return f"Calculator error: {e}"

def get_current_time() -> str:
    now = datetime.now()

    return json.dumps({
        "year": now.year,
        "month": now.month,
        "day": now.day,
        "hour": now.hour,
        "minute": now.minute,
        "second": now.second,
        "iso": now.isoformat(timespec="seconds")
    })

def add_time(base_iso: str, days: int = 0, hours: int = 0, minutes: int = 0, seconds: int = 0) -> str:
    try:
        base_time = datetime.fromisoformat(base_iso)

        result = base_time + timedelta(
            days=days,
            hours=hours,
            minutes=minutes,
            seconds=seconds
        )

        return json.dumps({
            "year": result.year,
            "month": result.month,
            "day": result.day,
            "hour": result.hour,
            "minute": result.minute,
            "second": result.second,
            "iso": result.isoformat(timespec="seconds")
        })
    except Exception as e:
        return f"add_time error: {e}"