todos = []

while True:
    todo = input("Enter 'add' or 'show' or 'exit': ")

    if todo == "add":
        todo = input("Enter a to-do: ")       
        todos.append(todo)
    elif todo == "show":
        print("To-do list:")
        for i, todo in enumerate(todos):
            print(f"{i+1}: {todo.title()}")
    elif todo == "exit":
        break


