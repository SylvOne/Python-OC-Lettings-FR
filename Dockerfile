FROM python:3.9

WORKDIR /Python-OC-Lettings-FR

COPY . /Python-OC-Lettings-FR/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings
RUN python manage.py collectstatic --noinput
CMD ["gunicorn", "oc_lettings_site.wsgi", "--bind", "0.0.0.0:8000"]
