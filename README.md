Gene Expression Analysis Script
Author: Martha Scannell
Date: March 14, 2024
Description:
This Python script analyzes gene expression data to identify differentially expressed genes between tumor and normal samples. It performs the following tasks:

Loads gene information, sample information, and gene expression data.
Merges the dataframes based on Probe_ID.
Transposes the merged dataframe and merges it with sample information.
Renames columns based on sample pathology (tumor or normal).
Calculates average expression for tumor and normal samples.
Determines fold change and absolute fold change for each gene.
Identifies genes with fold change magnitude greater than 5.
Performs exploratory data analysis on genes, including creating histograms and heatmaps.
Visualizes gene expression data using various plots.
Dependencies:
pandas
numpy
matplotlib
seaborn
