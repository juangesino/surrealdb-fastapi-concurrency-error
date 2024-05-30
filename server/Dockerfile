FROM python:3.11.4-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -qq -y \
  gcc build-essential libpq-dev git make ca-certificates libicu-dev libzbar-dev pkg-config --fix-missing --no-install-recommends \ 
  && apt-get clean

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && \
  pip install -r requirements.txt

COPY ./app /app

CMD uvicorn main:app --reload --host 0.0.0.0 --port 5057 --proxy-headers