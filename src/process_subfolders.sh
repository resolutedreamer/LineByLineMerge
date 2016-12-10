#!/bin/bash

for $directory in */ ; do
    echo "$directory"
    python LineByLineMerge.py $directory
done

