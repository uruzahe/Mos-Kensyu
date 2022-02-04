from src.classes.handler_base import HandlerBase
from src.utils import (
    csv2dict_list,
    str_similarity,
)

class Character:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class CharacterHandler(HandlerBase):
    FILE_PATH = "./src/data/characters.pickle"
    CSV_FILE_PATH = "./src/data/characters.csv"

    def __init__(self):
        super().__init__(
            CharacterHandler.FILE_PATH,
            CharacterHandler.CSV_FILE_PATH
        )

    def add(self, name):
        super().add_data(Character(self.unique_id(), name))

    def csv_patch(self):
        super().update_data([Character(**d) for d in csv2dict_list(CharacterHandler.CSV_FILE_PATH)])

    def data_by_name(self, name):
        for d in self.all():
            if d.name == name:
                return d

        return None

    def name_exist(self, name):
        return (name in [d.name in d in self.all()])

    def similer_data_with_name(self, name, lowest_similarity = 0.5):
        return [d.name for d in self.all() if lowest_similarity <= str_similarity(name, d.name)]
