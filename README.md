#  DM-Amazon Fine Food Reviews

This project is a recommendor based on food reviews from Amazon.

## Prerequisite 

* Python > 3.6
* Pandas
* nltk
* vaderSentiment
* Jupyter-notebook

## Getting Started

* dataset can be downloaded from the following link:
https://docs.google.com/document/d/1Kant1WYF7grgqUE1yo8zhRubtdrajtU31K-C7Zlbwkc/edit?usp=sharing

* Extract the downloaded file under the root directory of this folder.

* Run sa.py to construct and save Sentiment Analysis result, Reviews_sa.csv

* Run each block in Preprocessing.ipynb to get:
    * bucket_test_vip5.csv
    * bucket_test.csv
    * bucket_train_vip5.csv
    * bucket_train.csv
    * bucket.csv
    * Ratings_vip_moderateS.csv
    * Ratings_vip_sa.csv
    * Ratings_vip.csv
    * Ratings_vip5_sa.csv
    * Ratings_vip5.csv

* Run AssociationRule.ipynb and PMF.inpyb to train, test and visualise the result.