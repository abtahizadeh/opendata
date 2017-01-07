#!/bin/bash

elasticsearch -H 0.0.0.0 &
echo '>>> Running Kibana ...'
kibana -H 0.0.0.0 &
