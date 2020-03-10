FROM python:3.7.3
RUN pip install --upgrade pip
RUN apt update \
    && apt install -y --no-install-recommends python3 python3-pip \
    && rm -rf /var/lib/apt/lists/*
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
ADD backend/requirements.txt /code/
WORKDIR /code/
RUN pip install -r requirements.txt
ADD backend /code/
