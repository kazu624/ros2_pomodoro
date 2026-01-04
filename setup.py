# SPDX-FileCopyrightText: 2025 Kazuki Nakagawa
# SPDX-License-Identifier: BSD-3-Clause

from setuptools import find_packages, setup

package_name = 'ros2_pomodoro'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kazuking',
    maintainer_email='s24c1089eq@s.chibakoudai.jp',
    description='A Pomodoro Timer package for ROS 2',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pomodoro_timer = ros2_pomodoro.pomodoro_timer:main',
        ],
    },
)
