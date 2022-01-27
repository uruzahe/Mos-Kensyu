from src.classes.question_mode import QuestionModeHandler
from src.classes.character_mode import CharacterModeHandler
from src.classes.answer_mode import AnswerModeHandler


class Akinator:
    def __init__(self):
        self.question_mode = QuestionModeHandler()
        self.character_mode = CharacterModeHandler()
        self.answer_mode = AnswerModeHandler()

    def run(self):
        self.answer_mode.run()

    def character(self):
        self.character_mode.mode_select()

    def question(self):
        self.question_mode.mode_select()

    def answer(self):
        self.answer_mode.mode_select()
