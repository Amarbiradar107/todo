FROM python:3.12-slim

WORKDIR /todo_app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "todo.wsgi:application", "--bind", "0.0.0.0:8000"]