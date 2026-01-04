# SPDX-FileCopyrightText: 2025 Kazuki Nakagawa
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from rclpy.executors import ExternalShutdownException # 追加
from std_msgs.msg import String

class PomodoroTimer(Node):
    def __init__(self):
        super().__init__('pomodoro_timer')
        self.pub = self.create_publisher(String, 'remaining_time', 10)
        self.remaining_sec = 25 * 60  # 25分 = 1500秒
        self.create_timer(1.0, self.timer_callback) # 1秒ごとに実行

    def timer_callback(self):
        # 分と秒に変換
        minutes = self.remaining_sec // 60
        seconds = self.remaining_sec % 60

        # メッセージ作成
        msg = String()
        msg.data = f"Remaining: {minutes:02d}:{seconds:02d}"

        self.pub.publish(msg)
        self.get_logger().info(f"Publish: {msg.data}")

        # カウントダウン（0になるまで）
        if self.remaining_sec > 0:
            self.remaining_sec -= 1

def main():
    rclpy.init()
    node = PomodoroTimer()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException): # 変更: ExternalShutdownExceptionもキャッチ
        pass
    finally:
        node.destroy_node()
        if rclpy.ok(): # 追加: まだ終了していない場合のみshutdown
            rclpy.shutdown()

if __name__ == '__main__':
    main()
