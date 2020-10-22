FROM python:3.8

WORKDIR /src

COPY . .

CMD ["python", "./app.py"]
