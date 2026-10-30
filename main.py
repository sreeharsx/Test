from storage import load_tasks, save_tasks
from tasks import add_task, complete_task
from reports import show_tasks, show_summary


def main():
    tasks = load_tasks()

    while True:
        print("\n===== TEAM TASK MANAGER =====")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Complete Task")
        print("4. View Summary")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter task: ")

            if add_task(tasks, title):
                save_tasks(tasks)
                print("Task added successfully!")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID: "))
                if complete_task(tasks, task_id):
                    save_tasks(tasks)
                    print("Task completed!")
                else:
                    print("Task not found.")
            except ValueError:
                print("Enter a valid ID.")

        elif choice == "4":
            show_summary(tasks)

        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()