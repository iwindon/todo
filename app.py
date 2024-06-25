print("Todo App")
print("To add a new to-do, type 'add' followed by the to-do.")
print("To complete a to-do, type 'complete' followed by the to-do number.")

def get_todos(filepath):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

while True:
    todo = input("Enter 'add', 'complete', 'show', 'edit' or 'exit': ")
    todo = todo.strip().lower()

    if todo.startswith("add"):
        todo = todo[4:]
        todos = get_todos("files/todos.txt")

        todos.append(todo + "\n")
        
        with open("files/todos.txt", "w") as file:
            file.writelines(todos)
    elif todo.startswith("show"):
        print("To-do list:")
        todos = get_todos("files/todos.txt")
        for i, todo in enumerate(todos):
            print(f"{i+1}: {todo.strip().title()}")
    elif todo.startswith("edit"):
        try:
            index = int(todo[5:])
            todo = input("Enter the new to-do: ")
            todos = get_todos("files/todos.txt")
            todos[index-1] = todo + "\n"
            with open("files/todos.txt", "w") as file:
                file.writelines(todos)
        except ValueError:
            print("Invalid input. Please enter the item number.  Please try again.")
            continue
        except IndexError:
            print("Invalid number. Please try again.")
            continue

    elif todo.startswith("complete"):
        try:
            index = int(todo[9:])
            todos = get_todos("files/todos.txt")
            todo_to_complete = todos[index-1]   
            todos.pop(index-1)
            with open("files/todos.txt", "w") as file:
                file.writelines(todos)
            print(f"Completed: {todo_to_complete.strip().title()}")
        except ValueError:
            print("Invalid input. Please enter the item number.  Please try again.")
            continue
        except IndexError:
            print("Invalid number. Please try again.")
            continue
        
    elif todo.startswith("exit"):
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please try again.")








