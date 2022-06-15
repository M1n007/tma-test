FROM ubuntu:18.04

RUN apt-get update -y

RUN apt-get install -y \
    libsm6 \
    libxext6 \
    python3-pip \
    python3 \
    build-essential

COPY . /app
WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["server.py"]