task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            reminder = f"'{task}' is a high priority task that requires immediate attention today!"
        else:
            reminder = f"'{task}' is a high priority task. Consider completing it when you have the free time."
    
    case "medium":
        if time_bound == "yes":
           reminder = f"'{task}' is a medium priority task that requires attention today."
        else:
            reminder = f"'{task}' is a medium priority task. Consider completing it when you have the free time."
    case "low":
        if time_bound == "yes":
            reminder = f"'{task}' is a low priority task that requires attention today."
        else:
            reminder = f"'{task}' is a low priority task. Consider completing it when you have the free time."
    case _:
        reminder = "Invalid priority level entered. Please try again."
    
print()