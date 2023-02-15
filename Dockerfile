FROM python:3.9

ENV PYTHONBUFFEREDID 1
ENV PYTHONWRITEBYTECODE 1

WORKDIR /GraduationProject/

COPY requirements.txt /GraduationProject/

RUN pip install -r /GraduationProject/requirements.txt

ADD . .