from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'tb3_multirobot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name,'launch'),
         glob('launch/*launch.[pxy][yma]*')),
        (os.path.join('share',package_name,'urdf'),
         glob('urdf/*')),
        (os.path.join('share',package_name,'params'),
         glob('params/*')),
        (os.path.join('share',package_name,'rviz'),
         glob('rviz/*')),
        (os.path.join('share',package_name,'worlds'),
         glob('worlds/*')),
        (os.path.join('share',package_name,'maps'),
         glob('maps/*')),
        (os.path.join('share',package_name,'scripts'),
         glob('scripts/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros',
    maintainer_email='ros@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
