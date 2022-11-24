# Module 7 Documentation
## Create a production and development environment and deploy your final project to both environments.

### Tutorial for reference: https://cloud.google.com/deploy/docs/overview

1. git clone https://github.com/GoogleCloudPlatform/cloud-deploy-tutorials
2. Assure you have necessary APIs and credientials for deployment (IAM Roles)
3. Follow the below commands

gcloud deploy apply \
    --file=clouddeploy-config/delivery-pipeline.yaml
    
gcloud deploy delivery-pipelines \
    describe web-app
    
gcloud deploy releases create \
    web-app-001 \
    --delivery-pipeline web-app \
    --build-artifacts \
    web/artifacts.json --source web/

gcloud deploy rollouts list \
    --delivery-pipeline web-app \
    --release web-app-001

gcloud deploy targets describe \
    prod --delivery-pipeline web-app
    
gcloud deploy rollouts approve \
    web-app-001-to-prod-0001 \
    --delivery-pipeline web-app \
    --release web-app-001
    

