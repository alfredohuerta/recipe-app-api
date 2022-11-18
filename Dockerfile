FROM python:3.9-alpine3.13
LABEL maintainer="Pantro"

ENV PYTHONUNBUFFERED 1

COPY ./requierments.txt /tmp/requierments.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requierments.txt && \
    rm -rf /tmp && \
    adduser \
        --disable-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user
