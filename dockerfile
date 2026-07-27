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
#The next thing to keep in mind is virtualenv creation. We do not need it in Docker. It is already isolated. So, we use POETRY_VIRTUALENVS_CREATE=false or poetry config virtualenvs.create false setting to turn it off.
ENV POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_VIRTUALENVS_CREATE=false \
#Tells Poetry where to store downloaded files. 
#This is useful if you want to "mount" a folder from your host to speed up repeated builds.    
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
#Tells the system where to install the Poetry executable so you can run the poetry command from any folder.
    POETRY_HOME='/usr/local' \
    POETRY_VERSION=2.1.3

# Install Poetry
RUN pip install --no-cache-dir poetry==${POETRY_VERSION}

# Set working directory
WORKDIR /app

# Copy dependency files first (for layer caching)
COPY pyproject.toml poetry.lock /app/
#Reminder: The COPY [OPTIONS] <src> ... <dest> instruction copies new files or directories from <src> and adds them to the filesystem of the image at the path <dest>
# Install dependencies directly to system Python
RUN poetry install --no-root --no-directory

# Copy application code
COPY . /app

ENTRYPOINT ["python", "main.py"]

CMD ["pub"]