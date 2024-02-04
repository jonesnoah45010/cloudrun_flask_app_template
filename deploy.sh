#!/bin/bash

SERVICE_NAME="NAME_OF_YOUR_SERVICE_HERE" # Define your service name here. Example "my-web-project"

PROJECT_NAME="YOUR_GCLOUD_PROJECT" # Define the project you created in the google cloud console

REGION="YOUR_PROJECT_REGION" # Define what region the project you created in the google cloud console is under. Example "us-east1"

# Step 1: Build and push the container image
gcloud builds submit --tag gcr.io/${PROJECT_NAME} /${SERVICE_NAME} .

# Step 2: Deploy the Cloud Run service 
gcloud run deploy ${SERVICE_NAME} \
    --image=gcr.io/${PROJECT_NAME}/${SERVICE_NAME} \
    --region=${REGION} \
    --allow-unauthenticated \
    --platform managed \
    --project ${PROJECT_NAME} \
    --quiet