#!/bin/sh

trolling=$((100 + RANDOM % 1000000000))

mkdir archives
cp database.txt archives/database-$trolling.txt
rm -rf database.txt
