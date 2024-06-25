"""
Module to display the current date and time as well as to add, 
complete, show, edit and exit to-do list.
"""
import time
import functions

FILEPATH = "files/todos.txt"

print(time.strftime("%A, %B %d %Y %I:%M %p"))
print("To add a new to-do, type 'add' followed by the to-do.")
print("To complete a to-do, type 'complete' followed by the to-do number.")


while True:
    todo = input("Enter 'add', 'complete', 'show', 'edit' or 'exit': ")
    todo = todo.strip().lower()

    if todo.startswith("add"):
        todo = todo[4:]
        todos = functions.get_todos(FILEPATH)

        todos.append(todo + "\n")

        functions.write_todos(FILEPATH, todos)

    elif todo.startswith("show"):
        print("To-do list:")
        todos = functions.get_todos(FILEPATH)
        for i, todo in enumerate(todos):
            print(f"{i+1}: {todo.strip().title()}")
    elif todo.startswith("edit"):
        try:
            index = int(todo[5:])
            todo = input("Enter the new to-do: ")
            todos = functions.get_todos(FILEPATH)
            todos[index-1] = todo + "\n"
            functions.write_todos(FILEPATH, todos)
        except ValueError:
            print("Invalid input. Please enter the item number.  Please try again.")
            continue
        except IndexError:
            print("Invalid number. Please try again.")
            continue

    elif todo.startswith("complete"):
        try:
            index = int(todo[9:])
            todos = functions.get_todos(FILEPATH)
            todo_to_complete = todos[index-1]
            todos.pop(index-1)
            functions.write_todos(FILEPATH, todos)
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
