def get_todos(filepath='todos.txt'):
    """ This is the help for get_todos """


    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    print(todos_local)
    return todos_local

def write_todos(todos_arg,filepath='todos.txt'):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("lib executed")