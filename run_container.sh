#!/bin/bash

source .env

# Connexion au registre Docker
docker login --username $DOCKERHUB_USERNAME --password $DOCKERHUB_PASSWORD

# Nom de l'image dans le registre
IMAGE_NAME=$DOCKERHUB_USERNAME/oc_lettings:latest

# Téléchargement de l'image depuis le registre
docker pull $IMAGE_NAME

# Lancer l'image en tant que conteneur
docker run -p 8000:8000 \
  -e SECRET_KEY=$SECRET_KEY \
  -e SENTRY_DSN=$SENTRY_DSN \
  -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
  -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
  -e AWS_STORAGE_BUCKET_NAME=$AWS_STORAGE_BUCKET_NAME \
  -e DJANGO_DEBUG=$DJANGO_DEBUG \
  $IMAGE_NAME
  