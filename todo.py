class Todo():
    def __init__(self):
        self.tasks = []
        self.completed_tasks = "tasks.txt"
        
    def add_task(self):
        new_task = input("Enter some task:")
        self.tasks.append(new_task)
    def show_task(self):
        if (not self.tasks):
            print("your list is emptied")
        else:
            for i,task in enumerate(self.tasks):
                print(i + 1, task)
my_todo = Todo()
while True:
    user_choice = input("Enter 1 to add_task,2 to show_task,3 to exit: ")
    if (user_choice == "1"):
        my_todo.add_task()
    elif(user_choice == "2"):
        my_todo.show_task()
    elif(user_choice == "3"):
        break
    else:
       print("print only 1,2,and 3:--")
    
                
        