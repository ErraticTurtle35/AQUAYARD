FROM ubuntu
RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install flask
COPY app.py /opt/app.py
ENTRYPOINT FLASK_APP=app.py flask run --host=0.0.0.0