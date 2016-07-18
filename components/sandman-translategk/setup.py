from distutils.core import setup

import setuptools

import sandman_translategk

setup(
    name='sandman-translategk',
    version=sandman_translategk.__version__,
    packages=setuptools.find_packages(exclude=['tests']),
    url='http://sandman.example.net',
    license='',
    author='PG-SanDMAN',
    author_email='awiens@mail.upb.de',
    description='',
    test_suite='tests',
    zip_safe=False,
    entry_points={
      'console_scripts': [
          'translategkd = sandman_translategk.translategk:daemon',
      ]   
    }   
)

