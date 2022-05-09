# メモ

## npm

node.jsのパッケージ管理ツール

## npm install

### 引数無し

カレントディレクトリにある`package.json`をもとに`node_modules`にパッケージをインストール。
`package.json`がなかったら`npm ERR! enoent ENOENT: no such file or directory, open C:\Users\username\Desktop\package.json'`て言われた。（`%homepath%\Desktop`でやったとき）

### npm install -g \<package-name\>

グローバル領域にパッケージをインストール。自分の環境だとたぶんここ。（Windows11 21H2）  
`%ProgramFiles%\nodejs\node_modules`

### npm install \<package-name\>

ローカル環境にパッケージをインストール。

### npm install -D \<package-name\>

ローカル環境にパッケージをインストール。
`-D` は `--save-dev` の略。開発のときしか使わないdevDependenciesなパッケージ（実行には必要ないパッケージのこと？）はこうやってインストールする。
これは便利。

### npm install --production

`npm install` 引数無しのときと違って、dependenciesなパッケージのみインストールしてくれる。

## npx

なんかいい感じにしてくれるとんでもないコマンド。
順番は

1. ローカル
1. システム領域
1. npm registry

なのかな？
使い終わったパッケージは消してくれるから環境を汚さないらしい。

## npm audit

npmパッケージをaudit（監査）してくれる。

## npm outdated

outdatedなnpmパッケージをチェックしてくれる。

## npm update

パッケージをいい感じに（tag, semver制約を尊重）アップデートする。
`npm update --save` で`package.json`も更新する。
