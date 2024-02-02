#!/bin/bash

# Navigate to the home directory 
cd ~

# Create and navigate to a directory called 'Informatics_573'
mkdir Informatics_573
cd Informatics_573

# Download secondary assemblies for human chromosome 1 (excluding "chr1.fa.gz")from UCSC Genome Browser
wget --no-check-certificate -r -nd -P . -A "chr1_*.fa.gz" https://hgdownload.soe.ucsc.edu/goldenPath/hg38/chromosomes/

# Unzip all the downloaded chromosome 1 assemblies
#tar did not work
gzip -d *.gz

# Create a new empty file called "data_summary.txt" and append a list of all detailed information (including at least file name, size, and permissions) to the 'data_summary.txt'
ls -l > data_summary.txt

# Append the first 10 lines of each of the chromosome 1 assemblies to 'data_summary.txt' 
for file in *.fa
do
    head -n 10 "$file" >> data_summary.txt
done

# Append the name of the assembly as well as the total number of lines included in that assembly to 'data_summary.txt'
# Append the first 10 lines of each of the chromosome 1 assemblies to 'data_summary.txt'
for file in *.fa
do
    name=$(basename "$file" .fa)
    total_lines=$(wc -l < "$file")
    echo "Assembly: $name, Total Lines: $total_lines" >> data_summary.txt
done

echo "Script execution completed successfully" 
