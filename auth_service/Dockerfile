FROM hub.hamdocker.ir/python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy poetry files
COPY pyproject.toml poetry.lock* ./

# Install Poetry
RUN pip install poetry

# Disable virtualenv creation by Poetry
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-root

# Copy app code
COPY app ./app

# Start the FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
