FROM python:3.12.10-slim-bookworm

# Fix for OS vulnerabilities (glibc, etc.)
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Python
ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Poetry
ENV POETRY_NO_INTERACTION=1 \
    #The next thing to keep in mind is virtualenv creation. We do not need it in Docker. It is already isolated. So, we use POETRY_VIRTUALENVS_CREATE=false or poetry config virtualenvs.create false setting to turn it off.
    POETRY_VIRTUALENVS_CREATE=false \
    #Tells Poetry where to store downloaded files. 
    #This is useful if you want to "mount" a folder from your host to speed up repeated builds.
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    #Tells the system where to install the Poetry executable so you can run the poetry command from any folder.
    POETRY_HOME='/usr/local' \
    POETRY_VERSION=2.1.3

# Install curl (to install poetry after)
RUN pip install --no-cache-dir poetry==${POETRY_VERSION}

#WORKDIR instruction is used to set the working directory for all the subsequent Dockerfile instructions. Default path is /
WORKDIR /app

#We copy these first. If we change the code, Docker will reuse this cached layer. We want to cache our requirements and only reinstall them when pyproject.toml or poetry.lock files change. Otherwise builds will be slow. To achieve working cache layer we should put:
COPY pyproject.toml poetry.lock /app/
#Reminder: The COPY [OPTIONS] <src> ... <dest> instruction copies new files or directories from <src> and adds them to the filesystem of the image at the path <dest>
COPY . /app

CMD ["poetry", "run", "python", "main.py", "sub"]