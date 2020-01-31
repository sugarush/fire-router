__author__ = 'Paul Severance'

from setuptools import setup

setup(
    name='fire-router',
    version='0.0.1',
    author='Paul Severance',
    author_email='paul.severance@gmail.com',
    url='https://github.com/sugarush/fire-router',
    packages=[
        'fire_router'
    ],
    description='A lightweight event router.',
    install_requires=[
        'fire_asynctest'
    ],
    dependency_links=[
        'git+https://github.com/sugarush/fire-asynctest@master#egg=fire-asynctest'
    ]
)
