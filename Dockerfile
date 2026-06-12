FROM python:3.15.0b2-bookworm
LABEL authors="amar biradar"

ENV PYTHONUNBUFFERED=1

WORKDIR /todo_app/todo

COPY reqirement.txt reqirement.txt

RUN pip install -r reqirement.txt

COPY . .

CMD gunicorn todo.wsgi:application --bind 0.0.0.0:8000

EXPOSE 8000
