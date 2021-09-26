#!/usr/bin/env bash
# this if loop looks for the holbertonschool file and determines its contents
if [[ -e "holbertonschool" ]]
then
    echo "holbertonschool file exits"
    
    if [[ -s  "holbertonschool" ]]
    then
        echo "holbertonschool file is not empty"
    else
        echo "holbertonschool file is empty"
    fi
    
    if [[ -f "holbertonschool" ]]
    then
        echo "holbertonschool is a regular file"
    fi
    
else
    echo "holbertonschool file does not exist"
fi