FROM python:3.9

ARG SECRET_KEY
ARG SENTRY_DSN
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG DJANGO_DEBUG

ENV SECRET_KEY=${SECRET_KEY}
ENV SENTRY_DSN=${SENTRY_DSN}
ENV AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
ENV AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
ENV DJANGO_DEBUG=${DJANGO_DEBUG}

WORKDIR /Python-OC-Lettings-FR

COPY . /Python-OC-Lettings-FR/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings
RUN python manage.py collectstatic --noinput
CMD ["gunicorn", "oc_lettings_site.wsgi", "--bind", "0.0.0.0:8000"]
