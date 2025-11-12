from task import Task
from db import get_tasks, store_tasks
from date import tasks_due_on, get_date_obj

class TaskManager:
    """ Models task manager """

    def __init__(self, tasks_file):
        """ Initializes list and adds stored tasks """

        # List to hold order
        self.tasks_list = []
        # Dictionary for fast lookup
        self.tasks_dict = {}

        # Add stored tasks in list and dict, if any
        get_tasks(self.tasks_list, self.tasks_dict, tasks_file)

    def add_task(self, name, description="", due_date=""):
        """ Create new task instance """
        # Turn date into date obj if it's a str
        if due_date and type(due_date) == str:
            # Turn into date object
            due_date = get_date_obj(due_date)

        # Create a new task object
        new_task = Task(name, description, due_date)

        # Add object to list and dict
        self.tasks_list.append(new_task)
        self.tasks_dict[name.lower().strip()] = new_task

    def get_all_task_dicts(self):
        dict_list = []
        for task in self.tasks_list:
            dict_list.append(task.get_dict())

        return dict_list
    
    # Find task
    def lookup(self, task):
        """ Find Task """

        # Find reference with dictionary
        return self.tasks_dict[task.lower().strip()]

    def edit_task_name(self, target_task, new_task_name):
        """ Update task name"""
        original_name = target_task.name

        target_task.edit_name(new_task_name)

        # Create new key val pair with updated name
        self.tasks_dict[new_task_name] = target_task

        # delete old one
        del self.tasks_dict[original_name]

    def edit_task_description(self, target_task, new_task_desc):
        """ Update task name"""
        target_task.edit_description(new_task_desc)

    def edit_task_due_date(self, target_task, new_task_date):
        """ Update task name"""
        # Turn date into date obj if it's a str
        if type(new_task_date) == str:
            # Turn into date object
            new_task_date = get_date_obj(new_task_date)

        target_task.edit_due_date(new_task_date)
        
    def show_task(self, task):
        """ Show one task """
        # Print data
        print(f"\nName: {task.name}")
        if task.description:
            print(f"Description: {task.description}")
        if task.due_date:
            print(f"Due date: {task.due_date}")
    
    def show_tasks(self, tasks):
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

            if task.due_date:
                print(f"   Due: {task.due_date}")

    def show_all_tasks(self):
        """ Shows all tasks """

        self.show_tasks(self.tasks_list)

    def show_tasks_on_date(self, date):
        """ Show tasks based on date """

        if date == 'today':
            tasks = tasks_due_on(self.tasks_list, date)
        elif date == 'overdue':
            tasks = tasks_due_on(self.tasks_list, date)
        elif date == 'future':
            tasks = tasks_due_on(self.tasks_list, date)

        # Print tasks
        self.show_tasks(tasks)


    def delete_task(self, t_name):
        """ Delete task """

        # check it exists and save dict
        try:
            target_task = self.lookup(t_name)
        except KeyError:
            print("\nTask was not found.")
            return 
        
        # Remove from list and map
        self.tasks_list.remove(target_task)  
        del self.tasks_dict[t_name.lower().strip()]

        print(f"\nTask '{t_name}' was successfully deleted.")

    def save_data(self):
        """ Saves data in file """
        
        store_tasks(self.tasks_list)