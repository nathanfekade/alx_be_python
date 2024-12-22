task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case 'high':
        if time == "yes":
            print(f"Reminder: {task} is a high priority task that requires immdediate attention today!")
        else:
            print(f"Note: '{task}' is high priority task. Consier completing it when you have free time.")
    
    case 'medium':
        if time == "yes":
            print(f"Reminder: {task} is a medium priority task that requires immdediate attention today!")
        else:
            print(f"Note: '{task}' is medium priority task. Consier completing it when you have free time.")

    case 'low':
            if time == "yes":
                print(f"Reminder: {task} is a low priority task that requires immdediate attention today!")
            else:
                print(f"Note: '{task}' is low priority task. Consier completing it when you have free time.")
