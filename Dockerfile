FROM python:3.11-slim

RUN pip install flask
COPY . /app
WORKDIR /app
CMD ["python", "-c", "print('hello')"]
