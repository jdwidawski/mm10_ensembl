#!/bin/bash

## Download and process ensembl annotation files from ensebml.org ftp.
## Output relevant information in a .csv table
## Input files have to be previously unpacked
##
##
##  Source:
##    ftp://ftp.ensembl.org/pub/release-99/embl/mus_musculus/ (Latest mouse genome release)

printf "\nStarting program\n"

echo "Downloading ensembl annotation for Mus musculus genome version GRCm38.99..."

bash download_ensembl.sh

echo "Unpacking and extracting data from the chromosome data files..."

bash process_ensembl.sh

echo "Running python script to create resuls table..."

python generate_results.py

echo "Removing .dat.gz files..."

rm *.dat.gz

echo "Done"