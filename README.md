
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

1. get the goldstandard annotated files, put into data

2. create a new data.csv containing three columns

    [ url_origin, date_origin, header_origin, body_origin, body_article, link_paragraph, date_article, label ]

3. modify generateFeatures.py to account for the new information

4. modify the layers on Lux.py

