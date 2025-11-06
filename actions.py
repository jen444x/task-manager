# create new task
def add_task(tasks, task):
    """ Add task to set of tasks """

    # Create new task dict
    new_task = {'name': task, 'name_lower': task.lower()}

    # Add dict to list
    tasks.append(new_task)

    return True

# Find task
def lookup(tasks, task):
    """ Find Task """
    # check it exists and save map
    task_lowered = task.lower()
    for curr_task in tasks:       
        if curr_task['name_lower'] == task_lowered:
            return curr_task

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

# edit task
def edit_task(tasks, task):
    """ Edit task """
    
    # check it exists and save dict
    target_task = lookup(tasks, task)

    if not target_task:
        return False
    
    # Get new task name
    new_task_name = input("\nPlease enter new task name: ")
    
    # Edit data
    target_task['name'] = new_task_name
    target_task['name_lower'] = new_task_name.lower()

    return True

# print tasks
def show_tasks(tasks):
    """ Show all tasks """

    print("\nCurrent tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task['name']}")
