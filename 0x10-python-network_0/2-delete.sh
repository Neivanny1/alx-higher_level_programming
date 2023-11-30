#!/bin/bash
# sends a DELETE request to a URL and displays the body of the response
curl -s "$1" -X DELETE -H "$1"
