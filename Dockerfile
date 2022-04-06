# Dockerfile

# pull the official docker image
FROM python:3

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install dependencies
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY . .
