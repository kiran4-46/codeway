import os

# Guidelines for users to use this todos application

'''("please follow below instructions to use the todo application features
1.  Enter (1) for  Display todo list
2.  Enter (2) for  add task in todo list
3.  Enter (3) for  Delete task from todo list
4.  Enter (4) for  Exit from todo list changes'''

def displayTodo(todos):
    print("TODO List:")
    for index, todo in enumerate(todos, start=1):
        print(f"{index}. {todo}")

def addTask(todos, new_todo):
    todos.append(new_todo);
    print("task successfully added")

def deleteTask(todos, index):
    if (1 <= index <= len(todos)):
        deleted_todo = todos.pop(index -1)
        print("the below specified taks is successfully deleted:")
        print(f"{index}. {deleted_todo}")
    
    else:
        print("please enter valid index")
def exit():
    print("You successfully existed from the making changes of todos application")


def main():
    todos =[]
    while True:
        print("Todo List");
        print("please follow below instructions to use the todo application features")
        print("1.  Enter (1) for  Display todo list");
        print("2.  Enter (2) for  add task in todo list");
        print("3.  Enter (3) for  Delete task from todo list");
        print("4.  Enter (4) for  Exit from todo list changes");
       
        user_response = input("Please Enter task here (number between 1-4): ")
        if(user_response == "1" ):
            displayTodo(todos)
        elif (user_response == "2"):
            new_todo = input("Enter what do you want to do ? ")
            addTask(todos, new_todo)
            
        elif (user_response == "3"):
            index = int(input("please enter the index of the, you want to delete!"))
            deleteTask(todos, index)
        elif(user_response == "4"):
            exit();
            break
        else:
            print("please choose right choice , enter a  number between 1 to 4")

if __name__ == "__main__":
    main();
__name__ == "__main__"
