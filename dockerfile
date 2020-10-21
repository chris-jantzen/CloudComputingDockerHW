FROM python:3.8

WORKDIR /src

COPY home /src/home

COPY app.py /src

CMD ["python", "./src/app.py"]
