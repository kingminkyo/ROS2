from setuptools import setup

package_name = 'my_first_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='minkyo2',
    maintainer_email='maplezero@naver.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_first_node = my_first_package.my_first_node:main',
            'my_subscriber = my_first_package.my_subscriber:main',
            'my_publisher = my_first_package.my_publisher:main'
        ],
    },
)
