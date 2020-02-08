__author__ = 'Paul Severance'

from setuptools import setup

setup(
    name='sugar-router',
    version='0.0.1',
    author='Paul Severance',
    author_email='paul.severance@gmail.com',
    url='https://github.com/sugarush/sugar-router',
    packages=[
        'sugar_router'
    ],
    description='A asynchronous event router.',
    install_requires=[
        'sugar-asynctest@git+https://github.com/sugarush/sugar-asynctest@master'
    ]
)
