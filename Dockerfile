FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /todo_app/todo

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn todo.wsgi:application --bind 0.0.0.0:8000

EXPOSE 8000
