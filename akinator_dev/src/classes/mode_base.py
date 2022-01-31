class ModeHandler:
    def __init__(self, data_handler, mode_name):
        self.modes = {
            1: "add",
            2: "show",
            3: "csv_dump",
            4: "csv_patch",
            8: "delete_by_id",
            9: "finish"
        }
        self.mode_name = mode_name
        self.data_handler = data_handler


    def mode_select(self):
        while True:
            print(f"\n----- {self.mode_name} -----\n")
            print(f"モード一覧: {self.modes}")
            print(f"モード選択: ")

            try:
                mode = int(input())

            except Exception:
                print(f"Invalid input.")
                continue


            if mode == 1:
                self.mode_add()

            elif mode == 2:
                self.data_handler.show()

            elif mode == 3:
                self.data_handler.csv_dump()

            elif mode == 4:
                self.data_handler.csv_patch()

            elif mode == 8:
                print("----- 全データ -----")
                self.data_handler.show()

                print("\n消去するデータのIDを入力してください")
                id = input("ID: ")
                self.data_handler.delete_by_id(id)

            elif mode == 9:
                print(f"{self.mode_name} を抜けます．")
                break

            else:
                print(f"Invalid mode:  {mode}")
                continue


    def mode_add(self):
        raise Exception("Uninheritanced ...")
