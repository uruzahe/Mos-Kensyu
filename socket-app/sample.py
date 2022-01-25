import tkinter as tk

def btn_click():

    # 入力した値を取得
    text1 = input_text.get()
    # 入力した値をラベルに出力
    label2['text'] = text1

baseGround = tk.Tk()
# GUIの画面サイズ
baseGround.geometry('1200x800')
#GUIの画面タイトル
baseGround.title('入力値をラベルに表示する')

# テキストボックス
input_text = tk.Entry()
input_text.pack()

# ボタン
btn = tk.Button(baseGround, text='入力値を出力', command=btn_click)
btn.pack()

# ラベル
label1 = tk.Label(text = '入力値:')
label1.pack()
label2 = tk.Label()
label2.pack()

#表示
baseGround.mainloop()
