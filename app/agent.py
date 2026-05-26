import json
from openai import OpenAI
from dotenv import load_dotenv

from app.config import MODEL, DEBUG

from app.prompts import SYSTEM_PROMPT
from app.tools import TOOLS, calculator, get_current_time, add_time
from app.memory import (
    load_memory,
    save_memory,
    reset_memory
)

load_dotenv()

class StatefulAgent:
    def __init__(self):
        self.client = OpenAI()
        self.messages = load_memory()

    def _execute_tool_call(self, tool_call) -> str:
        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        if DEBUG:
            print(f"[DEBUG] Tool requested: {tool_name}")
            print(f"[DEBUG] Tool arguments: {arguments}")

        if tool_name == "calculator":
            result = calculator(arguments["expression"])
        elif tool_name == "get_current_time":
            result = get_current_time()
        elif tool_name == "add_time":
            result = add_time(
                base_iso=arguments["base_iso"],
                days=arguments.get("days", 0),
                hours=arguments.get("hours", 0),
                minutes=arguments.get("minutes", 0),
                seconds=arguments.get("seconds", 0),
            )
        else:
            result = f"Unknown tool: {tool_name}"

        if DEBUG:
            print(f"[DEBUG] Tool result: {result}")

        return result

    def _looks_like_math(self, text: str) -> bool:
        math_keywords = ["sqrt", "power", "plus", "minus", "times", "divided", "multiply", "add", "subtract"]
        math_symbols = ["+", "-", "*", "/", "^", "(", ")"]

        text_lower = text.lower()

        has_digit = any(char.isdigit() for char in text)
        has_math_keyword = any(keyword in text_lower for keyword in math_keywords)
        has_math_symbol = any(symbol in text for symbol in math_symbols)

        return has_digit and (has_math_keyword or has_math_symbol)

    def _looks_like_time_request(self, text: str) -> bool:
        text_lower = text.lower()
        time_keywords = [
            "what time",
            "current time",
            "today",
            "current date",
            "date today",
            "what date",
        ]
        return any(keyword in text_lower for keyword in time_keywords)

    def chat(self, user_input: str) -> str:
        self.messages.append({"role": "user", "content": user_input})
        save_memory(self.messages)

        tool_choice = "auto"

        if self._looks_like_math(user_input):
            tool_choice = {
                "type": "function",
                "function": {"name": "calculator"}
            }
        elif self._looks_like_time_request(user_input):
            tool_choice = {
                "type": "function",
                "function": {"name": "get_current_time"}
            }

        response = self.client.chat.completions.create(
            model=MODEL,
            messages=self.messages,
            tools=TOOLS,
            tool_choice=tool_choice,
        )

        message = response.choices[0].message
        self.messages.append(message.model_dump())
        save_memory(self.messages)

        max_tool_rounds = 5
        tool_round = 0

        while message.tool_calls and tool_round < max_tool_rounds:
            tool_round += 1

            for tool_call in message.tool_calls:
                tool_result = self._execute_tool_call(tool_call)

                self.messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": tool_result
                    }
                )
                save_memory(self.messages)

            response = self.client.chat.completions.create(
                model=MODEL,
                messages=self.messages,
                tools=TOOLS,
                tool_choice="auto",
            )

            message = response.choices[0].message
            self.messages.append(message.model_dump())
            save_memory(self.messages)

        if message.tool_calls:
            return "Error: Tool loop limit reached"

        return message.content or ""

    def reset(self) -> None:
        self.messages = reset_memory()