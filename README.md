# BDS-Proj
Code for Big Data Science Spring 2017 Project - Movies

Team Members:
Emma Draper,
Will Brantley,
Yoshnee Raveendran

## Data Preparation 
Includes code used to pull data from Twitter and OMDb. merge_data.py provides a template to merge them if we decide to add dimensions to our table later.

#### Dependencies
**crawlOMDB.py** and **merge_data.py**:
* unicodecsv

This can be installed with `pip install unicodecsv`

**GetFollowerCount.java**
* twitter4j

You you can down load the jar at <http://twitter4j.org/en/>.

## Feature Set Generation

#### K-Modes Clustering

To get the clusters of the movies, you can run `python kmodes_movie.py`, but the clusters are already included in the reposititory.

#### Dependency

There is a dependency in this file for a python package called kmodes. THis can be installed with `pip install kmodes`.

#### Feature Sets

Running the scripts in Feature Sets will produce a numerical CSV file for all data in the file. This helpful for using these in RapidMiner. Generate these, and import them into RapidMiner, and connected to the multiply unit in RapidMiner\ Processes/Movie_Workbench.rmp to run and reproduce our results. 
