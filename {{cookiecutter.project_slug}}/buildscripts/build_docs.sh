#!/bin/sh

sphinx-apidoc --force --separate --module-first --no-toc \
	--output-dir docs/source/api $1
sphinx-build docs docs/_build
