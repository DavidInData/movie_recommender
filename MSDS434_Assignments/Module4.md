# Module 4 Documentation

## Create an ingest to ETL pipeline using CSV files and Google BigQuery. Schedule a recurring cron job to batch update the data.

### Tutorial Reference for Data Pipeline: https://cloud.google.com/dataflow/docs/guides/data-pipelines#create_a_batch_data_pipeline
### ----Specific Git Repository for this module --> https://github.com/DavidInData/module4.git -------

1. Create new project in GCP.
2. Click Activate Cloud Shell
3. Follow the commands below

glcoud projects list

gcloud config set project alsnewbigquery

rm -r data-science-on-gcp/ #removes the directory

git clone https://github.com/GoogleCloudPlatform/data-science-on-gcp

cd data-science-on-gcp

cd 02_ingest/

mkdir data

cp download.sh data
cd data

for MONTH in `seq 1 12`; do
bash download.sh 2015 $MONTH
done

cp 201501.csv 201501.bck
rm *csv
python

>>> f=open("201501.bck").readlines()
>>> f[0]

>>>> fout = open("201501.csv","w")
>>> for i in range(5000):
... 	fout.write(f[i])

fout.close()

4. To get out of python mode. Use the bellow keys
ctrl + z

cat 201501.csv

##bucket, create bucket davidtwonewbucket

gsutil -m cp *.csv gs://davidtwonewbucket   ## Write to bucket

bq mk davidtwosongcp

## gcloud config set project alsnewbigquery-XXXXX

bq load --autodetect --source_format=CSV alstwosongcp.flight_auto gs://davidtwonewbucket/201501.csv

## open bigquery


----Batch Data Pipeline https://github.com/DavidInData/module4.git -------

git clone https://github.com/DavidInData/module4.git

gsutil cp bq_three_column_table.json gs://davidtwonewbucket/text_to_bigquery/
gsutil cp split_csv_3cols.js gs://davidtwonewbucket/text_to_bigquery/
gsutil cp file01.csv gs://davidtwonewbucket/inputs/


