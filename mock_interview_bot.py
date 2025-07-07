# file: mock_interview_bot.py

import ollama

# Interview questions bank
QUESTIONS = [
    "Tell me about yourself.",
    "What are your strengths and weaknesses?",
    "Why should we hire you?",
    "Describe a challenging project you worked on.",
    "Where do you see yourself in 5 years?",
]

# Call Ollama with LLaMA2 to evaluate the answer
def evaluate_answer(question: str, answer: str) -> str:
    prompt = f"""
You are a senior technical interviewer. Evaluate the following answer from a job candidate.

Question: {question}
Answer: {answer}

Give constructive feedback and a follow-up question.
"""
    response = ollama.chat(model='llama2', messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# Save Q&A + feedback to a file
def save_to_file(question: str, answer: str, feedback: str):
    with open("interview_log.txt", "a", encoding="utf-8") as f:
        f.write("\nQ: " + question + "\n")
        f.write("A: " + answer + "\n")
        f.write("📝 Feedback:\n" + feedback + "\n")
        f.write("""----------------------------------------\n""")


def run_mock_interview():
    print("\n📢 Welcome to Mock Interview AI (powered by LLaMA2)")
    print("Type your answer and press Enter. Type 'exit' to quit.\n")

    for question in QUESTIONS:
        print(f"\n💬 Interviewer: {question}")
        user_input = input("🧑 You: ")

        if user_input.strip().lower() == 'exit':
            print("👋 Exiting interview.")
            break

        print("\n🤖 Thinking...\n")
        feedback = evaluate_answer(question, user_input)
        print(f"📝 Feedback:\n{feedback}")

        # Save result
        save_to_file(question, user_input, feedback)


if __name__ == '__main__':
    run_mock_interview()
