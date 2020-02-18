
## Model for origin identification given origin candidate and fc-article

# Lux
Lux proposes the usage of Linguistic Aspects as Features.

#Here we use the Lux features plus some contextual ones in order to determine which is the origin of a rumour of a given fc-article

## INSTALLATION

# This repository uses bert. in order to use BERT properly:

1)Clone bert repo inside Lux/res:

    -- git clone https://github.com/google-research/bert

2)Download the pre-trained model from bert:

    -- wget https://storage.googleapis.com/bert_models/2018_10_18/uncased_L-12_H-768_A-12.zip

3)Unzip the model inside bert folder:

    -- unzip uncased_L-12_H-768_A-12.zip

   You should have 3 files, the model, bert_config.json and vocab.txt.

4)Set env variable BERT_BASE_DIR:

    -- export BERT_BASE_DIR=/path/to/OriginID/res/bert/uncased_L-12_H-768_A-12

   in our case: export BERT_BASE_DIR=~/OriginID/res/bert/uncased_L-12_H-768_A-12

# Install Specificity model

1)Download DASSP.zip
    
    -- wget https://www.dropbox.com/s/41uw7wm2bbgoff4/DASSP.zip
   
2)Unzip its contents

    -- unzip DASSP.zip

3)Go into folder, download and unzip glove:

    -- cd Domain-Agnostic-Sentence-Specificity-Prediction/
    -- wget https://www.dropbox.com/s/0g880op64chjw4b/glove.840B.300d.zip
    -- unzip glove.840B.300d.zip

+)Check the README.md inside the folder, if modifications have to be done

# Create an virtual environment with python3 and activate it

1)Back to OriginID/

    -- virtualenv envOriginID -p python3
    
    -- source envOriginID/bin/activate
    
# Install requirements

    -- pip install -r requirements.txt

# Download and extract GoogleNews-vectors-negative300.bin into data/

    -- cd data/
    -- wget -c "https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz"
    -- gunzip GoogleNews-vectors-negative300.bin.gz

## Known issues

semantic complexity might raise a division by 0 critical error if the texts fed are not big enough. A simple solution to that is increasing the minimum lenght of body texts in data_loader.py.

# Steps to adapt Lux to OriginID:
1. We will need two .csv files to create the data.csv file used by our model:

- the dataset.csv file from Crawling/input/, that has the following structure (we will rename it to crawling_dataset.csv:

    [page,claim,claim_label,tags,claim_source_domain,claim_source_url,date_check,  source_body,date_fake]

- the datasetVeritas3.csv file from OriginID/data/datasets/datasetVeritas3.csv, that has the following structure:

    [page,claim,verdict,tags,date,author,source_list,source_url,value,name]


Those two files should be placed in the data/datasets/ folder.


2. Then, by using 'generateDataCSV.py' we will create a new data.csv containing three columns in the following manner:


[
       +++ article_body,
       +++ link_paragraph,
       *& date_article = date,
       *& article_tags = tags,
       *& origin_url = source_url,
       & origin_body, 
       +++ origin_header, 
       & origin_date, 
       * label = value 
]

* : obtained from data/datasets/datasetVeritas3.csv

& :  obtained from Crawling/input/dataset.csv

+++ : obtained from the .html files and/or crawled

    the article .html file might be useful for obtaining the first two, but the third will have to be crawled.  

3. after generating data.csv from the updated files (datasetVeritas3.csv will be the updated file after the annotations) run the model with 'python3 lux.py'

## TODO:

1. generateDataCSV.py

2. modify generateFeatures.py to account for the new information

3. probably modify data_loader.py to account for the new vector formats?

4. modify the layers on Lux.py accordingly



