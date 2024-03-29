## 研修概要

本研修では既存の通信技術をシミュレーションで再現し，通信における実際の処理ととシミュレーションにおける処理の双方を理解することを目的としています．

## 事前準備

下記のURLに従い研修環境を作成し，仮想環境中にてNS3が動くようにする．

https://github.com/uruzahe/Mos-Kensyu/tree/master/kensyu-devenv

## 研修内容

下記の３点を進めてください．

1. 仮想環境中の[examplesディレクトリ](https://github.com/nsnam/ns-3-dev-git/tree/master/examples)からサンプルコードを一つ選択し，選択したサンプルコードが実行可能であることを確認する．
2. 選択したサンプルコード中のシステムを現実世界で実際に構成すると仮定する際，OSI参照モデルにおける各レイヤにおいてどのような処理が行われているかをスライドにまとめる．
3. OSI参照モデルにおける各レイヤの処理がシミュレーションではどのように実装されているかをスライドにまとめる．
4. 現実世界での処理とシミュレーション中の処理の差分をスライドにまとめる．
5. シミュレーション中にて，アプリケーションレイヤ間の通信における通信遅延，及びスループットを計測する．
6. 通信遅延とスループットに関して理論値を算出し，理論値と計測値の差分を考察する．
7. (+α)理論値や実測値を参考に，選択したサンプルコードのような構成を実際に適応することが困難な場面（問題点）を考察する．
