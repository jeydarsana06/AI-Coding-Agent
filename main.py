from agent import ask_llm

print("=" * 45)
print("       AI CODING AGENT")
print("=" * 45)

print("Type 'exit' to quit.\n")

while True:

    user_input = input("\nYou: ").strip()

    if user_input.lower() in ["exit", "quit"]:
        print("Agent: Goodbye!")
        break

    if not user_input:
        continue

    print("\nAgent is working...")

    response = ask_llm(user_input)

    print("\nGemini:", response)
