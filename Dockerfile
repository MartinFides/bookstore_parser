FROM python:3.11-slim-buster

RUN : \
	&& apt-get -y update \
	&& apt-get -y upgrade \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR "/home/python"

COPY ["requirements.txt", "."]

RUN : \
	&& python3 -m pip --no-cache-dir install -U pip setuptools wheel \
	&& python3 -m pip --no-cache-dir install -r "requirements.txt"

COPY ["app", "app"]

ENV PYTHONPATH="/home/python"

RUN : \
	&& useradd python \
	&& chown -R python:python "/home/python"

USER python

CMD ["python3", "/home/python/app/main.py"]
