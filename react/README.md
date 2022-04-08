# メモ
# npm
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

# 書きかた
関数な書き方（`function`のやつ）でも、変数にラムダ式？（`const functionName = () => {};`）みたいな書き方でも動く。
最近の主流なのは後者のほう？良さがあんまりわからないので要調査。この書き方の名称はなんていうんだろう。
## このときの脳内
変数（のようなもの）にできること多くないか。
`function`があるのなら関数定義は`function`にやらせればいいと思うのだが。  
実行をほかのコンポーネントに委譲したいときは、変数にラムダ式のほうが見やすい？

# コンポーネント

# React Hooks
* [公式ドキュメント（日本語）](https://ja.reactjs.org/docs/hooks-intro.html)
    * [動機](https://ja.reactjs.org/docs/hooks-intro.html#motivation)

## useState
Stateを扱う
### ReactにおけるStateとは
画面に表示するデータ、可変の状態。

## useEffect
再レンダリングされるときに、毎回処理させたくない処理がある時に使う。
再レンダリングされるとコンポーネントの初めからコードが走るため。
特定の値が変わったときのみ実行、みたいなことができる。

# css
書き方がいろいろある。
## コンポーネントライブラリ


# 再レンダリング
変化がないところは再レンダリングしたくない。なのでメモ化する。いろんなのがある。
* コンポーネントのメモ化 `memo`
* 関数メモ化 `useCallback`
* 変数メモ化 `useMemo`


# カスタムフック
機能の分離。Hook(`useなんとか`)を自作できる。
外部ファイルに関数作るイメージ。
