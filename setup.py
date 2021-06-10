from setuptools import find_packages, setup

PACKAGE_NAME = 'stelix'
VERSION = '1.0.1'

with open('README.rst', 'r') as readme:
    long_description = readme.read()

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author='iclapcheeks',
    python_requires='~=3.7',
    author_email='iclapcheeks@seized.us',
    description='A Python wrapper for the Sellix API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/iclapcheeks/Seltix',
    packages=find_packages(),
    install_requires=[
        'requests >=2.25.1, <3'
    ]
)
