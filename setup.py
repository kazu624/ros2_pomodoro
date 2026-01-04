# SPDX-FileCopyrightText: 2025 Kazuki Nakagawa
# SPDX-License-Identifier: BSD-3-Clause

from setuptools import find_packages, setup

package_name = 'ros2_pomodoro'

setup(
    name=package_name,
    version='0.0.0',
    # __init__.py があるので、標準的な自動検索機能を使います
    packages=find_packages(exclude=['test']),
    data_files=[
        # resource ディレクトリの参照は削除したままにします
        # ('share/ament_index/resource_index/packages',
        #     ['resource/' + package_name]),
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

#-このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
#-© 2025 Kazuki Nakagawa
