from pathlib import Path
import json

from .pet import Pet
from .todos import TodosManager

_dirname = Path(__file__).parent
store_file = _dirname.joinpath("store.json")


class Store:
    def __init__(self):
        self.pet = Pet("?", "?")
        self.todos = TodosManager()

    def to_json(self):
        return {"pet": self.pet.to_json(), "todos": self.todos.to_json()}

    @classmethod
    def from_json(cls, json):
        store = cls()
        store.pet = Pet.from_json(json["pet"])
        store.todos = TodosManager.from_json(json["todos"])

        return store

    def save(self):
        store = self.to_json()
        store_file.write_text(json.dumps(store, indent=4))

    def __repr__(self):
        return repr(self.__dict__)


store = Store.from_json(json.loads(store_file.read_text()))
