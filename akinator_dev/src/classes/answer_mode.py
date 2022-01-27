import time
import src.aa as aa

from src.utils import (
    count_down,
    entropy,
)
from src.classes.answer import AnswerHandler
from src.classes.character import CharacterHandler
from src.classes.question import QuestionHandler
from src.classes.mode_base import ModeHandler


class SmapleAnswerModeHandler(ModeHandler):
    def __init__(self):
        super().__init__(AnswerHandler(), "回答更新モード")

        self.character_handler = CharacterHandler()
        self.question_handler = QuestionHandler()

    def predict_character(self, target_answers, state, previous_expeected_ids=[]):
        #  一番情報量が多い質問を選択することで大雑把に分類する．

        # 回答を集計
        question_id2ans = {}
        question_id2all_ans = {}
        for ans in target_answers:
            if ans.question_id not in question_id2ans.keys():
                question_id2ans[ans.question_id] = {}
                question_id2all_ans[ans.question_id] = 0

            if ans.answer not in question_id2ans[ans.question_id].keys():
                question_id2ans[ans.question_id][ans.answer] = 0

            question_id2ans[ans.question_id][ans.answer] += 1
            question_id2all_ans[ans.question_id] += 1

        # エントロピーが最大になる質問を探索
        max_entrpy = 0
        max_entrpy_question_id = None
        for question_id, ans in question_id2ans.items():
            if max_entrpy < entropy([ count / question_id2all_ans[question_id] for ans, count in ans.items()]):
                max_entrpy_question_id = question_id

            else:
                continue

        # 質問
        question = self.question_handler.find_by_id(max_entrpy_question_id)
        aa.random()
        print(f"Question: {question.name} (1: はい, 2: いいえ, 3: わからない)")

        # 回答を元にstateを更新
        user_answer = int(input())
        state.append({"question_id": question_id, "answer": user_answer})

        # 回答から質問の候補を絞っていく．
        expected_character_ids = list(set([ans.character_id for ans in target_answers if ans.question_id == max_entrpy_question_id and ans.answer == user_answer]))
        target_answers = [t_ans for t_ans in target_answers if t_ans.character_id in expected_character_ids]

        if len(expected_character_ids) == 1:
            return expected_character_ids[0], state

        elif 2 <= len(expected_character_ids):
            # ----- 再帰 -----
            return self.predict_character(target_answers, state, expected_character_ids)

        else:
            # 最後の絞り込みで候補が０になったということなので直前の結果から適当に返す．
            return previous_expeected_ids[0], state

    def run(self):
        aa.smiling()
        print("やあ、私はアキネイター Command Line Inetrface (CLI)です．")
        print("有名な人物やキャラクターを思い浮かべて．魔人が誰でも当ててみせよう．魔人は何でもお見通しさ．")
        print("5秒後に開始します．")
        count_down(5)

        predicted_character_id, state = self.predict_character(self.data_handler.all(), [], [character.id for character in self.character_handler.all()])
        predict_character = self.character_handler.find_by_id(predicted_character_id)

        time.sleep(0.5)
        print(f"\nAnswer: 思い浮かべているのは ... {predict_character.name} ですか？(y/n)")
        ans = input()
        if ans == "y":
            aa.happy()
            print("よぉし！, また正解！！魔人は何でもお見通しだ!")

        else:
            aa.sad()
            print("(悲しみのアーキネータ君 ...)")

            while True:
                print("\n----- あなたが思い浮かべたキャラクターの名前を記入してください． -----")
                predict_name = input()
                predict_character = self.character_handler.data_by_name(predict_name)

                if predict_character is None:
                    print(f"{predict_name} はデータベースに存在しません．")
                    print("\n類似するキャラクター名\n")
                    print(self.character_handler.similer_data_with_name(predict_name))

                    print(f"\n{predict_name} を新たに登録しますか？(y/n)")
                    ans = input()
                    if ans == "y":
                        self.character_handler.add(predict_name)
                        predict_character = self.character_handler.data_by_name(predict_name)
                        break

                    else:
                        continue

                else:
                    break

        # ----- せっかく回答してくれたので回答履歴として保存する．
        print(f"\n----- The End of Akinator CLI, 今回の {predict_character.name} に関する回答を保存しますか？(y/n)")
        ans = input()
        if ans == "y":
            for s in state:
                self.data_handler.add(s["question_id"], predict_character.id, s["answer"])

    def mode_add(self):
        while True:
            print("\n----- キャラクターの名前を記入してください． -----\n")
            name = input()

            character = self.character_handler.data_by_name(name)
            if character is None:
                print(f"{name} はデータベースに存在しません．")
                print("類似するキャラクター名")
                print(self.character_handler.similer_data_with_name(name))
                continue

            print(f"\n----- {name} に関する以下の質問に答えてください -----")
            index = 1
            all = len(self.question_handler.all())
            for question in self.question_handler.all():
                print(f"\n({index}/{all}): {question.name} (1: はい, 2: いいえ, 3: わからない, 9: 終了)")
                try:
                    ans = int(input())

                except Exception as e:
                    ans = 9
                    print(e)
                    print("エラーが発生しましたので終了します．")

                if ans == 9:
                    break

                self.data_handler.add(question.id, character.id, ans)


            print(f"\n----- {name} に関する以下の質問を終了します． -----\n")
            print("他のキャラクターに関する回答を続けますか？(y/n)")
            ans = input()
            if ans == "y":
                continue

            else:
                break


class AnswerModeHandler(SmapleAnswerModeHandler):
    def predict_character(self, target_answers, state, previous_expeected_ids=[]):
        # target_answers は Answerオブジェクトのリストです．
        # state は回答の途中経過です, ex. [{"question_id": 1, "answer": 1}, ..., {"question_id": 20, "answer": 1}]
        # previous_expeected_ids は前の回答にて候補となったキャラクターのIDです，再起を使わなければ不必要だと思います．
        #
        # return では予測したキャラクターのIDとstate を返すようにしましょう．
        # ex. return character_id, state

        # ----- 下記のコードを消して，この間にアーキネーターのロジックを書く -----
        return super().predict_character(target_answers, state, previous_expeected_ids)
        # ----- この間にアーキネーターのロジックを書く -----
