FROM python:3.12-alpine AS builder

COPY . /usr/src/kali
WORKDIR /usr/src/kali

RUN pip install poetry
RUN poetry env use python3.12
RUN poetry install

CMD [ "poetry", "run", "python", "kali/main.py" ]