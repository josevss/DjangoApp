# #Docker filr is a list of instruction used to create a docker
# #hyper-v is a microsoft technology to create virtula operating system
# FROM python:3.7-alpine
# MAINTAINER Josekurian
#
# ENV PYTHONUNBUFFERED 1
#
# COPY ./requirements.txt /requirements.txt
# RUN pip install -r /requirements.txt
#
# RUN mkdir /app   #create empty folder with name app
# WORKDIR /app  #switches to default root directory
# COPY ./app /app
#
# #RUN adduser -D jouser
# #USER jouser    #if this is not created then it will use the root account of docker
#
#
# #get docker-compose --version
#
#
# #poershell enable the virtulaiztion enable   link -  Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
# #refrence link - https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v
#
#
# #to enable docker we have to enable the visualtization
# #to build in docker- docker build .




FROM python:3.7-alpine
MAINTAINER London App Developer Ltd.

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Setup directory structure
RUN mkdir /app
WORKDIR /app
COPY ./app/ /app
