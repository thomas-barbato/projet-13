# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/engine/reference/builder/

#ARG PYTHON_VERSION=3.11.4
#FROM python:${PYTHON_VERSION}-slim as base
FROM python:latest
# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

FROM python:latest

COPY requirements.txt .

COPY requirements-dev.txt .

ENV SQLITE_URL=sqlite:///db/oc-lettings-site.sqlite3

RUN pip install -r requirements.txt

RUN pip install -r requirements-dev.txt

COPY . /projet-13/

WORKDIR /projet-13/

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
