# -*- encoding: UTF-8 -*-

from setuptools import setup, find_packages

setup(
    name='pdssoyoger',  # 包名
    version="0.0.1",  # 版本信息
    author="Soyoger",
    author_email="810480876@qq.com",
    description="python_base",
    license="MIT",
    keywords="python_base",
    url="https://github.com/sujeek/python_base",
    packages=find_packages('src'),  # 要打包的项目文件夹
    package_dir={'': 'src'},
    include_package_data=True,  # 自动打包文件夹内所有数据
    zip_safe=True,  # 设定项目包为安全，不用每次都检测其安全性
    install_requires=[  # 安装依赖的其他包
        'neso2',
        'pytest',
        'cov-core',
        'subprocess',
        'argparse'
    ]
)
