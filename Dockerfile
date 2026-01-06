FROM python:3.12-slim

WORKDIR /usr/src/app

COPY main.py .

CMD ["python", "main.py"]
