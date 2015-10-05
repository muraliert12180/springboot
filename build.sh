#!/usr/bin/env bash

rm -rf target
rm deploy/service.jar
rm -rf deploy/classes
mvn dependency:tree
mvn clean install
mvn package
cp target/myprojecls
t-0.0.1-SNAPSHOT-boot.jar deploy/service.jar