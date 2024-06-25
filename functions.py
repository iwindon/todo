def get_todos(filepath):
    """Reads the to-do list from a file and returns it as a list."""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(filepath, todos_arg):
    """Writes the to-do list to a file."""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)