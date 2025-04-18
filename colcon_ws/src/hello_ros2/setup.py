from setuptools import find_packages, setup
import os
from glob import glob  # 특정한 규칙의 파일을 추출할 때 필요

package_name = 'hello_ros2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        # ament index에 패키지를 등록하기 위한 설정
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        # 패키지의 package.xml을 설치하기 위한 설정
        ('share/' + package_name,
         ['package.xml']),
        # launch 디렉터리 안의 모든 .launch.py 파일을 설치하기 위한 설정
        ('share/' + package_name + '/launch',
         glob(os.path.join('launch', '*.launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='son',
    maintainer_email='you@example.com',
    description='TODO: Package description',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'hello_ros = hello_ros2.hello_ros:main',
            'move_turtle = hello_ros2.move_turtle:main',
            'simple_sub = hello_ros2.simple_sub:main',
            'simple_pub = hello_ros2.simple_pub:main',
        ],
    },
)
