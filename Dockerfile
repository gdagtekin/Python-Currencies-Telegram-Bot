FROM python:3.11-slim

WORKDIR /app

COPY . /app/

RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

CMD ["pipenv", "run", "python", "CurrenciesBot.py"]