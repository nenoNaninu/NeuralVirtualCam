# NeuralVirtualCam
実際のカメラから取得した画像をGANで変換して仮想カメラ経由で垂れ流すやつ

# Require
```
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
//実際のカメラの接続数+1。カメラが1個の場合は2
$ sudo modprobe v4l2loopback devices=2

// python main 接続先カメラ番号 出力先パス
// 想カメラが2台目なら /dev/video1 でok
$ python main.py 0 /dev/video1
```

動画が表示されているウィンドウにフォーカスして操作
- q : 終了
- a,s,d,f : スタイル変更


web camに流れているのを確認したい場合
```
ffplay /dev/video1
```

# ちなみに
Googleハングアウトにおいては、chromeには問題なく垂れ流せた。
FireFox,Linuxにおいてはさっくり動画を(普通のwebカメラでさえ)流せなかった...。