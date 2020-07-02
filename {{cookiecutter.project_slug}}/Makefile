SOURCES := $(shell find "{{ cookiecutter.project_slug }}" -name '*.py')

.PHONY:
	all
	dist
	dev
	docs
	format
	lint
	image
	shell

all: dist docs

dist: $(SOURCES) setup.py
	./buildscripts/build_package.sh

dev: requirements.txt requirements_dev.txt
	pip install -r requirements_dev.txt

requirements.txt: setup.py
	./buildscripts/update_requirements_txt.py

docs: $(SOURCES) docs/conf.py
	./buildscripts/build_docs.sh {{ cookiecutter.project_slug }}

format:
	./buildscripts/format_python.sh

lint:
	./buildscripts/lint_python.sh

image: requirements.txt requirements_dev.txt
	./buildscripts/build_image.sh {{ cookiecutter.project_slug }}

shell: image
	./buildscripts/start_container.sh --entrypoint /bin/bash {{ cookiecutter.project_slug }}
