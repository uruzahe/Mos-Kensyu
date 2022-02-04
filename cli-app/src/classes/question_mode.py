from src.classes.question import QuestionHandler
from src.classes.mode_base import ModeHandler

class QuestionModeHandler(ModeHandler):
    def __init__(self):
        super().__init__(QuestionHandler(), "質問更新モード")

    def mode_add(self):
        while True:
            print("\n----- 追加する質問を記入してください -----\n")
            name = input()

            print(f"{name} を追加しますか?(y/n)")
            ans = input()
            if ans == "y":
                self.data_handler.add(name)
                print(f"{name}: を追加しました!")

            else:
                print(f"{name}: の追加をキャンセルしました．")

            print("質問の追加を続けますか？(y/n)")
            ans = input()
            if ans == "y":
                continue

            else:
                break
