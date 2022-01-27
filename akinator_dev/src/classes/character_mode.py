from src.classes.character import CharacterHandler
from src.classes.mode_base import ModeHandler

class CharacterModeHandler(ModeHandler):
    def __init__(self):
        super().__init__(CharacterHandler(), "キャラクター更新モード")

    def mode_add(self):
        while True:
            print("\n----- 追加するキャラクターの名前を記入してください -----\n")
            name = input()

            print(f"{name} を追加しますか?(y/n)")
            ans = input()
            if ans == "y":
                self.data_handler.add(name)
                print(f"{name}: を追加しました!")

            else:
                print(f"{name}: の追加をキャンセルしました．")

            print("キャラクターの追加を続けますか？(y/n)")
            ans = input()
            if ans == "y":
                continue

            else:
                break
