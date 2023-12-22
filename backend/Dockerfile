FROM python:3.9.13

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get -y install netcat && apt-get -y install gettext

COPY ./requirements.txt /opt/requirements.txt

RUN python -m pip install --upgrade pip
RUN pip install -r /opt/requirements.txt
RUN pip install django-mail-queue
RUN pip install django-rest-framework-nested==0.0.1
RUN pip install phonenumbers
WORKDIR /code
