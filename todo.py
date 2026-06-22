TASK_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("📌 No tasks available.")
        return

    print("\n----- TO-DO LIST -----")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def update_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_num = int(input("Enter task number to update: "))
        if 1 <= task_num <= len(tasks):
            new_task = input("Enter updated task: ")
            tasks[task_num - 1] = new_task
            save_tasks(tasks)
            print("✅ Task updated successfully!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"🗑️ Deleted task: {removed}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def complete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_num = int(input("Enter task number to mark completed: "))
        if 1 <= task_num <= len(tasks):
            if not tasks[task_num - 1].startswith("✔"):
                tasks[task_num - 1] = "✔ " + tasks[task_num - 1]
                save_tasks(tasks)
                print("✅ Task marked as completed!")
            else:
                print("⚠️ Task already completed.")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n")
        print("=" * 35)
        print("      TO-DO LIST APPLICATION")
        print("=" * 35)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Completed")
        print("6. Exit")
        print("=" * 35)

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            update_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            complete_task(tasks)

        elif choice == "6":
            print("👋 Thank you for using To-Do List Application!")
            break

        else:
            print("❌ Invalid choice! Please select between 1 and 6.")

if __name__ == "__main__":
    main()