FROM ubuntu:20.04

WORKDIR /usr/src/app
ARG DEBIAN_FRONTEND=noninteractive
RUN chmod 777 /usr/src/app
RUN apt -qq update
RUN apt -qq install -y python3 python3-pip locales
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
RUN chmod +x bot.py
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

CMD ["bash","start.sh"]