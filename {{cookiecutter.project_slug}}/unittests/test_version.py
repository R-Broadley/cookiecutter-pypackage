"""Tests for `{{ cookiecutter.project_slug }}` package."""

from distutils.version import StrictVersion
from functools import partialmethod
from unittest import TestCase

import {{ cookiecutter.project_slug }}


class TestVersionInfo(TestCase):
    """Tests of package metadata format and consistency."""

    def check_version_format(self, version, file):
        """Check string is a valid version number.

        Args:
            version (str): The version string to check.
            file (str): the file which contains the version string.

        """
        try:
            StrictVersion(version)
        except ValueError as exception:
            self.fail(msg=f"{exception} in {file}")

    # pylint: disable=protected-access
    test_versionpy_version_format = partialmethod(
        check_version_format,
        {{ cookiecutter.project_slug }}._version.__version__,
        "package _version.py",
    )

    test_init_version_format = partialmethod(
        check_version_format,
        {{ cookiecutter.project_slug }}.__version__,
        "package __init__.py",
    )

    def test_versions_match(self):
        """Ensure version in __init__ and _version match."""
        self.assertEqual(
            {{ cookiecutter.project_slug }}._version.__version__,
            {{ cookiecutter.project_slug }}.__version__,
            msg="Version in __init__.py does not match _version.py",
        )

    # pylint: enable=protected-access

    def test_version_is_extractable(self):
        """Ensure version number can be extracted without importing package."""
        version_file = "{{ cookiecutter.project_slug }}/_version.py"
        try:
            with open(version_file, "r") as vfile:
                value = vfile.readlines()[-1]
                version = value.split("=")[1].strip().strip('"')
        except Exception as exception:  # pylint: disable=broad-except
            self.fail(
                msg=f"Could not extract version from _version.py due to: `{exception}`"
            )

        self.check_version_format(version, "_version.py (text extraction)")
        self.assertEqual(
            {{ cookiecutter.project_slug }}.__version__,
            version,
            msg=(
                "Version number imported from _version.py does not match that "
                "read from said file."
            ),
        )
