FROM python:3.7-alpine
MAINTAINER Angel Resendiz

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-libs postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev python3-dev linux-headers musl-dev postgresql-dev 
RUN pip install -r requirements.txt --no-cache-dir
RUN apk --purge del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app


RUN adduser -D user
USER user

