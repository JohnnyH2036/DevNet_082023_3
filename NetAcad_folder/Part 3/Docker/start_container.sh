#!/bin/bash

docker build -t apache_microservice .

docker run -d -p 85:80 --name apache_container apache_microservice
