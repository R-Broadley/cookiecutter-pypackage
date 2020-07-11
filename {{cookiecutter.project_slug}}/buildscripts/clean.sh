#!/bin/sh

function rm_if_dir {
	if [ -d "$1" ]
		then
			echo "removing '$1' (and everything under it)"
			rm -Rf "$1"
	fi
}

function rm_if_file {
	if [ -f "$1" ]
		then
			echo "removing '$1'"
			rm -f "$1"
	fi
}

rm_if_dir docs/_build
rm_if_dir reports
rm_if_dir .tox
rm_if_file requirements.txt
python setup.py clean --build --dist --eggs --pycache
