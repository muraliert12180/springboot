#!/usr/bin/env bash

git checkout builds
rm -rf deploy
git checkout master -- deploy
git checkout master -- src
git checkout master -- pom.xml
git checkout master -- build.sh

./build.sh
rm -rf target
rm -rf src
rm pom.xml
rm build.sh

git add .
git add -u
git commit -m 'build'
git push origin builds
#git checkout master