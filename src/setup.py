#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name   ='NumpyToJson',
    version='0.1',
    author='Fernando Pujaico Rivera',
    author_email='fernando.pujaico.rivera@gmail.com',
    packages=['NumpyToJson'],
    #scripts=['bin/script1','bin/script2'],
    url='https://github.com/trucomanx/NumpyToJson',
    license='GPLv3',
    description='Creates a json from a numpy array',
    #long_description=open('README.txt').read(),
    install_requires=[
       "numpy" #"Django >= 1.1.1",
    ],
)

#! python setup.py sdist bdist_wheel
# Upload to PyPi
# or 
#! pip3 install dist/NumpyToJson-0.1.tar.gz 
