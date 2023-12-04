from setuptools import setup, find_packages
import codecs
import os.path

with open("README.md") as file:
    long_description = file.read()

if os.path.isfile("./requirements.txt"):
    with open("./requirements.txt") as f:
        REQUIREMENTS = f.read().splitlines()


CLASSIFIERS = [
'Programming Language :: Python :: 3.9'
'Programming Language :: Python :: 3.10',
]

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

setup(name='dust2f1a',
version=get_version("dust2f1a/__init__.py"),
description='Converter tool to fix DUST output VTU files for\
reading with the meshio based method in pyF1A.',
long_description=long_description,
url='https://github.com/sfpullin/dust2f1a',
author='Shaun Pullin' ,
author_email='sp16189@bristol.ac.uk',
license='MIT',
classifiers=CLASSIFIERS,
install_requires=REQUIREMENTS,
packages=find_packages(exclude=("Examples",)),
keywords='',
entry_points={
    'console_scripts': [
        'dust2f1a = dust2f1a.cmd:main',
    ]
}
)

