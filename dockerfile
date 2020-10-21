FROM python:3.8

WORKDIR /code

# COPY ...textfiles

COPY . .

CMD ["python", "./app.py"]
