# Module 8 Documentation

## Use the Google Cloud Platform Billing API and create a cost forecast using BigQuery ML.

### Additional tutorial/documentation https://cloud.google.com/billing/docs/reference/rest https://cloud.google.com/billing/docs/how-to/export-data-bigquery-setup

1. To export Cloud Billing data to BigQuery, take the following steps:
2. Create a project where the Cloud Billing data will be stored, and enable billing on the project (if you have not already done so).
3. Configure permissions on the project and on the Cloud Billing account.
4. Enable the BigQuery Data Transfer Service API (required to export your pricing data).
5. Create a BigQuery dataset in which to store the data.
6. Enable Cloud Billing export of cost data and pricing data to be written into the dataset.
7. In BigQuery ML, you should see a Dataset that provides overview of billing/costs.

Alternatively, you can also view Billing Dashboard and enable notifications.
