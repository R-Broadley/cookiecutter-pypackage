#!/usr/bin/env python
"""Run unit tests and generate an HTML report."""

from os.path import join as pathjoin
from sys import path, version_info
from unittest import defaultTestLoader

from HtmlTestRunner import HTMLTestRunner
from {{ cookiecutter.project_slug }} import __version__ as version


def main():
    """Write requirements.txt from setup.py."""
    testsuit = defaultTestLoader.discover("unittests")
    pyversion = f"{version_info.major}_{version_info.minor}"
    report_title = (
        f"{{ cookiecutter.project_name }} v{version} Unit Test Results",
        f"(Python {version_info.major}.{version_info.minor})",
    )
    report_title = " ".join(report_title)
    report_name = report_title.lower().replace(" ", "_").replace(".", "_")
    testrunner = HTMLTestRunner(
        report_name=report_name,
        report_title=report_title,
        combine_reports=True,
        output=pathjoin("reports", pyversion),
    )
    testrunner.run(testsuit)


if __name__ == "__main__":
    path.insert(0, "./")
    main()
