#!/bin/bash
# script that takes in a URL, sends a POST request to the passed URL
curl -s -X POST "$1" -d "email=test@gmail.com&subject=I will always to be here for PLD"
