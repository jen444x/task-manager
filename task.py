from date import is_valid_date

class Task:
    """ Models a single task"""

    def __init__(self, name, description="", due_date=""):
        self.name = name
        self.name_lowered = name.lower()
        self.description = description
        self.due_date = due_date

    def get_dict(self):
        return self.__dict__
    
    # edit name
    def edit_name(self):
        """Edit task name"""
        old_name = self.name
        # Get new task name
        new_task_name = input("\nPlease enter new task name: ")
        
        # Edit data
        self.name = new_task_name
        self.name_lowered = new_task_name.lower()  

        # notify user
        print(f"\nTask name was changed from '{old_name}' to '{new_task_name}'.")  

    # edit description
    def edit_description(self):
        """Edit task description"""

        old_description = self.description
        # Get new task description
        new_description = input("\nPlease enter new task description: ")
        
        # Edit data
        self.description = new_description 

        # notify user
        print(f"\nTask description was changed from '{old_description}' to '{new_description}'.")  

    
    def edit_due_date(self):
        """Edit task due_date"""

        old_due_date = self.due_date

        new_due_date = input("Please enter new due date (MM/DD/YYYY): ")

        valid_date = is_valid_date(new_due_date)

        while not valid_date:
            new_due_date = input("Due date was invalid. " \
            "Make sure to use the following format MM/DD/YY: ")

            valid_date = is_valid_date(new_due_date)
        
        # Edit data
        self.due_date = new_due_date 

        # notify user
        print(f"\nTask due date was changed from '{old_due_date}' to '{new_due_date}'.")  

