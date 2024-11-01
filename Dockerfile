
FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN invalid_command

EXPOSE 5000

CMD ["python", "app.py"]
