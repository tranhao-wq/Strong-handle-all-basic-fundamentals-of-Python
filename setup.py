#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="python-fundamentals-practice",
    version="1.0.0",
    author="Tran The Hao",
    author_email="your.email@example.com",
    description="Interactive desktop app for learning Python fundamentals",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tranthehao/python-fundamentals-practice",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "python-practice-gui=python_practice_gui:main",
            "python-practice-console=python_practice_app:main",
        ],
    },
)