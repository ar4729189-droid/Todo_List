import info
class Todo():
    def __init__(self):
        self.tasks = []
        self.completed_tasks = "tasks.txt"
        
    def add_task(self):
        new_task = input("Enter some task:")
        self.tasks.append(new_task)
        with open("Data_base.txt","a") as f:
            result = f.write(new_task + "\n")
            print("Data successfully saved")
            f.close
    def show_task(self):
        if (not self.tasks):
            print("your list is emptied")
        else:
            for i,task in enumerate(self.tasks):
                print(i + 1, task)
