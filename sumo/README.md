# Mos-Kensyu: SUMO
この研修では以下の作業ができるようになることを期待しています．

- sumo が自分の環境で使えるようになる．
- git が自分の環境で使えるようになる．
- 特性評価によって改善点を指摘できる．
- 改善するためのアイデアをプログラム化することができる．

研修では以下の内容を進めてください．

## sumo をインストールする．

以下のページを参考にすると良い．

https://sumo.dlr.de/docs/Installing.html

SUMO がインストールされていれば以下のコマンドが使えるようになる
```sh
sumo
sumo-gui
```

また，以下のコマンドによって SUMO_HOME が環境変数に設定されていることを確認
```sh
echo $SUMO_HOME
```

## git を自分の環境にインストールする．

以下のページを参考にすると良い．

https://git-scm.com/book/ja/v2/%E4%BD%BF%E3%81%84%E5%A7%8B%E3%82%81%E3%82%8B-Git%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB

git がインストールされていれば以下のコマンドが使えるようになる．
```sh
git
```

## git を使いこなす．

gitに関する説明は下記のスライドを参照

https://docs.google.com/presentation/d/1D48Ss_3Vysgoh8cOC6k6e-4sqC0lcTKa_6z93vpa-Rg/edit#slide=id.g84dd18d9ed_0_7

適当なディレクトリを作成し，ディレクトリ内で以下のコマンドを実行する．
```sh
git clone https://github.com/uruzahe/Mos-Kensyu.git
```

成功した場合，mos-kensyu というディレクトリがダウンロードされる．

mos-kensyu ディレクトリに移動し，以下のコマンドを実行する
```sh
# ex. git checkout -b kensyu_yoshida
git checkout -b kensyu_{自分の名前}
```

git のコマンド一覧を下記に書くので，適宜使用する．
```sh
# 現在のブランチを確認
git branch

# 変更差分を確認
git status

# 変更差分を仮登録にする．
git add .

# 仮登録された変更差分に名前をつけて保存する．
git commit -m "仮登録をまとめた名前"

# 保存した変更差分をリモートサーバに反映させる
git push origin kensyu_{自分の名前}
```

## サンプルコードの実行
以下のコマンドが実行できるか確認

```sh
# 1台の車両が道路を走行するシナリオ
# 簡単なシナリオなので，最初は以下のコマンドを使用する．
python runner.py --sample

# N台の車両が道路を走行するシナリオ
# 徐々にシナリオを複雑にしていくために使用．
python runner.py --sample --sample_num N

# GUI無しでプログラムを実行する場合に使用．
python runner.py --nogui --sample --sample_num N

# 車両制御を行わないシナリオ
# 何も制御を行わない場合の特性を取得する際に使用．
python runner.py --sample --sample_num N --unapply_prop
```

## 改善するべき特性を１つ決定し， 車両台数に対する特性の変化をグラフ化する．

SUMO標準のメソッド(getSpeed メソッド等)を使用することで様々な特性（速度等）を取得することができる（下記のサイトを参考に）

https://sumo.dlr.de/daily/pydoc/traci.html
https://sumo.dlr.de/daily/pydoc/traci._simulation.html

所望の特性を取得するメソッドを確認し，runner.py 中の formatted_data メソッド中に特性を取得するメソッドを追記する．

例えば，車速の特性評価を取りたい場合はgetSpeed メソッドを formatted_data メソッド中追記する．
```py
def formatted_data(self, veh_id):
        formatted_data = {
            "id": veh_id,
            "time": traci.simulation.getCurrentTime(),
            "speed": traci.vehicle.getSpeed(veh_id),
        }

        return formatted_data
```

特性を取得するメソッドを追記後，以下のコマンドを実行し，"./result/all/" ディレクトリ配下に "sample_num_10_apply_prop_False.csv" が配置されることを確認
```sh
python runner.py --sample --sample_num 10 --unapply_prop
ls ./result/all
cat ./result/all/sample_num_10_apply_prop_False.csv
```

成功すれば sample_num_10_apply_prop_False.csv 中に取得したい特性が追記されるので，excel等で開いて確認する．

以下のコマンドを実行することで，車両数を10刻みで変更した場合の特性を取得することができる．
```sh
python runner.py --sample --sample_num 10 --unapply_prop
python runner.py --sample --sample_num 20 --unapply_prop
python runner.py --sample --sample_num 30 --unapply_prop
python runner.py --sample --sample_num 40 --unapply_prop
python runner.py --sample --sample_num 50 --unapply_prop
python runner.py --sample --sample_num 60 --unapply_prop
python runner.py --sample --sample_num 70 --unapply_prop
python runner.py --sample --sample_num 80 --unapply_prop
python runner.py --sample --sample_num 90 --unapply_prop
python runner.py --sample --sample_num 100 --unapply_prop
```

"./result/all/" ディレクトリ配下にそれぞれの特性が出力されるので，Excel や matplotlib 等を使用して，車両台数に対する特性の変化をグラフ化する．

## 自分が選んだ特性を改善するように車両を制御する．

SUMO標準のメソッド(setSpeed メソッド等)を使用することで車両を制御することができる（下記のサイトを参考に）

https://sumo.dlr.de/daily/pydoc/traci._simulation.html

runner.py 中の vehicle_manupulation メソッド中に車両を制御するコードを書き，自分が選択した特性を改善するように努める．

```py
def vehicle_manipulation():
    # この下に好きにコードを書いてください.

    # この上に好きにコードを書いてください.
    pass
```

特性評価を行う場合は以下のコードを実行する．
```sh
# N台の車両が道路を走行するシナリオ
python runner.py --sample --sample_num N
```
