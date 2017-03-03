from setuptools import setup

import pytest_mimesis

setup(
    name='pytest-mimesis',
    version=pytest_mimesis.__version__,
    packages=['pytest_mimesis'],
    url='https://github.com/lk-geimfari/pytest-mimesis',
    license='MIT License',
    author='Likid Geimfari',
    author_email='likid.geimfari@gmail.com',
    description='Mimesis integration with the pytest test runner',
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
        "mimesis>=0.0.5",
        "pytest>=3.0.0"
    ],
    entry_points={
        'pytest11': [
            'mimesis = pytest_mimesis',
        ]
    },
    include_package_data=True
)
