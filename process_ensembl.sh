#!/bin/bash

file="Mus_musculus.GRCm38.99.chromosome"

for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 MT X Y
do
  gunzip -c "$file"."$i".dat.gz | grep '^FT' > "$file"_"$i".txt
done

gunzip -c Mus_musculus.GRCm38.99.nonchromosomal.dat.gz | grep '^FT' > Mus_musculus.GRCm38.99.chromosome_nonchromosomal.txt