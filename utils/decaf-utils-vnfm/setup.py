from setuptools import setup, find_packages

setup(
    name='decaf-utils-vnfm',
    version='0.1.0-dev4',
    packages=find_packages(exclude=['tests']),
    url='',
    license='',
    author='thgoette',
    author_email='thgoette@mail.upb.de',
    description='Infaces for VNF Management + basic implementations',
    test_suite='tests',
    zip_safe=False
)
