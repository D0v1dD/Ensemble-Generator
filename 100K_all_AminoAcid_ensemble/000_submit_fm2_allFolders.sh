#!/bin/bash

for i in $( ls -1d 001_* ) ; do
    cd $i
    pwd
    sh submit_fm2.sh
    cd ..
done
