FROM python:3.6.10


# installing libs
RUN apt update -y &&\
    apt install -y python3-numpy unixodbc unixodbc-dev libodbc1 \
                   build-essential cmake ffmpeg libsm6 libxext6 &&\
    pip3 install --upgrade pip

WORKDIR /app

CMD ["bash","-c","service postgresql start"]

EXPOSE 5000

ARG DB_NAME

ENV ENV_NAME=staging \
    ALLOWED_HOSTS=* \
    DB_NAME=${DB_NAME} \
    APPLICATION_PORT=${APPLICATION_PORT}

# instaling dependencies
COPY requirements.txt requirements-dev.txt ./
RUN pip3 install -r requirements.txt

COPY . .

# generating SECRET KEY
RUN mv .env.example .env
