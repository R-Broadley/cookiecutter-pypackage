#!/bin/sh

function rm_if_dir {
	if [ -d "%1" ]
		then
			rm -Rf "$1"
	fi
}

python setup.py clean --build --dist --eggs --pycache
rm_if_dir docs/_build
rm_if_dir reports
