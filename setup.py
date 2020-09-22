# -*- coding: utf-8 -*-
from pathlib import Path

from setuptools import setup

__version__ = "0.1.0"
ROOT_DIR = Path(".")

with open(ROOT_DIR / "README.md") as readme:
    long_description = readme.read()

setup(
    name="slack_time",
    version=__version__,
    packages=["slack_time"],
    include_package_data=True,
    author="Jack Wardell",
    url="http://github.com/jackwardell/SlackTime/",
    description="A simple, intuitive and fast Slack API client for the Slack Web API",
    long_description=long_description,
    install_requires=["requests >= 2.2"],
    test_suite="tests",
    classifiers=[
        "Natural Language :: English",
        "Topic :: Office/Business",
        "Topic :: System :: Networking",
        "Topic :: Communications :: Chat",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="slack api slack-web chat client post get message chatbots bots chatops",
)