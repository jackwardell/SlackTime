# -*- coding: utf-8 -*-
from pathlib import Path

from setuptools import find_packages
from setuptools import setup

__version__ = "0.1.5"
ROOT_DIR = Path(".")

with open(str(ROOT_DIR / "README.md")) as readme:
    long_description = readme.read()

setup(
    name="slack_time",
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    author="Jack Wardell",
    author_email="jack@wardell.xyz",
    url="http://github.com/jackwardell/SlackTime/",
    description="A simple, intuitive and fast Slack API client for the Slack Web API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["requests >= 2.2"],
    test_suite="tests",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Office/Business",
        "Topic :: System :: Networking",
        "Topic :: Communications :: Chat",
        "Intended Audience :: Developers",
    ],
    keywords="slack api slack-web chat client post get message chatbots bots chatops",
    python_requires=">=3.5",
)
