#!/bin/bash
# SPDX-FileCopyrightText: 2025 Kazuki Nakagawa
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws

# 1. 追記: ros2コマンドを使えるようにする
source /opt/ros/humble/setup.bash

# ビルドと環境読み込み
colcon build
source install/setup.bash

# ノードを10秒間実行してログを保存
# 2. 修正: 末尾に 2>&1 をつける
timeout 10 ros2 run ros2_pomodoro pomodoro_timer > /tmp/ros2_pomodoro.log 2>&1

# ログの確認
# 正常に動いていれば "Remaining: 24:59" という文字が出ているはず
cat /tmp/ros2_pomodoro.log |
grep 'Remaining: 24:59'

#-このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
#-© 2025 Kazuki Nakagawa
