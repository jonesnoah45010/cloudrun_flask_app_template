@echo off
SET SERVICE_NAME=NAME_OF_YOUR_SERVICE_HERE
SET PROJECT_NAME=YOUR_GCLOUD_PROJECT
SET REGION=YOUR_PROJECT_REGION

REM Step 1: Build and push the container image
gcloud builds submit --tag gcr.io/%PROJECT_NAME%/%SERVICE_NAME% .

REM Step 2: Deploy the Cloud Run service
gcloud run deploy %SERVICE_NAME% ^
    --image=gcr.io/%PROJECT_NAME%/%SERVICE_NAME% ^
    --region=%REGION% ^
    --allow-unauthenticated ^
    --platform managed ^
    --project %PROJECT_NAME% ^
    --quiet
