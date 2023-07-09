FROM jenkins/jenkins:latest

USER root

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Install Flask and black
RUN pip3 install flask black

USER jenkins