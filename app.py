# todos = []

while True:
    todo = input("Enter 'add', 'complete', 'show', 'edit' or 'exit': ")
    todo = todo.strip().lower()

    match todo:
        case "add":
            todo = input("Enter a to-do: ") + "\n"
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)
            
            with open("files/todos.txt", "w") as file:
                file.writelines(todos)
        case "show":
            print("To-do list:")
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()
            for i, todo in enumerate(todos):
                print(f"{i+1}: {todo.strip().title()}")
        case "edit":
            index = int(input("Enter the number of the to-do item you want to edit: "))
            todo = input("Enter the new to-do: ")
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()
            todos[index-1] = todo + "\n"
            with open("files/todos.txt", "w") as file:
                file.writelines(todos)
        case "complete":
            index = int(input("Enter the number of the to-do item you want to complete: "))
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()
            todo_to_complete = todos[index-1]   
            todos.pop(index-1)
            with open("files/todos.txt", "w") as file:
                file.writelines(todos)
            print(f"Completed: {todo_to_complete.strip().title()}")
        case "exit":
            print("Goodbye!")
            break
        case _:
            print("Invalid input")








