from todo import Todo
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

