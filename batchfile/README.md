# Windows バッチファイル置き場
## 作ったもの
* [vfr2cfr.bat](./vfr2cfr.bat)  
  vfrな動画をcfrな動画に変換する。
    * ffmpegが必要
    * 複数ファイルまとめてドラッグアンドドロップ可能
* [video_merge.bat](./video_merge.bat)  
  複数の動画をくっつけて一つの動画にする。
    * ffmpegが必要
    * 複数ファイルまとめてドラッグアンドドロップ可能
    * つなげる動画は全部同じコーデックである必要がある
        * 違うコーデックが混ざっているのは試していない
    * nintendo switchとかの連番動画をつなげるために作った
* [extractaudio.bat](./extractaudio.bat)  
  動画の音声を抽出する。
    * ffmpegが必要
    * 複数ファイルまとめてドラッグアンドドロップ可能
    * コンテナ（拡張子）は手動で変える
        * 暇だったら改善する
* [extractaudio_multitrack.bat](./extractaudio_multitrack.bat)  
  上記のマルチトラック音声対応版、複数の音声トラックを含む動画から1トラックずつ音声を抽出する。
    * obsとかで撮った複数の音声トラックを含む動画の音声をばらばらにしたいときに使う
* [volumedetect.bat](./volumedetect.bat)  
  音量を調べられる
    * ffmpegが必要
* [set_onetime_path.bat](./set_onetime_path.bat)  
  一時的にadbとかのパスを通す
    * ホームディレクトリに置いとくと便利


# メモ
## 遅延環境変数
`!value!`, みたいな`!`で囲むやつ。

for文とかif文の丸かっこ（）で囲むやつは、**1行**とみなして実行される。
なので、変数代入時に代入したつもりが何も起こってないように見える。

丸かっこ内で定義した変数を同じ丸かっこ内で使いたいときは遅延環境変数を使うことでいい感じにやってくれる。

`setlocal ENABLEDELAYEDEXPANSION`

を、ファイルの一番上とかで設定して`!value!`, みたいな`!`で囲んだ変数を使えばいい。変数読み込みのタイミングを遅延してくれる。
