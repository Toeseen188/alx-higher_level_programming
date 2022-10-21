#!/bin/bash
# send a request to webserve to display all the METHODS allowed
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
