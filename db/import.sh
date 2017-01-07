#!/bin/bash

echo 'Importing JSON files ...'

mongoimport --db opendatadb --collection developers --file developers.json
mongoimport --db opendatadb --collection developersmetadata --file developers.metadata.json
mongoimport --db opendatadb --collection systems --file systems.json
mongoimport --db opendatadb --collection systemsmetadata --file systems.metadata.json
mongoimport --db opendatadb --collection tasks --file tasks.json
mongoimport --db opendatadb --collection tasksmetadata --file tasks.metadata.json

echo ''
echo 'Completed.'
