#!/bin/bash

repo_name= 'workflows-test1'

repo_link='git@github.com:revanth-itv/workflows-test1.git'


if ls -Fa | grep -q '.git/'
	if git config --get remote.origin.url | grep -q "$repo_name"
	then
		git pull
	fi
else
	git init
	git remote add origin "$repo_link"
	git pull origin master
then
	echo "done"
fi
