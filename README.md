B573 Advanced R Homework 5
Author: Matti Scannell

Programming Language: R 4.3.3

Date: 19 Apr 2024

Description
This repository explores the differences in gene expression between tumor and normal samples using R. It generates various visualizations such as heatmaps, histograms, barplots, and clustering maps to analyze the data. Additionally, it calculates log2 fold changes to assess gene expression changes.

Required Files
Gene_Information.csv
Sample_Information.tsv
Gene_Expression.xls

Required Packages
dplyr
tibble
ggplot2

Execution Steps
Read the gene expression data, gene information, and sample information as dataframes.
Merge all three dataframes into one.
Split the merged dataframe based on tumor or normal phenotype.
Calculate the average expression for each gene.
Compute the log2 fold change.
Identify genes with an absolute fold change greater than 5.
Add a column indicating whether genes have higher expression in normal or tumor samples.
Conduct exploratory statistical analysis.
Generate a histogram showing differentially expressed genes per chromosome.
Create another histogram incorporating tumor vs normal samples.
Produce a bar chart showing the percentage of genes increased in tumor vs normal samples.
Generate a heatmap of differentially expressed genes.
Create a clustermap of differentially expressed genes.

Output Files
Merged dataframe
Histogram showing DEGs: Can be exported for visualization.
Histogram showing DEGs separated by phenotype: Can be exported for analysis.
Barplot showing the percentage of genes increased in tumor vs normal samples: Can be exported for visualization.
Heatmap of DEGs: Visual representation of gene expression differences.
Clustermap of DEGs: Visual representation of clustered gene expression patterns.
