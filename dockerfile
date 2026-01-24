FROM python:3.12.10-slim-bookworm

# Python
ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Poetry
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    #Tells Poetry where to store downloaded files. 
    #This is useful if you want to "mount" a folder from your host to speed up repeated builds.
    POETRY_CACHE_DIR='/var/cache/pypoetry' \ 
    #Tells the system where to install the Poetry executable so you can run the poetry command from any folder.
    POETRY_HOME='/usr/local' \
    POETRY_VERSION=1.8.3

# Install curl (to install poetry after)
RUN pip install --no-cache-dir poetry==1.8.3

WORKDIR /app

#We copy these first. If we change the code, Docker will reuse this cached layer
COPY pyproject.toml poetry.lock /app/

COPY . /app

CMD ["poetry", "run", "python", "main.py", "pub"]