SHELL := /bin/sh

SOURCES := $(shell find "{{ cookiecutter.project_slug }}" -name '*.py')
UNITTESTS := $(shell find "unittests" -name '*.py')

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

dev: requirements.txt requirements_dev.txt tox.ini
	tox -e lint --devenv .venv
	source .venv/bin/activate && pip install -U pip -r $(word 2,$^) -r $<

clean:
	./buildscripts/clean.sh
