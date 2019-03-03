FROM python:3.6-alpine3.9

COPY /src /app

WORKDIR /app

RUN pip install beautifulsoup4 && pip install requests

ENTRYPOINT [ "python", "./main.py" ]