FROM python:3.7.2
WORKDIR /tmp
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update 
RUN apt-get install vim -y