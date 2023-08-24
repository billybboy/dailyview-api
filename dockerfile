FROM python:3.7-slim
LABEL maintainer="billybboy"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install psycopg2-binary && \
    apt-get purge -y --auto-remove libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/* && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol

ENV PATH="/py/bin:$PATH"

USER django-user