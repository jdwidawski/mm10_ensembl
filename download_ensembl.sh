#!/bin/bash

link=ftp://ftp.ensembl.org/pub/release-99/embl/mus_musculus/Mus_musculus.GRCm38.99.chromosome

for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 MT X Y
do
  if [ ! -f Mus_musculus.GRCm38.99.chromosome."$i".dat.gz ]; then wget "$link"."$i".dat.gz; fi
done

if [ ! -f Mus_musculus.GRCm38.99.nonchromosomal.dat.gz ]; then  wget ftp://ftp.ensembl.org/pub/release-99/embl/mus_musculus/Mus_musculus.GRCm38.99.nonchromosomal.dat.gz; fi