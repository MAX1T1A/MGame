FROM python:3.12

WORKDIR /code

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock /code/
RUN poetry config virtualenvs.create false && poetry install --only main

COPY ./src/app /code/src/app
ENV PYTHONPATH=/code/src:/code/src/app

WORKDIR /code/src

CMD uvicorn app:app --host $APP_HOST --port $APP_PORT
