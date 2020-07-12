SHELL := /bin/sh

SOURCES := $(shell find "{{ cookiecutter.project_slug }}" -name '*.py')
UNITTESTS := $(shell find "unittests" -name '*.py')
PYVER := $(shell python3 -c "from sys import version_info; print(f'{version_info.major}.{version_info.minor}')")

.PHONY:
	all
	image
	dist
	docs
	format
	lint
	shell
	test
	dev
	clean

all: test

image:
	./buildscripts/build_image.sh {{ cookiecutter.project_slug }}

dist: $(SOURCES) setup.py tox.ini image
	./buildscripts/start_container.sh {{ cookiecutter.project_slug }} tox -e wheel

docs: $(SOURCES) docs/conf.py tox.ini image
	./buildscripts/start_container.sh {{ cookiecutter.project_slug }} tox -e $@

format: $(SOURCES) tox.ini image
	./buildscripts/start_container.sh {{ cookiecutter.project_slug }} tox -e $@

lint: $(SOURCES) tox.ini image
	./buildscripts/start_container.sh {{ cookiecutter.project_slug }} tox -e $@

shell: image
	./buildscripts/start_container.sh --entrypoint /bin/bash {{ cookiecutter.project_slug }}

test: $(SOURCES) $(UNITTESTS) tox.ini image
	./buildscripts/start_container.sh {{ cookiecutter.project_slug }} tox

requirements.txt: setup.py
	./buildscripts/update_requirements_txt.py

dev: export PYVERSION=$(PYVER)
dev: requirements_dev.txt tox.ini
	tox -e devenv
	source .venv/bin/activate && pip install -U pip -r $<

clean:
	./buildscripts/clean.sh
