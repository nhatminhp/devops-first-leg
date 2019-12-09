FROM python:3.7-slim

COPY . /srv/flask-jwt-auth
WORKDIR /srv/flask-jwt-auth

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install nginx
RUN apt-get -y install python3-dev \
    && apt-get -y install build-essential \
    && apt-get -y install default-libmysqlclient-dev

#RUN pip3 install virtualenv
#
#RUN virtualenv -p python3 venv
#
#RUN /bin/bash -c "source ./venv/bin/activate"

RUN pip install -r requirements.txt

COPY ./nginx/nginx.conf /etc/nginx
RUN chmod +x ./startup.sh
CMD ["./startup.sh"]