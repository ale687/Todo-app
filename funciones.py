FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Leer in archivo de texto y devolver la lista de
    tareas pendientes.
    """
    with open(filepath,"r") as file_local:
            todos_local = file_local.readlines()
    return todos_local
 
 
def write_todos(todos_arg , filepath=FILEPATH):
    """ Escribe en la lista de tareas pendientes en el archivo de texto."""
    with open(filepath, "w") as file:
            file.writelines(todos_arg)
 
 
if __name__ == "__main__":
    print("Hello fron funciones")
    print(get_todos())
     