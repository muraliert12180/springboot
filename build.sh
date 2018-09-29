#!/usr/bin/env bash

rm -rf target
rm deploy/service.jar
mvn dependency:tree
mvn clean install
mvn package
cp target/myproject-0.0.1-SNAPSHOT-boot.jar deploy/service.jar
