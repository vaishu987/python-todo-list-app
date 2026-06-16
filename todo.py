# To-Do List Application

tasks = []

while True:
    print("\n" + "=" * 35)
    print("        TO-DO LIST APP")
    print("=" * 35)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        description = input("Enter task description: ")

        task = {
            "description": description,
            "completed": False
        }

        tasks.append(task)
        print("✅ Task added successfully!")

    elif choice == "2":

        if not tasks:
            print("No tasks available.")

        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{index}. {task['description']} - {status}")

    elif choice == "3":

        if not tasks:
            print("No tasks available.")

        else:
            print("\nTasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task['description']}")

            try:
                task_num = int(input("Enter task number: "))

                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]["completed"] = True
                    print("✅ Task marked as completed!")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Thank you for using To-Do List App.")
        break

    else:
        print("Invalid choice. Please try again.")