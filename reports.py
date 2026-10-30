def show_tasks(tasks):

    if not tasks:
        print("No tasks available.")
        return

    print("\nID    TASK                 STATUS")
    print("------------------------------------------")

    for task in tasks:

        status = (
            "Completed"
            if task["completed"]
            else "Pending"
        )

        print(
            f'{task["id"]:<5} '
            f'{task["title"]:<21} '
            f'{status}'
        )


def show_summary(tasks):

    total = len(tasks)

    completed = sum(
        1 for task in tasks if task["completed"]
    )

    pending = total - completed

    print("\n===== TASK SUMMARY =====")
    print("Total Tasks:", total)
    print("Completed:", completed)
    print("Pending:", pending)