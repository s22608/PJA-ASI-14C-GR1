FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY src/ml-pipeline/requirements.txt .
RUN pip install -r requirements.txt
RUN pip install toposort

COPY src/ml-pipeline .

CMD ["kedro", "run"]
