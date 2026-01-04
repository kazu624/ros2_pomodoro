#!/bin/bash
# SPDX-FileCopyrightText: 2025 Kazuki Nakagawa
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws

# ビルドと環境読み込み
colcon build
source install/setup.bash

# ノードを10秒間実行してログを保存
# (ros2 run で直接起動します)
timeout 10 ros2 run ros2_pomodoro pomodoro_timer > /tmp/ros2_pomodoro.log

# ログの確認
# 正常に動いていれば "Remaining: 24:59" という文字が出ているはず
cat /tmp/ros2_pomodoro.log |
grep 'Remaining: 24:59'
