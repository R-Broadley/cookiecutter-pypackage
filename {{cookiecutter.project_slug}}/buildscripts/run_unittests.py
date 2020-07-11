#!/usr/bin/env python
"""Run unit tests and generate an HTML report."""

from argparse import ArgumentParser
from importlib import import_module
from os.path import join as pathjoin
from sys import argv, path, version_info
from unittest import defaultTestLoader

from HtmlTestRunner import HTMLTestRunner


def runtests(package_name, package_path):
    """Run unit tests and generate HTML reports.

    Args:
        package_name (str): The name of the package to test
            (used to get version and for report titles).
        package_path (str): The path of the directory containing the package.

    """
    path.insert(0, package_path)
    test_package = import_module(package_name)
    pretty_name = package_name.replace("_", " ").title()
    testsuit = defaultTestLoader.discover("unittests")
    pyversion = f"{version_info.major}_{version_info.minor}"
    report_title = (
        f"{pretty_name} v{test_package.__version__} Unit Test Results",
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


def main(args):
    """Parse command line arguments and run unit tests.

    The required args are --name and --path. Use --help for more information.

    Args:
        args (list[str]): the command line arguments.

    """
    parser = ArgumentParser(
        description="Script to run unit tests and generate HTML reports",
    )
    parser.add_argument(
        "--name", type=str, required=True, help="the name of the package to test"
    )
    parser.add_argument(
        "--path",
        type=str,
        required=True,
        help="the path of the directory containing the package",
    )
    parsed_args = parser.parse_args(args)
    runtests(parsed_args.name, parsed_args.path)


if __name__ == "__main__":
    main(argv[1:])
