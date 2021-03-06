# NeuralVirtualCam
実際のカメラから取得した画像をGANで変換して仮想カメラ経由で垂れ流すやつ。
Linux専用かつGPU必須。

# Require
```
$ apt-get install v4l2loopback-utils

$ conda install pytorch torchvision cudatoolkit=10.1 -c pytorch
$ conda install -c conda-forge opencv
$ pip install pyfakewebcam
```

- モデルのダウンロード
```
$ cd fast_neural_style
$ python download_saved_models.py
```
# Usage
```
$ ls /dev/|grep video
```
とかやると
```
video0
video1
video2
```
とか出てくる。今回video3を使っていないので、/dev/video3とかに流したいとする。その場合
```
$ sudo modprobe v4l2loopback video_nr=3
```
とコマンドを叩くことで仮想カメラの口をつくる。
口を用意したら
```
// python main 接続先カメラ番号 出力先パス
// 上で設定した仮想カメラ(/dev/video3)を出力先パスに渡す
$ python main.py 0 /dev/video3
```

動画が表示されているウィンドウにフォーカスして操作
- q : 終了
- a,s,d,f : スタイル変更
- z : 無変換

web camに流れている映像を確認したい場合はffplayコマンドを使う
```
ffplay /dev/video3
```

# こんな感じ。
LinuxのGPUマシン変換したものを仮想カメラ経由でGoogleハングアウトに垂れ流してMac book proで受信している。
![app](https://github.com/nenoNaninu/NeuralVirtualCam/blob/master/app.gif)

# ちなみに
Googleハングアウトにおいては、chromeには問題なく垂れ流せた。
FireFoxにおいてはさっくり動画を(普通のwebカメラでさえ)流せなかった...。
