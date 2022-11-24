# Module 3 Documentation
## Create a “hello world” pipeline to Google Cloud that calls into a Python-based Google App Engine (GAE) project and returns “hello world” as a JavaScript Object Notation (JSON) response.

1. Create new project in GCP
2. Follow the below commands

<<---In Clould Shell--->>
gcloud projects list

//if want to remove
rm -r "NAME_OF_DIRECTORY"

gcloud config set project newproject-364813
git clone https://github.com/GoogleCloudPlatform/python-docs-samples

cd python-docs-samples/
cd appengine/
cd standard_python3/
cd hello_world/
cat app.yaml
cat main.py

#enable App Engine Admin API

gcloud app deploy app.yaml

#Naviguate to IAM & Admin

gcloud projects describe demo3-364815

demo3-364815

 -->https://demo3-364815.uc.r.appspot.com/


gsutil cp -r gs://dthor1/iris tmp_dir

cp -r tmp_dir/iris/* serving_dir/iris_model/1

curl -d '{"instances": [{"sepal_length":5.0, "sepal_width":2.0, "petal_length":3.5, "petal_width":1.0}]}' -X POST http://localhost:8501/v1/models/iris_model:predict

MODEL_DIR="gs://dthor1/iris"
VERSION_NAME="v1"
FRAMEWORK="TENSORFLOW"
