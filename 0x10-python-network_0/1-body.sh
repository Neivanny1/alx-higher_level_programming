#!/bin/bash
# sends a GET request to a URL and displays the body of the response
curl -sL "$1" -X GET -H "Status: 200"
