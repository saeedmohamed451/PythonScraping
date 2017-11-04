#!/usr/bin/bash

echo "Hello world"

if [ "$#" = 1 ]
then
  echo "Got input argument"
  echo $1
else
  echo "Got no arguments!"
fi
