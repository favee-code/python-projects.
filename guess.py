
questions = {
    "What is the capital of Nigeria?": "abuja",
    "How many days are in a week?": "7",
    "What is 9 x 6?": "54",
    "Which planet is closest to the sun?": "mercury",
}

score = 0

for question, answer in questions.items():
    reply = input(question + " ").lower().strip()

    if reply == answer:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong. The answer is {answer}.")

print(f"You scored {score} out of {len(questions)}.")
