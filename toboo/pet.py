from .pets import pets


class Pet:
    def __init__(self, name, pet):
        self.name = name
        self.pet = pet

        self.exp = 0
        self.hp = 10
        self.max_hp = 10
        self.mp = 1

    def complete_task(self):
        self.exp += self.mp
        # TODO: If all tasks done, heal 10%
        # TODO: evolution

    def miss_task(self):
        self.hp -= 1
        self.mp = 0

        # TODO: die if no hp

    @property
    def mood(self):
        if self.mp < 3 and self.hp < (self.max_hp / 2):
            return "sad"
        elif (self.mp > 3 and self.hp < (self.max_hp / 2)) or (
            self.mp < 2 and self.hp > (self.max_hp / 2)
        ):
            return "neutral"
        else:
            return "happy"

    def show(self):
        face = pets[self.pet]["faces"][self.mood]

        print(f"EXP: {self.exp:>15}")
        hp_str = f"{self.hp}/{self.max_hp}"
        print(f"HP: {hp_str:>16}")
        print(f"MP: {self.mp:>16}")
        print(face)

    def to_json(self):
        return {
            "name": self.name,
            "pet": self.pet,
            "exp": self.exp,
            "hp": self.hp,
            "max_hp": self.max_hp,
            "mp": self.mp,
        }

    @classmethod
    def from_json(cls, json):
        pet = cls(json["name"], json["pet"])
        pet.exp = json["exp"]
        pet.hp = json["hp"]
        pet.max_hp = json["max_hp"]
        pet.mp = json["mp"]
        return pet

    def __repr__(self):
        return f"Pet('{self.name}', '{self.pet}', exp={self.exp}, hp={self.hp}, max_hp={self.max_hp}, mp={self.mp}, mood='{self.mood}')"
