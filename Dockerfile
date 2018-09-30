FROM ubuntu:16.04

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH
RUN apt-get update --fix-missing
RUN apt-get install -y curl bzip2

RUN curl -fSL https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh -o ~/anaconda.sh
RUN /bin/bash ~/anaconda.sh -b -p /opt/conda

WORKDIR /home
COPY . .

CMD jupyter notebook --ip=0.0.0.0 --allow-root