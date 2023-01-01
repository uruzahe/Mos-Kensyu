## 研修概要

自身のパソコン（ローカル環境）に研修環境を構築します．具体的にはVirtualBoxにて立ち上げたdebian(linux)を研修環境として使用します．

## 事前準備

git, VirtualBox, Vagrant, をローカル環境にインストールする．

#### git

https://github.com/uruzahe/Mos-Kensyu/tree/220116/sumo#git-%E3%82%92%E8%87%AA%E5%88%86%E3%81%AE%E7%92%B0%E5%A2%83%E3%81%AB%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B

#### VirtualBox

通常は以下からダウンロードする．

https://www.virtualbox.org/

MacでM1チップの人は以下からダウンロードする．

https://www.virtualbox.org/wiki/Downloads

バーチャルボックスのインストールが完了したら下記のコマンドにてバーチャルボックスのバージョンを確認する．
```sh
vboxmanage --version
# 6.0.22r137980 のような値を返すので，6.0.22の部分をメモしておく．
# 後々にVBOX_VERSIONという環境変数にバーチャルボックスのバージョンを設定する．
```
#### Vagrant

https://www.vagrantup.com/downloads

vagrantはバーチャルボックスを簡単に扱うためのツールである．vagrantコマンドの一覧は下記のURLから確認可能．

https://qiita.com/oreo3@github/items/4054a4120ccc249676d9

## 研修環境構築

#### debian(linux)の起動

1. ローカル環境にて下記のコマンドを実行する．
``` sh
# ローカル環境
# 研修用のコードをダウンロード
git clone https://github.com/uruzahe/Mos-Kensyu.git
cd Mos-Kensyu/kensyu-devenv/
# 研修環境をダウンロード
git clone --recurse-submodule https://github.com/riebl/artery.git
cd artery
```

2. arteryディレクトリ内のVagrantfile中にて "vb.memory = 2048" を "vb.memory = 4096" に変更する(わからなかったら[サンプルを参考に](https://github.com/uruzahe/Mos-Kensyu/blob/master/kensyu-devenv/Vagrantfile-sample))．

3. Vagrantfile を下記のように修正(わからなかったら[サンプルを参考に](https://github.com/uruzahe/Mos-Kensyu/blob/master/kensyu-devenv/Vagrantfile-sample))．
```
Vagrant.configure("2") do |config|
    config.vm.box = "debian/contrib-buster64"
    # ----- 以下追加 -----
    config.vm.synced_folder "./../../Mos-Kensyu/", "/home/vagrant/Mos-Kensyu"
    config.ssh.forward_agent = true
    config.ssh.forward_x11 = true
```

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
研修環境にて既に実行可能な状態である．下記のコマンドが実行可能であることを確認する．
``` sh
# 研修環境
omnetpp
```

ワークスペースのパスには"/home/vagrant/Mos-Kensyu/omnet/workspace"を設定する．

さらにチュートリアル用のモジュールをインストールするために下記の動画の"Launching OMNET(5:55 ~ 7:20)"の部分を実施する．

7:20 辺りの"install INET Framework", "import OMNet++ programing examples"に<b>チェックを付けた状態で</b>OKを押す

https://youtu.be/PfAWhrmoYgM?t=349

#### NS3

研修環境にて下記のコマンドにてNS3をインストールする．

```sh
# 研修環境
cd ~/Mos-Kensyu/ns3
wget https://www.nsnam.org/release/ns-allinone-3.35.tar.bz2
tar xjf ns-allinone-3.35.tar.bz2
cd ns-allinone-3.35
./build.py --enable-examples --enable-tests
cd ns-3.35
./test.py
```

インストール後，下記のコマンドにてサンプルコードが実行可能であることを確認する．
```sh
# 研修環境
./waf --run hello-simulator
```

## その他（メモ，プラスアルファ）

#### シミュレータをビルドする際にメモリ不足になる．

下記の方法のいくつかを実行し使用可能なメモリを増やす．

- 研修環境にて不要なアプリが開いている場合は閉じる．
- Vagrantfile中にて, vb.memoryの値を増加させる(vb.memory = 1024 * N )
  - 自分のパソコンのメモリの半分くらいに設定しておくと良い
  (ex. 自分のパソコンのメモリが8GBならN=4)
  - ローカル環境にて不要なアプリ（chromeとか）開いている場合は閉じる．
- Vagrantfile中にて, vb.gui = false に変更する
  - デスクトップに割いていたメモリをビルドに使用可能になる．
  - 作業は "vagrant ssh" にてターミナルに接続することで行う．
  - 作業が終わったら vb.gui = true に変更し再起動．

<!--
#### 仮想環境中のエディタが重い．

atomとか比較的重いエディタを使うと動きがもっさりします．

"Sublime Text3"は軽量なのでおすすめです．下記の手順でインストール可能です．

```sh
# 研修環境
sudo apt-get install apt-transport-https
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
sudo apt-get update
sudo apt-get install sublime-text
```

下記のコマンドのように適当なディレクトリを開ければインストール完了です．

```sh
subl .
```

#### それでもエディタが重い（X11 forwarding）

"X11 forwarding"を使いましょう．下記の手順で設定してください．


1. 自分のパソコンにて x11 client の設定を行う．
  - mac: xquartzのインストールと実行のみで良い．http://www.xquartz.org/
  - windows:

2. ローカル環境から研修環境にssh接続した後にターミナルからエディタが開けることを確認する．

```sh
# ローカル環境
vagrant ssh

# 研修環境
subl ./ns3
```
-->

#### 仮想環境中の表示が重い
 Vagrantfile中のvb.customizeを下記のように変更し再起動する．

 （これでも重かったらすいません．．．，ブラウザは重い傾向にあるのでローカル環境のブラウザを使った方が良いです．）

 ```
 vb.customize [
     "modifyvm", :id,
     "--vram", "256",
     "--clipboard", "bidirectional",
     "--accelerate3d", "on",
     "--hwvirtex", "on",
     "--nestedpaging", "on",
     "--largepages", "on",
     "--ioapic", "on",
     "--pae", "on",
     "--paravirtprovider", "kvm",
   ]
 ```
