#!/bin/bash

# Set CSS
sudo cp /var/www/html/css/style.css.bak /var/www/html/css/style.css

# Run MongoDB engine
# mongod --dbpath opendatadb/data &

# Run the server
cd /home/amir/opendatadb/api/code
python server.py
