#!/bin/sh
git stash --all
git checkout deploy
git merge master
git push heroku deploy:master
git checkout master
git stash pop
