FROM python:3-alpine3.15

WORKDIR /app
COPY . /app

RUN pip install flask

# Expose Port
EXPOSE 5000

# Running Python Application
CMD python ./main.py