# Module 5 Documentation

## Return an aggregated result with a machine-learning (ML) prediction using Google BigQuery ML and serve out results using Google App Engine.


### The following Example creates a web-service for the IRIS Dataset fore prediction
docker run -p 8500:8500 --network="host" --mount type=bind,source=`pwd`/tmp_dir/test,target=/models/iris_model -e MODEL_NAME=iris_model -t tensorflow/serving &

curl -d '{"instances": [{"sepal_length":5.0, "sepal_width":2.0, "petal_length":3.5, "petal_width":1.0}]}' -X POST http://localhost:8501/v1/models/iris_model:predict

### The following example provides SQL in BigQuery to train a model with validation using Google analytics sample
### The following article for reference: https://towardsdatascience.com/introduction-to-bigquery-ml-e746a3eaa28d

select * from `bigquery-public-data.google_analytics_sample.ga_sessions_*`

##create dataset davidsdataset

#standardSQL
CREATE MODEL `davidsdataset.sample_model14`
OPTIONS(model_type='logistic_reg',
       input_label_cols=['isBuyer'])
AS
SELECT
 IF(totals.transactions IS NULL, 0, 1) AS isBuyer,
 IFNULL(totals.pageviews, 0) AS pageviews,
 IFNULL(totals.timeOnSite, 0) AS timeOnSite,
 IFNULL(totals.newVisits, 0) AS isNewVisit,
 IF(device.deviceCategory = 'mobile', 1, 0) AS isMobile,
 IF(device.deviceCategory = 'desktop', 1, 0) AS isDesktop,
 IF(trafficSource.medium in ('affiliate', 'cpc', 'cpm'), 1, 0) AS isPaidTraffic
FROM
 `bigquery-public-data.google_analytics_sample.ga_sessions_*`
WHERE
 _TABLE_SUFFIX BETWEEN '20160801' AND '20160901'


#test set
SELECT *
FROM ML.EVALUATE(MODEL `davidsdataset.sample_model14`,
   (
     SELECT
        IF(totals.transactions IS NULL, 0, 1) AS isBuyer,
        IFNULL(totals.pageviews, 0) AS pageviews,
        IFNULL(totals.timeOnSite, 0) AS timeOnSite,
        IFNULL(totals.newVisits, 0) AS isNewVisit,
        IF(device.deviceCategory = 'mobile', 1, 0) AS isMobile,
        IF(device.deviceCategory = 'desktop', 1, 0) AS isDesktop,
        IF(trafficSource.medium in ('affiliate', 'cpc', 'cpm'), 1, 0) AS isPaidTraffic
     FROM
        `bigquery-public-data.google_analytics_sample.ga_sessions_*`
     WHERE
        _TABLE_SUFFIX BETWEEN '20170701' AND '20170801'
   ),
   STRUCT(0.5 AS threshold)
   )

#standardSQL
SELECT *
FROM ML.PREDICT(MODEL `davidsdataset.sample_model14`,
   (
     SELECT
        IFNULL(totals.pageviews, 0) AS pageviews,
        IFNULL(totals.timeOnSite, 0) AS timeOnSite,
        IFNULL(totals.newVisits, 0) AS isNewVisit,
        IF(device.deviceCategory = 'mobile', 1, 0) AS isMobile,
        IF(device.deviceCategory = 'desktop', 1, 0) AS isDesktop,
        IF(trafficSource.medium in ('affiliate', 'cpc', 'cpm'), 1, 0) AS isPaidTraffic
     FROM
        `bigquery-public-data.google_analytics_sample.ga_sessions_*`
     WHERE
        _TABLE_SUFFIX BETWEEN '20170701' AND '20170801'
   )
   )



