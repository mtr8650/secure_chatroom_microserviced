FROM hub.hamdocker.ir/python:3.11-slim

WORKDIR /app

COPY pyproject.toml poetry.lock* ./
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

COPY app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
