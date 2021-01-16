ARG IMAGE=containers.intersystems.com/intersystems/iris-ml:2020.3.0.304.0
FROM $IMAGE
USER root   

RUN \
  apt-get update && \
  apt-get -y install nano
  
RUN \
  apt-get update && \
  apt-get -y install python3 python3-pip

WORKDIR /opt/irisapp
RUN chown ${ISC_PACKAGE_MGRUSER}:${ISC_PACKAGE_IRISGROUP} /opt/irisapp

USER ${ISC_PACKAGE_MGRUSER}

# COPY  Installer.cls .
COPY  stream/* /usr/irissys/mgr/stream/
COPY  python/* /usr/irissys/mgr/python/
COPY  src src 
COPY  iris.key /usr/irissys/mgr/
COPY  module.xml module.xml
COPY  iris.script /tmp/iris.script

RUN iris start IRIS \
	&& iris session IRIS < /tmp/iris.script \
    && iris stop IRIS quietly
