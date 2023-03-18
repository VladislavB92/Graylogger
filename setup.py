from io import open
from setuptools import setup

"""
:authors: v.oficerov
:license: MIT License
:copyright: (c) 2023 v.oficerov
"""

version = '0.1.0'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='graylogging',
    version=version,

    author='v.oficerov',
    author_email='valeryoficerov@gmail.ru',

    description='Набор graylog хэндлеров для библиотеки logging.',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/Oficerov/Graylogging',
    download_url=f'https://github.com/Oficerov/Graylogging/archive/refs/heads/v{version}.zip',

    license='MIT License',

    packages=['graylogging'],

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)