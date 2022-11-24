# Module 2 Documentation
## Demonsrate a project creation (either following the provided demo or a project of your own choosing) , pushing to a github repository , followed by editing your project and pushing updates back to github. You need to demonstrate this capability on both the Google Cloud Platform and Amazon Web Service EC2

### GCP & AWS

1. Follow steps in Module 1 to successfully create an instance (GCP or AWS).
2. Navtigate to the SSH in the instance.
3. Use the following commands

sudo apt update
sudo apt install git
git clone https://github.com/palomasoftware/MSDS434_ModuleTwo.git

This will clone the demo files into the instance. The below commands will push changes and make modifications to my personal github.

git init
git add README.md
git config --global user.email "davidindata@gmail.com"
git config --global user.name "david"
git commit -m "first commit"
git branch -M main
git remote remove origin
git remote add origin https://davidindata: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@github.com/DavidInData/MSDS_experiment.git
vi test2.py

git add test2.py
git commit -m "commit"
git push -u origin main

The repository for this demo is https://github.com/DavidInData/MSDS_AWS

