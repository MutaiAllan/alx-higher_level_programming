#!/bin/bash
# Makes a request that causes the server respond with a message 'You got me!'.
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
