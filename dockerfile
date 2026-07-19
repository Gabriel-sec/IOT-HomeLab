FROM python:3.12.10-slim-bookworm

# Fix for OS vulnerabilities (glibc, etc.)
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Application Default Environment Variables
ENV BROKER_ADDRESS="host.docker.internal" \
    BROKER_PORT="1883" \
    TOPIC="python/mqtt"

# Python
ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local' \
    POETRY_VERSION=2.1.3

# Install Poetry
RUN pip install --no-cache-dir poetry==${POETRY_VERSION}

# Set working directory
WORKDIR /app

# Copy dependency files first (for layer caching)
COPY pyproject.toml poetry.lock /app/

# Install dependencies directly to system Python
RUN poetry install --no-root --no-directory

# Copy application code
COPY . /app

ENTRYPOINT ["python", "main.py"]

CMD ["pub"]