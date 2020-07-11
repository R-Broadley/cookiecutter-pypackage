#!/bin/sh

function run_as_user {
		CONTAINER_USER="$(id -u):$(id -g)" \
		&& export CONTAINER_USER \
		&& docker-compose run --rm $@
}

case $OSTYPE in
  *linux*) run_as_user $@ ;;
  *)       docker-compose run --rm $@ ;;
esac
