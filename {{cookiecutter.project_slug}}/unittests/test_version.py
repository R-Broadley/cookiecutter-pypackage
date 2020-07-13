"""Tests for `{{ cookiecutter.project_slug }}` package."""

from distutils.version import StrictVersion
from os import getcwd
from os.path import relpath

import pytest

import {{ cookiecutter.project_slug }}


# pylint: disable=protected-access
@pytest.mark.parametrize(
    "module",
    [{{ cookiecutter.project_slug }}, {{ cookiecutter.project_slug }}._version],
)
def test_version(module):
    """Check __version__ is a valid version number.

    Args:
        module (types.ModuleType): A module containing __version__

    """
    version = module.__version__
    full_path = module.__file__
    relative_path = relpath(full_path, start=getcwd())
    try:
        StrictVersion(version)
    except ValueError as exception:
        pytest.fail(msg=f"{exception} in {relative_path}")


def test_versions_match():
    """Ensure version in __init__ and _version match."""
    ver1 = {{ cookiecutter.project_slug }}.__version__
    # pylint: disable=protected-access
    ver2 = {{ cookiecutter.project_slug }}._version.__version__
    assert ver1 == ver2, "Version in __init__.py does not match _version.py"


def test_version_is_extractable():
    """Ensure version number can be extracted without importing package."""
    version_file = {{ cookiecutter.project_slug }}._version.__file__
    try:
        with open(version_file, "r") as vfile:
            value = vfile.readlines()[-1]
            version = value.split("=")[1].strip().strip('"')
    except Exception as exception:  # pylint: disable=broad-except
        pytest.fail(
            msg=f"Could not extract version from _version.py due to: `{exception}`"
        )
    msg = (
        "Version number imported from _version.py does not match that read from said "
        "file."
    )
    assert {{ cookiecutter.project_slug }}.__version__ == version, msg
