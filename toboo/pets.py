import json
from pathlib import Path

pets = {}

_dirname = Path(__file__).parent
pets_dir = _dirname.joinpath("pets")

for pet_path in pets_dir.iterdir():
    name = pet_path.stem
    pet_data = json.loads(pet_path.joinpath("pet.json").read_text())
    faces = {
        "sad": pet_path.joinpath("sad.txt").read_text(),
        "neutral": pet_path.joinpath("neutral.txt").read_text(),
        "happy": pet_path.joinpath("happy.txt").read_text(),
    }

    pets[name] = {"data": pet_data, "faces": faces}
