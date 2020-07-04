#!/usr/bin/env python
"""Run unit tests and generate an HTML report."""

from sys import path
from unittest import defaultTestLoader

from HtmlTestRunner import HTMLTestRunner


def main():
    """Write requirements.txt from setup.py."""
    testsuit = defaultTestLoader.discover("unittests")
    testrunner = HTMLTestRunner()
    testrunner.run(testsuit)


if __name__ == "__main__":
    path.insert(0, "./")
    main()
