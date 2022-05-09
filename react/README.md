# メモ

## 書きかた

関数な書き方（`function`のやつ）でも、変数にラムダ式？（`const functionName = () => {};`）みたいな書き方でも動く。
最近の主流なのは後者のほう？良さがあんまりわからないので要調査。この書き方の名称はなんていうんだろう。

### このときの脳内

変数（のようなもの）にできること多くないか。
`function`があるのなら関数定義は`function`にやらせればいいと思うのだが。  
実行をほかのコンポーネントに委譲したいときは、変数にラムダ式のほうが見やすい？

## コンポーネント

`<App />`とかのこと。関数名をhtmlのようにタグで囲むとコンポーネントとして扱える。
コンポーネントはどこかで定義する。関数のようなもの。

* [components and props](https://ja.reactjs.org/docs/components-and-props.html)
* [関数コンポーネントとクラスコンポーネント](https://ja.reactjs.org/docs/components-and-props.html#function-and-class-components)

## Props

コンポーネントに渡す引数のようなもの。**読み取り専用**。

* [Props は読み取り専用](https://ja.reactjs.org/docs/components-and-props.html#props-are-read-only)

## React Hooks

* [React Hooks](https://ja.reactjs.org/docs/hooks-intro.html)
  * [動機](https://ja.reactjs.org/docs/hooks-intro.html#motivation)

### useState

Stateを扱う

#### ReactにおけるStateとは

画面に表示するデータ、可変の状態。

### useEffect

再レンダリングされるときに、毎回処理させたくない処理がある時に使う。
再レンダリングされるとコンポーネントの初めからコードが走るため。
特定の値が変わったときのみ実行、みたいなことができる。

## css

書き方がいろいろある。

## コンポーネントライブラリ

## 再レンダリング

変化がないところは再レンダリングしたくない。なのでメモ化する。いろんなのがある。

* コンポーネントのメモ化 `memo`
* 関数メモ化 `useCallback`
* 変数メモ化 `useMemo`

## カスタムフック

機能の分離。Hook(`useなんとか`)を自作できる。
外部ファイルに関数作るイメージ。

## コンテクスト

* [コンテクスト](https://ja.reactjs.org/docs/context.html)
