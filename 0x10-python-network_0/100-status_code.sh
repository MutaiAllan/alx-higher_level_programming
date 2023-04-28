#!/bin/bash
# Displays the status code of the Response of a request to a URL.
curl -s -o /dev/null -w "%{http_code}" "$1"
