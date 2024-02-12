def schedule_tasks(deadlines, profits):
    n = len(deadlines)
    tasks = list(zip(deadlines, profits, range(1, n + 1)))  # (deadline, profit, task_number)
    tasks.sort(key=lambda x: x[1], reverse=True)  # Sort tasks by profit in descending order

    schedule = [0] * n  # Initialize schedule array
    slot = [False] * n  # Initialize slot array to keep track of available slots

    for i in range(n):
        for j in range(min(n, tasks[i][0]) - 1, -1, -1):
            if not slot[j]:
                schedule[j] = tasks[i][2]  # Assign task number to the schedule
                slot[j] = True
                break

    return schedule


def main():
    try:
        n = int(input("Enter the number of tasks: "))
        deadlines = [int(input(f"Enter deadline for task {i + 1}: ")) for i in range(n)]
        profits = [int(input(f"Enter profit for task {i + 1}: ")) for i in range(n)]

        result = schedule_tasks(deadlines, profits)

        # Display only scheduled tasks
        print("\nScheduled tasks:")
        for i, task_number in enumerate(result):
            if task_number != 0:
                task_index = task_number - 1  # Adjusting to 0-based indexing
                print(f"Task {task_index + 1} (Deadline: {deadlines[task_index]}, Profit: {profits[task_index]})")

    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()
