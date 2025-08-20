FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app

RUN sed -i 's|http://deb.debian.org/debian|http://archive.debian.org/debian|g' /etc/apt/sources.list && \
    sed -i '/deb.debian.org/d' /etc/apt/sources.list && \
    apt-get update -o Acquire::Check-Valid-Until=false && \
    apt-get install -y awscli


RUN pip install -r requirements.txt
CMD ["python3","app.py"]