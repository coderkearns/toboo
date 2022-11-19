from .store import store
from .console import console


def main():
    do_updates()
    store.pet.show()

    console.do(
        "What do you want to do?",
        ["List todos", do_list_todos],
        ["Add a todo item", do_add_todo],
        ["Complete a todo item", do_complete_todo],
    )

    store.save()


def do_updates():
    for todo in store.todos.todos:
        if todo.is_late():
            store.todos.remove(todo)
            store.pet.miss_task()


def do_list_todos():
    for todo in store.todos.todos:
        print(todo)


def do_add_todo():
    todo = store.todos.add_todo()
    print(f"{todo} added!")


def do_complete_todo():
    todo = console.ask("What todo did you complete?", store.todos.todos)
    store.todos.remove(todo)
    store.pet.complete_task()
    print(f"Todo {todo} completed!")


if __name__ == "__main__":
    main()
