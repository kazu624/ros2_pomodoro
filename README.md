# ros2_pomodoro

![test](https://github.com/kazu624/ros2_pomodoro/actions/workflows/test.yml/badge.svg)

## 概要
ROS 2で動作するポモドーロ・タイマーパッケージです。

## 環境
* Ubuntu 22.04 LTS
* ROS 2 Humble Hawksbill
* Python 3.10

## インストール

```bash
$cd ~/ros2_ws/src$ git clone [https://github.com/kazu624/ros2_pomodoro.git](https://github.com/kazu624/ros2_pomodoro.git)
$cd ~/ros2_ws$ rosdep install -i --from-path src --rosdistro humble -y
$ colcon build --packages-select ros2_pomodoro
```

## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- © 2025 Kazuki Nakagawa
