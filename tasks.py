def add_task(tasks, title):

    title = title.strip()

    if not title:
        return False

    new_id = max(
        (task["id"] for task in tasks),
        default=0
    ) + 1

    tasks.append({
        "id": new_id,
        "title": title,
        "completed": False
    })

    return True


def complete_task(tasks, task_id):

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return True

    return False