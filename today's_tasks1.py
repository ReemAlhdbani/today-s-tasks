

# Get tasks from the user, separated by commas
your_task = input("Enter your tasks for today, separated by commas: ").split(", ")

# Create lists to store done and ongoing tasks
Done_tasks = []
Ongoing_tasks = []

# Loop through each task
for task in your_task:
    # Ask the user if they finished the task
    qus_tasks = input(f"Did you finish the {task} yet? (yes/no): ")
    # Check if the user finished the task
    if qus_tasks.lower() == 'yes':
        print("Great Job!")
        # Add the task to the Done_tasks list
        Done_tasks.append(task)
    else:
        print("Try not to put it off.")
        # Add the task to the Ongoing_tasks list
        Ongoing_tasks.append(task)
    print("_"*7)  # Print a separator line

# Ask the user if they want to see their progress
prograc = input("Do you want to see your today's progress (yes/no): ")
# Check if the user wants to see their progress
if prograc.lower() == "yes":  # Use lowercase for case-insensitive comparison
    print(f"""            *** Done Tasks ****
     {Done_tasks}  \n
                  *** Ongoing Tasks ***
                       {Ongoing_tasks} 
                  """)
else:
    print("Try again")