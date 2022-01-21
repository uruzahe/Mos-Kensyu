## 研修概要

自身のパソコン（ローカル環境）に研修環境を構築します．具体的にはVirtualBoxにて立ち上げたdebian(linux)を研修環境として使用します．

## 事前準備

git, VirtualBox, Vagrant, をローカル環境にインストールする．

#### git

https://github.com/uruzahe/Mos-Kensyu/tree/220116/sumo#git-%E3%82%92%E8%87%AA%E5%88%86%E3%81%AE%E7%92%B0%E5%A2%83%E3%81%AB%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B

#### VirtualBox

https://www.virtualbox.org/

バーチャルボックスのインストールが完了したら下記のコマンドにてバーチャルボックスのバージョンを確認する．
```sh
vboxmanage --version
# 6.0.22r137980 のような値を返すので，6.0.22の部分をメモしておく．
# 後々にVBOX_VERSIONという環境変数にバーチャルボックスのバージョンを設定する．
```
#### Vagrant

https://www.vagrantup.com/downloads

## 研修環境構築

#### debian(linux)の起動

1. ローカル環境にて下記のコマンドを実行する．
``` sh
# ローカル環境
git clone --recurse-submodule https://github.com/riebl/artery.git
cd artery
```

2. arteryディレクトリ内のVagrantfile中にて "vb.memory = 2048" を "vb.memory = 4096" に変更する．

3. 下記のコマンドにてdebian(linux)のデスクトップ環境を起動する
```sh
# ローカル環境
vagrant up
```

4. 起動後ローカル環境にて下記のコマンドを実行し，debianのターミナルにssh接続する．
```sh
# ローカル環境
vagrant ssh
```

5. ssh接続後のターミナル(debian)にて下記のコマンドを実行する．
```sh
# 研修環境
sudo -i
VBOX_VERSION='自分のバーチャルボックスのバージョン(ex. 6.0.22)'
# ex. VBOX_VERSION='6.0.22'
wget http://download.virtualbox.org/virtualbox/$VBOX_VERSION/VBoxGuestAdditions_$VBOX_VERSION.iso
mount -o loop,ro VBoxGuestAdditions_$VBOX_VERSION.iso /mnt
sh /mnt/VBoxLinuxAdditions.run --nox11
umount /mnt
rm VBoxGuestAdditions_$VBOX_VERSION.iso
unset VBOX_VERSION
reboot
```

rebootコマンドによってdebianデスクトップが再び立ち上がる．
debianデスクトップ内の左下部にターミナルを開くボタンがあるので，デスクトップ内にてターミナルを立ち上げる．以降の研修環境のターミナルを使う場面ではデスクトップ内のターミナルを使う．

#### SUMO
研修環境にて既に実行可能な状態である．下記のコマンドが実行可能であることを確認する．
```sh
# 研修環境
sumo
sumo-gui
```

#### Omnet++
研修環境にて既に実行可能な状態である．下記のコマンドが実行可能であることを確認する
``` sh
# 研修環境
omnetpp
```

さらにチュートリアル用のモジュールをインストールするために下記の動画の"Launching OMNET(5:55 ~ 7:20)"の部分を実施する．

https://youtu.be/PfAWhrmoYgM?t=349

#### NS3

研修環境にて下記のコマンドにてNS3をインストールする．

```sh
# 研修環境
cd
mkdir ns3
cd ns3
wget https://www.nsnam.org/release/ns-allinone-3.35.tar.bz2
tar xjf ns-allinone-3.35.tar.bz2
cd ns-allinone-3.35
./build.py --enable-examples --enable-tests
./test.py
```

インストール後，下記のコマンドにてサンプルコードが実行可能であることを確認する．
```sh
# 研修環境
./ns3 run hello-simulator
```
