FROM python:3.10

WORKDIR /opt/demo_duplicate_counter

ARG YOUR_ENV

ENV YOUR_ENV=${YOUR_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.1 \
  PYTHONPATH="${PYTHONPATH}:./"

RUN pip install "poetry==$POETRY_VERSION"

# in order to optimize rebuilding
COPY pyproject.toml .
COPY poetry.lock .
COPY fixture.py .

RUN poetry config virtualenvs.create false  \
    && poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

COPY . .
