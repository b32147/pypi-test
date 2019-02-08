import os
import re
import sys
from io import open

from setuptools import find_packages, setup


def read(f):
    return open(f, 'r', encoding='utf-8').read()


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.join(package, '__init__.py'))).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('pypitest')

setup(
    name='pypi-test',
    version=version,
    url='https://github.com/b32147/pypi-test',
    author='HMS DBMI Tech-core',
    author_email='dbmi-tech-core@hms.harvard.edu',
    packages=find_packages(exclude=['tests*']),
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    install_requires=[
        'requests',
        'furl',
    ],
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
