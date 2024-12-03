# El proyecto tiene la finalidad de agregar tareas y verlas, trabajando con un sistema vista controlador

class TaskModel:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks


class TaskView:
    @staticmethod
    def display_tasks(tasks):
        print("\nLista de Tareas:")
        if not tasks:
            print("No hay tareas por mostrar.")
        else:
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")

    @staticmethod
    def show_message(message):
        print(message)


class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_new_task(self, task):
        if not task.strip():
            self.view.show_message("¡La tarea no puede estar vacía!")
        else:
            self.model.add_task(task)
            self.view.show_message("Tarea agregada exitosamente.")
            self.view.display_tasks(self.model.get_tasks())

    def list_tasks(self):
        self.view.display_tasks(self.model.get_tasks())


def main():
    model = TaskModel()
    view = TaskView()
    controller = TaskController(model, view)

    while True:
        print("\nGestor de Tareas")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            task = input("Ingrese la tarea: ")
            controller.add_new_task(task)
        elif option == "2":
            controller.list_tasks()
        elif option == "3":
            print("Nos vemos :)")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
