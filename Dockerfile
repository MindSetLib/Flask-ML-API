FROM python:3.8

RUN apt-get update && \
    apt-get install -y openjdk-11-jre-headless && \
    apt-get clean

COPY . ./demonstration
WORKDIR ./demonstration

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT gunicorn --workers=1 --timeout=60 --bind 0.0.0.0:5000 app:app
