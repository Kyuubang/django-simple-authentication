FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt update 

RUN pip install -U pip

WORKDIR /code

COPY . /code

RUN pip install -r requirements.txt

ENTRYPOINT ["sh", "entrypoint.sh"]
