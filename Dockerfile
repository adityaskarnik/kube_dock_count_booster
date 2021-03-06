# Download base image ubuntu 18.04
FROM ubuntu:20.04

# Most important of all give this your own name
MAINTAINER adityakarnik

ARG DEBIAN_FRONTEND=noninteractive

# This will give you all the latest updates and required packages to start
RUN apt-get update \
    && apt-get install -my wget gnupg \
    && apt-get install -y --no-install-recommends \
        apt-utils \
        ca-certificates \
        apt-transport-https \
        jq \
        numactl \
&& rm -rf /var/lib/apt/lists/*

RUN apt-get update

# Installing python and its dependencies
RUN apt-get install -y python3-pip python-dev build-essential

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

RUN apt-get install -y ./google-chrome-stable_current_amd64.deb

# Copy the local folder of your app to docker container
# Consider this app folder in placed in the same folder as your Dockerfile
COPY app/ /app

# Navigate to yoru app directory
WORKDIR /app

# for requirements to work
RUN apt-get install -y gdal-bin

# Install you application dependencies
RUN pip install -r requirements.txt

# This will the command run when you start your container
ENTRYPOINT ["python3"]

# Like "python app.py", this will run when you start your container
CMD ["open_urls.py"]
