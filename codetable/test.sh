#!/bin/bash

echo $#
if [ $1 = "good" ] || [ $1 = "bad" ]; then
    echo "2 args"
fi
