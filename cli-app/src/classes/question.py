from src.classes.handler_base import HandlerBase
from src.utils import csv2dict_list

class Question:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class QuestionHandler(HandlerBase):
    FILE_PATH = "./src/data/questions.pickle"
    CSV_FILE_PATH = "./src/data/questions.csv"

    def __init__(self):
        super().__init__(
            QuestionHandler.FILE_PATH,
            QuestionHandler.CSV_FILE_PATH,
        )


    def add(self, name):
        super().add_data(Question(self.unique_id(), name))


    def csv_patch(self):
        super().update_data([Question(**d) for d in csv2dict_list(QuestionHandler.CSV_FILE_PATH)])
