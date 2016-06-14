#!/usr/bin/env python
import os
from setuptools import setup

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
long_description = f.read()
f.close()

setup(
    name='redis timeseries',
    version='0.0.1',
    description='Python client for Redis key-value store',
    long_description=long_description,
    url='https://github.com/grinner/redis-timeseries-py',
    author='Nick Grinner',
    keywords=['Redis', 'key-value store', 'time series'],
    license='MIT',
    packages=['redistimeseries'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ]
)
