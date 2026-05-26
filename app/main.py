from app.agent import StatefulAgent

def main() -> None:
    agent = StatefulAgent()
    print("Stateful Conversational Agent ready. Type 'quit' or 'exit' to exit.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue
        
        if user_input.lower() in {"quit", "exit"}:
            print("\nGoodbye!")
            break
        
        if user_input.lower() == "reset":
            agent.reset()
            print("Memory reset.\n")
            continue

        reply = agent.chat(user_input)
        print(f"\nAgent: {reply}\n")
