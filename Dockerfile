# Base image
FROM ubuntu:16.04

# Maintainer
MAINTAINER mann.dhiman@gmail.com

# Copy the current directory content into the container at /Package
COPY . /Package

# Install package requirements
RUN apt-get -y update --fix-missing && apt-get install -y python-pip python-dev libev4 libev-dev gcc libxslt-dev libxml2-dev libffi-dev vim curl git

RUN pip install --upgrade pip

RUN apt-get install -y python-numpy python-scipy

RUN pip install -r /Package/requirements.txt

# Set the working directory to /Package
WORKDIR /Package

# Make port 5000 available to the world outside the container
EXPOSE 5000

# Entry point in the container for present example -
# Launch Flask web server
ENTRYPOINT ["python"]
CMD ["app/server.py"]

