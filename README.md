# demo-flask

PythonフレームワークのFlask練習用

## メイン操作

参考1  
https://youtu.be/bzbrpkbjWe8  
参考2  
https://youtu.be/mW0_60SRr3s  
参考3  
https://youtu.be/Gyy1tzwenc8

全てappフォルダ内で作業し、問題があればissueすること

## Git操作の手順

### 手順 1: このリポジトリをローカルの開発用ディレクトリににクローンする

```
$ git clone git@github.com:gwrhyr/demo-flask.git
```

* 共同開発しない場合

    新たに自分のリモートリポジトリを作って勝手にやる。

* 共同開発する場合

    新たにブランチを切って作業する。

### 手順 2: ブランチを切る

ブランチ名 = branch/{ユーザ名}

```
# ブランチを切って移動
$ git branch branch/{ユーザ名}
$ git checkout branch/{ユーザ名}

# 現在のブランチ確認
$ git branch
```

### 手順 3: 自分のブランチに対してコミット・プッシュして開発する

## Docker操作の手順

### 手順 1: 環境を作る

```
# dockerコマンドはプロジェクトフォルダ内で！
$ docker-compose build
```

### 手順 2: 作業開始

```
$ docker-compose up -d
```

### 手順 3: 作業中断

```
$ docker-compose down
```

### 手順 4: 後片付け

```
# 作ったイメージの確認
$ docker images
{イメージ1} {イメージ2}

$ docker-compose down
$ docker rmi {イメージ1} {イメージ2}
```
