#!/bin/sh

USER_UID=$(id -u)
USER_GID=$(id -g)

(
	export USER_UID USER_GID \
	&& docker-compose build $1
)
