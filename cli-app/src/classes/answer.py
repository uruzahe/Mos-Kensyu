from src.classes.handler_base import HandlerBase
from src.utils import csv2dict_list


class Answer:
    def __init__(self, id, question_id, character_id, answer):
        self.id = id
        self.question_id = question_id
        self.character_id = character_id
        self.answer = answer


class AnswerHandler(HandlerBase):
    FILE_PATH = "./src/data/answers.pickle"
    CSV_FILE_PATH = "./src/data/answers.csv"

    def __init__(self):
        super().__init__(
            AnswerHandler.FILE_PATH,
            AnswerHandler.CSV_FILE_PATH
        )


    def add(self, question_id, character_id, answer):
        super().add_data(Answer(self.unique_id(), question_id, character_id, answer))

    def csv_patch(self):
        super().update_data([Answer(**d) for d in csv2dict_list(AnswerHandler.CSV_FILE_PATH)])
