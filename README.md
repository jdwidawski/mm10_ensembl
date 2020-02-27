## Build table with ensembl annotation data for genes in the mouse genome

The input of the program is the ftp site for genome annotation from ENSEMBL.

- pipeline.sh* - performes all the tasks and outputs a comma-delimetered table with ensembl gene id, gene_name, start position, end position and gene description

- download_ensembl.sh - downloads all the necessary .dat.gz files from ensembl

- process_ensembl.sh - unpack the files for each chromosome and cut irrelevant data (e.g the sequences) for processing speed

- generate_results.py - python script to create the result table and output it to the working directory


*pipeline.sh will automatically delete the input files (.dat.gz and unpacked .dat/.txt) after proccessing 
