# Dockerfile for rabbitmq_tryout
# https://github.com/hallaj/rabbitmq_tryout

FROM  python:latest
COPY  requirements.txt  /tmp/requirements.txt
RUN   pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt
