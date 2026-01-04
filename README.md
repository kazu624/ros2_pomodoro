# ros2_pomodoro

![test](https://github.com/kazu624/ros2_pomodoro/actions/workflows/test.yml/badge.svg)

ROS 2で動作するポモドーロ・タイマーパッケージです。
作業時間と休憩時間を管理し、残り時間をトピックとして配信します。

## 実行環境
* Ubuntu 22.04 LTS
* ROS 2 Humble Hawksbill
* Python 3.10

## ノードとトピック

### ノード: `pomodoro_timer`
ポモドーロ・タイマーのメインノードです。起動すると自動的に25分間のカウントダウンを開始します。

### トピック
* `/remaining_time` (std_msgs/String)
    * **機能**: 現在の残り時間を配信します。
    * **データ形式**: `Remaining: MM:SS` （例: `Remaining: 24:59`）
    * **頻度**: 1Hz（1秒ごとに配信）

## 使用方法

以下のコマンドでノードを起動します。

```bash
$ ros2 run ros2_pomodoro pomodoro_timer
```

## ライセンス
このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．

## 著作権
© 2025 Kazuki Nakagawa
