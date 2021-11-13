# Windows バッチファイルのめも

## 遅延環境変数
!a!, みたいな`!`で囲むやつ。

for文とかif文の丸かっこ（）で囲むやつは、**1行**とみなして実行される。
なので、変数代入時に代入したつもりが何も起こってないように見える。
* 変数に計算して代入後、その変数を丸かっこ内で使うとき

その時は**遅延環境変数**を使えばいい。

`setlocal ENABLEDELAYEDEXPANSION`

と、ファイルの一番上とかで設定して`!a!`, みたいな`!`で囲んだ変数を使えばいい。変数読み込みのタイミングを遅延してくれる。