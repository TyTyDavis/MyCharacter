FROM python:3.10-slim

WORKDIR /code

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

COPY ./requirements /code/requirements

RUN pip install --upgrade pip pip-tools \ 
    && pip-sync requirements/*.txt

COPY . /code

EXPOSE 8000

ENV PYTHONPATH /code

CMD ["python", "manage.py", "runserver" "8000"]