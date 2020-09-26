import os
from distutils.core import setup
from setuptools import find_packages

os.chdir(os.path.normpath(os.path.dirname(__file__)))

setup(
    name='MicroCRM',
    version='0.1',
    description='Minimalistic Customer Relations Management software',
    author='',
    author_email='',
    url='',
    packages=find_packages(),
    python_requires='>3.5',
    install_requires=[
    ],
    extras_require={
    },
    scripts=[
    ]
)
