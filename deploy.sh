#!/bin/bash

apidoc -i /home/amir/opendatadb/api/code/ -o /home/amir/opendatadb/api/apidoc/
sudo cp -r /home/amir/opendatadb/api/apidoc/* /var/www/html
