FROM python:3.9-slim

WORKDIR /app

COPY app.py /app

RUN pip install mysql-connector-python

ENV MYSQL_HOST=mysql
ENV MYSQL_USER=sample
ENV MYSQL_PASSWORD=password
ENV MYSQL_DB=test

CMD ["python", "app.py"]
