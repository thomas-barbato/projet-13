# syntax=docker/dockerfile:1
FROM python:latest
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


COPY requirements.txt .

COPY requirements-dev.txt .

ENV SQLITE_URL=sqlite:///db/oc-lettings-site.sqlite3

RUN pip install -r requirements.txt

RUN pip install -r requirements-dev.txt

COPY . /projet-13/

WORKDIR /projet-13/

CMD ["python", "setup_env.py"]

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
