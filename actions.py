from task import Task

# create new task
def add_task(tasks, task):
    """ Add task to set of tasks """

    # Make description optional
    user_input = input("\nWould you like to enter a description as well (y/n): ").lower().strip()
    if user_input == 'y':
        description = input("\nPlease enter description: ")
    elif user_input == 'n':
        description = ""
    else:
        print("\nInvalid input.", end="")
        return False
    
    # Create a new task object
    new_task = Task(task, description)

    # Add object to list
    tasks.append(new_task)

    return True

# Find task
def lookup(tasks, task):
    """ Find Task """
    # check it exists and save map
    task_lowered = task.lower()
    for task_instance in tasks:       
        if task_instance.name_lowered == task_lowered:
            return task_instance

    return None

# delete task
def delete_task(tasks, task):
    """ Delete task """

    # check it exists and save dict
    target_task = lookup(tasks, task)

    if not target_task:
        return False
    
    # Remove if it was found
    tasks.remove(target_task)   
    return True 

# edit name
def edit_name(task):
    """Edit task name"""
    old_name = task.name
    # Get new task name
    new_task_name = input("\nPlease enter new task name: ")
    
    # Edit data
    task.name = new_task_name
    task.name_lowered = new_task_name.lower()  

    # notify user
    print(f"\nTask name was changed from '{old_name}' to {new_task_name}.")  

# edit description
def edit_description(task):
    """Edit task description"""
    old_description = task.description
    # Get new task description
    new_description = input("\nPlease enter new task description: ")
    
    # Edit data
    task.description = new_description 

    # notify user
    print(f"\nTask description was changed from '{old_description}' to {new_description}.")  

# edit task
def edit_task(tasks, task):
    """ Edit task """
    # See what they want to edit
    attribute_to_edit = input("\nPlease chose what you would like to edit:\n\n" \
    "a - Name\n" \
    "b - Description\n" \
    "c - Both\n\n" \
    "d - Return\n\n" \
        ).lower().strip()

    if attribute_to_edit == "d":
        return False
    
    # check it exists, if not notify user
    target_task = lookup(tasks, task)
    if not target_task:
        print("\nTask was not found.")
        return False
    
    # if it does exist, ask user what to edit
    if attribute_to_edit == "a":
        edit_name(target_task)
    elif attribute_to_edit == "b":
        edit_description(target_task)
    elif attribute_to_edit == "c":
        edit_name(target_task)
        edit_description(target_task)

    return True

# print tasks
def show_tasks(tasks):
    """ Show all tasks """

    print("\nCurrent tasks:")
    for i, task in enumerate(tasks):
        # doesnt go to newline for formatting
        print(f"{i+1}. {task.name}", end="")
        if task.description:
            print(f" - {task.description}")
        else:
            # new line
            print("\n")
