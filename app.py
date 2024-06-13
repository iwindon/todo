todos = []

while True:
    todo = input("Enter 'add', 'show', 'edit' or 'exit': ")
    todo = todo.strip().lower()

    match todo:
        case "add":
            todo = input("Enter a to-do: ")       
            todos.append(todo)
        case "show":
            print("To-do list:")
            for i, todo in enumerate(todos):
                print(f"{i+1}: {todo.title()}")
        case "edit":
            index = int(input("Enter the number of the to-do item you want to edit: "))
            todo = input("Enter the new to-do: ")
            todos[index-1] = todo
        case "exit":
            print("Goodbye!")
            break
        case _:
            print("Invalid input")





