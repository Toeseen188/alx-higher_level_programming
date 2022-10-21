#!/usr/bin/bash
# Bash script that takes in a URL as an argument, sends a GET
# request to the URL, and displays the body of the response
# * A header variable X-School-User-Id must be sent with the value 98
# * You have to use curl
curl -s -header "X-School-User-Id:98" "$1"
