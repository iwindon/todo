todos = []
prompt = "Enter a to-do item ('exit' to quit): "

while True:
    todo = input(prompt)
    todos.append(todo)
    if todo == "exit":
        break

    print("To-do list:")
    for i, todo in enumerate(todos):
        print(f"{i+1}: {todo.title()}")
