FILENAME = "tasks.txt"


def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")


def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


tasks = load_tasks()

while True:
    print("\n1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Quit")
    choice = input("Choose: ").strip()

    if choice == "1":
        show_tasks(tasks)
    elif choice == "2":
        new_task = input("New task: ").strip()
        if new_task:
            tasks.append(new_task)
            save_tasks(tasks)
            print("Added.")
    elif choice == "3":
        show_tasks(tasks)
        try:
            number = int(input("Number to remove: "))
            removed = tasks.pop(number - 1)
            save_tasks(tasks)
            print(f"Removed: {removed}")
        except (ValueError, IndexError):
            print("Invalid number.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Please choose 1, 2, 3, or 4.")
df5
