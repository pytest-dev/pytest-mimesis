from setuptools import setup

import pytest_elizabeth

setup(
    name='pytest-elizabeth',
    version=pytest_elizabeth.__version__,
    packages=['pytest_elizabeth'],
    url='https://github.com/lk-geimfari/pytest-elizabeth',
    license='MIT License',
    author='Likid Geimfari',
    author_email='likid.geimfari@gmail.com',
    description='Elizabeth integration with the pytest test runner',
    classifiers=[
        "Development Status :: 6 - Mature",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3"
    ],
    install_requires=[
        "elizabeth>=0.3.15",
        "pytest>=3.0.0"
    ],
    entry_points={
        'pytest11': [
            'elizabeth = pytest_elizabeth',
        ]
    },
    include_package_data=True
)
