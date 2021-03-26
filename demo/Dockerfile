FROM python:alpine

WORKDIR /opt/app

COPY . .

RUN apk add -u --no-cache tzdata gcc musl-dev linux-headers\
    libffi-dev postgresql-dev && \
    pip install -r requirements.txt

ENV PORT=8080

ENTRYPOINT ["/bin/sh","launch.sh"]