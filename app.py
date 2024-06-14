print("Todo App")
print("To add a new to-do, type 'add' followed by the to-do.")
print("To complete a to-do, type 'complete' followed by the to-do number.")

while True:
    todo = input("Enter 'add', 'complete', 'show', 'edit' or 'exit': ")
    todo = todo.strip().lower()

    if "add" in todo:
        todo = todo[4:]
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)
        
        with open("files/todos.txt", "w") as file:
            file.writelines(todos)
    elif "show" in todo:
        print("To-do list:")
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()
        for i, todo in enumerate(todos):
            print(f"{i+1}: {todo.strip().title()}")
    elif "edit" in todo:
        index = int(todo[5:])
        todo = input("Enter the new to-do: ")
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()
        todos[index-1] = todo + "\n"
        with open("files/todos.txt", "w") as file:
            file.writelines(todos)
    elif "complete" in todo:
        index = int(todo[9:])
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()
        todo_to_complete = todos[index-1]   
        todos.pop(index-1)
        with open("files/todos.txt", "w") as file:
            file.writelines(todos)
        print(f"Completed: {todo_to_complete.strip().title()}")
    elif "exit" in todo:
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please try again.")








