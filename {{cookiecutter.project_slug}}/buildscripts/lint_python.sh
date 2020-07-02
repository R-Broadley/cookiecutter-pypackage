#!/bin/sh

BUILDSCRIPTS="$(dirname "$0")"

source "$BUILDSCRIPTS/output_formatting.sh"

# Constants
PYLINT_FAIL=10

# Run pydocstyle
echo "Checking doc strings..."
pydocstyle
docstyle_result=$?
end_section "-"

# Run pylint and store score
echo "Running static analysis..."
pylint-fail-under --fail_under $PYLINT_FAIL setup.py {{ cookiecutter.project_slug }} unittests
pylint_result=$?

end_section "="

if [ $docstyle_result -ne 0 ] || [ $pylint_result -ne 0 ]
then
	echo "Package does not meet the required standard."
	if [ $docstyle_result -ne 0 ]
	then
		echo "Issues were found with docstrings."
	fi
	if [ $pylint_result -ne 0 ]
	then
		echo "The package's pylint score is too low."
	fi
else
	echo "Package meets the required standard."
fi
