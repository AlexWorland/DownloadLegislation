# dockerfile to run a python script

FROM python:latest

RUN apt update && apt install -y wget

COPY . /app

WORKDIR /app

CMD ["python3", "/app/download.py"]
