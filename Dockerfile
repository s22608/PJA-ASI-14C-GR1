FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY src/ml-pipeline .
RUN apt-get update \
     && apt-get install -y build-essential \
    && apt-get install -y wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV CONDA_DIR /opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/sh ~/miniconda.sh -b -p /opt/conda
RUN conda install -c conda-forge gcc
RUN pip install -r requirements.txt
RUN pip install toposort

CMD ["kedro", "run"]
