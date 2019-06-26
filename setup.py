__author__ = 'Lucifer Avada'

from setuptools import setup

setup(
    name='sugar-router',
    version='0.0.1',
    author='Lucifer Avada',
    author_email='lucifer.avada@gmail.com',
    url='https://github.com/sugarush/sugar-router',
    packages=[
        'sugar_router'
    ],
    description='A lightweight event router.',
    install_requires=[
        'sugar_asynctest'
    ],
    dependency_links=[
        'git+https://github.com/sugarush/sugar-asynctest@master#egg=sugar-asynctest'
    ]
)
