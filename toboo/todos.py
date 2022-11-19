from datetime import datetime
from .console import console


class Todo:
    def __init__(self, title, due):
        self.title = title
        self.due = due

    def is_late(self):
        return datetime.now() > self.due

    def to_json(self):
        return [self.title, self.due.timestamp()]

    @classmethod
    def from_json(cls, json):
        return cls(json[0], datetime.fromtimestamp(json[1]))

    def __repr__(self):
        return f"Todo('{self.title}', due={self.due})"


class TodosManager:
    def __init__(self):
        self.todos = []

    def add_todo(self):
        title = console.input("What is the todo's title?")
        due = self.input_date()
        todo = Todo(title, due)
        self.todos.append(todo)
        return todo

    def remove(self, todo):
        self.todos.remove(todo)

    def input_date(self):
        while True:
            try:
                date = datetime.strptime(
                    console.input(
                        "When is this todo due? [mm/dd/yyyy hh(24-time):mm] "
                    ),
                    "%m/%d/%Y %H:%M",
                )
                return date
            except KeyboardInterrupt:
                quit()
            except Exception:
                print("Bad datetime format, please try again or Ctrl-C to quit.")

    def to_json(self):
        return [t.to_json() for t in self.todos]

    @classmethod
    def from_json(cls, json):
        todos_manager = cls()
        todos_manager.todos = [Todo.from_json(t) for t in json]
        return todos_manager

    def __repr__(self):
        return repr(self.todos)
