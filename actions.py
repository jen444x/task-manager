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
    
    # Make due date optional
    user_input = input("\nWould you like to enter a due date as well (y/n): ").lower().strip()
    if user_input == 'y':
        due_date = input("\nPlease enter due date: ")
        #####
        # Make sure due date is valid  #
        ####
    elif user_input == 'n':
        due_date = ""
    else:
        print("\nInvalid input.", end="")
        return False
    
    # Create a new task object
    new_task = Task(task, description, due_date)

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
    print(f"\nTask name was changed from '{old_name}' to '{new_task_name}'.")  

# edit description
def edit_description(task):
    """Edit task description"""
    old_description = task.description
    # Get new task description
    new_description = input("\nPlease enter new task description: ")
    
    # Edit data
    task.description = new_description 

    # notify user
    print(f"\nTask description was changed from '{old_description}' to '{new_description}'.")  

# edit due date
def edit_due_date(task):
    """Edit task due_date"""
    old_due_date = task.due_date
    # Get new task due date
    new_due_date = input("\nPlease enter new task due date: ")
    
    # Edit data
    task.due_date = new_due_date 

    # notify user
    print(f"\nTask due date was changed from '{old_due_date}' to '{new_due_date}'.")  

# edit task
def edit_task(tasks, task):
    """ Edit task """
    # See what they want to edit
    attribute_to_edit = input("\nPlease chose what you would like to edit:\n\n" \
    "a - Name\n" \
    "b - Description\n" \
    "c - Due date\n\n" \
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
        edit_due_date(target_task)

    return True

# print tasks
def show_tasks(tasks):
    """ Show all tasks """

    print("\nCurrent tasks:")
    for i, task in enumerate(tasks):
        # print name
        print(f"{i+1}. {task.name}", end="")
        
        # print description if any
        if task.description:
            print(f" - {task.description}")
        # if no description was added
        else:
            # if due date was added 
            if task.due_date:
                # new line to format 
                print()
            # if due date was not added
            else:
                # we dont need to check the rest
                print()
                continue

        # if we go to this point, print due date
        print(f"   Due: {task.due_date}")