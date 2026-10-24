
def ask_number(prompt):
    while True:
        text = input(prompt).strip()
        if text.lower() == "q":
            return None
        try:
            return float(text)
        except ValueError:
            print("Please type a valid number (or q to quit).")


while True:
    a = ask_number("\nFirst number: ")
    if a is None:
        print("Goodbye!")
        break

    op = input("Operation (+, -, *, /): ").strip()
    if op not in operations:
        print("Please choose +, -, * or /.")
        continue

    b = ask_number("Second number: ")
    if b is None:
        print("Goodbye!")
        break

    print("Result:", operations[op](a, b))
