FROM python:2.7.15
WORKDIR /tmp
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update 
RUN apt-get install vim -y
