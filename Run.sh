#!/bin/sh
#
#
#docker run -d --rm --name m2x --network sensor-network tmc05/m2x_svc
docker run -d --name m2x --network sensor-network -p 8081:8080 --volume /home/pi/Project/m2x_svc/credential:/credential --entrypoint ash -it --rm tmc05/m2x_svc 
