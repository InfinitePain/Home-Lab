# Name: tf-streamlink:1.0.24
# Description: Dockerfile for Threadfin with Streamlink

FROM fyb3roptik/threadfin:1.2.9

# Packages for Streamkink
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y python3 \
                       python3-pip \
                       python3-venv \
                       libxml2-dev \
                       libxslt-dev

# Install Streamlink
RUN python3 -m pip install --upgrade setuptools \
                                     wheel \
                                     versioningit \
                                     certifi \
                                     isodate \
                                     pycountry \
                                     pycryptodome \
                                     pysocks \
                                     requests \
                                     trio \
                                     trio-websocket \
                                     typing_extensions \
                                     urllib3 \
                                     websocket-client \
                                     streamlink
