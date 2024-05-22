FROM ubuntu:18.04
ADD . /app
WORKDIR /app
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:9595"]