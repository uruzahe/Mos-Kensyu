# coding: utf-8

from src.classes.akinator import Akinator

MODES = {
    1: "run",
    2: "character",
    3: "question",
    4: "answer",
    9: "finish"
}
DESCRIPTION = 'This program is a program like Akinator.'

if __name__ ==  "__main__":
    engin = Akinator()

    while True:
        print(f"\n----- {DESCRIPTION} -----\n")
        print(f"Mode一覧: {MODES}")
        print(f"Mode選択: ")

        try:
            mode = int(input())

        except Exception:
            print(f"Invalid input")
            continue

        if mode == 1:
            engin.run()

        elif mode == 2:
            engin.character()

        elif mode == 3:
            engin.question()

        elif mode == 4:
            engin.answer()

        elif mode == 9:
            break

        else:
            print(f"Invalid mode: {mode}")
            continue
