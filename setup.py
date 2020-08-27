from setuptools import setup
import shutil
import os

setup(
    name='i3-unity-fix',
    version='1',
    packages=['i3unityfix'],
    package_data={},
    author="Mikołaj Gałkowski",
    author_email="hello@mikolajgalkowski.xyz",
    description="Fixes unity3d editor repaint issue when switching workspaces in the i3 window manager",
    long_description=open('README.md').read(),
    long_description_content_type='text/x-md',
    license="GPLv3",
    keywords="i3 unity3d",
    url="https://github.com/tesq0/i3-unity-fix",
    entry_points={
        'console_scripts': ['i3-unity-fix = i3unityfix.i3unityfix:main']
    },
    install_requires=[
        "i3ipc"
    ],
    data_files=[
        ('share/man/man1', ['i3-unity-fix.1'] if os.path.exists('i3-unity-fix.1') else []),
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
    ]
)
