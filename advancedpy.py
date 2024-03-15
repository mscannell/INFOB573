import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    # Load gene_information, sample_information, and gene_expression dataframes
    gene = pd.read_csv('Gene_Information.csv')
    sample = pd.read_excel('Sample_Information.xlsx')
    expression = pd.read_excel('Gene_Expression_Data.xlsx')
    
    # Set Probe_ID as the index for all dataframes
    gene.set_index('Probe_ID', inplace=True)
    sample.set_index('Probe_ID', inplace=True)
    expression.set_index('Probe_ID', inplace=True)
    
    return gene, sample, expression

def preprocess_data(gene, sample, expression):
    # Merge expression and gene on Probe_ID
    merged = pd.merge(gene, expression, on='Probe_ID', how='inner')
    
    # Transpose merged dataframe
    mergedT = merged.T
    
    # Merge sample with merged
    empty_rows = pd.DataFrame([[np.nan] * len(sample.columns)] * 4, columns=sample.columns)
    sample = pd.concat([empty_rows, sample], ignore_index=False)
    sample['index column'] = sample.index
    mergedT['pathology'] = sample['pathology']
    
    # Rename columns based on pathology
    pathology = {col: f"{pathology}{i}" for i, (col, pathology) in enumerate(zip(sample.columns, ['tumor', 'normal'] * (len(sample.columns) // 2)))}
    mergedT.rename(columns=pathology, inplace=True)
    
    return mergedT

def calculate_fold_change(merged):
    # Split merged dataframe based on pathology
    tumor_cols = [col for col in merged.columns if 'tumor' in col]
    normal_cols = [col for col in merged.columns if 'normal' in col]
    
    tumor_data = merged[tumor_cols]
    normal_data = merged[normal_cols]
    
    # Calculate average tumor and normal
    row_average_tumor = tumor_data.mean(axis=1)
    row_average_normal = normal_data.mean(axis=1)
    
    # Determine fold change and insert results into merged dataframe
    Foldchange = ((row_average_tumor - row_average_normal) / row_average_normal)
    merged['Foldchange'] = Foldchange
    
    # Calculate absolute value of foldchange and insert into new column of merged
    absolute_foldchange = merged['Foldchange'].abs()
    merged['absolute_foldchange'] = absolute_foldchange
    
    return merged

def identify_significant_genes(merged):
    # Identify all absolute_foldchange greater than 5
    genes_greater_than_5 = merged[merged['absolute_foldchange'] > 5]['absolute_foldchange']
    merged['values_greater_than_5'] = genes_greater_than_5
    
    # Identify all genes that were expressed higher in tumor vs normal
    higher_tumor = merged['row_average_tumor'] > merged['row_average_normal']
    higher_normal = merged['row_average_normal'] > merged['row_average_tumor']
    merged['higher_tumor'] = higher_tumor
    merged['higher_normal'] = higher_normal
    
    return merged

def perform_exploratory_analysis(merged):
    # Perform exploratory data analysis on genes
    gene_exploration = merged.describe()
    
    # Create a histogram of # of differential expressed genes by chromosome
    gene_counts = merged['Chromosome'].value_counts()
    sns.histplot(gene_counts, bins=10, kde=False, color='blue', orientation='vertical')
    plt.xlabel('Gene Count')
    plt.ylabel('Chromosome')
    plt.title('Histogram of Differentially Expressed Genes by Chromosome')
    plt.show()

    # Create histogram showing distribution of DEG by chromosome segregated by tumor status
    sns.histplot(data=merged, x='Chromosome', y='gene_counts', hue='higher_tumor')
    plt.xlabel('Gene Count')
    plt.ylabel('Chromosome')
    plt.title('Histogram of Differentially Expressed Genes by Chromosome')
    plt.show()

    # Create histogram showing distribution of DEG by chromosome segregated by tumor vs normal
    sns.barplot(data=merged, x='Symbol', y='absolute_foldchange', hue='higher_tumor')
    plt.xlabel('Gene')
    plt.ylabel('Fold Change')
    plt.title('Fold change based on tumor vs normal')
    plt.show()

    # Make heatmap of differentially expressed genes
    sns.heatmap(calcnormal, cmap='coolwarm', annot=True, fmt='.2f')
    plt.show()

    sns.heatmap(calctumor, cmap='coolwarm', annot=True, fmt='.2f')
    plt.show()

    # Make clustermap to visualize gene expression by pathology
    sns.clustermap(calcnormal, cmap='coolwarm', annot=True, fmt='.2f')
    plt.show()

    sns.clustermap(calctumor, cmap='coolwarm', annot=True, fmt='.2f')
    plt.show()

def main():
    # Load data
    gene, sample, expression = load_data()
    
    # Preprocess data
    merged = preprocess_data(gene, sample, expression)
    
    # Calculate fold change
    merged = calculate_fold_change(merged)
    
    # Identify significant genes
    merged = identify_significant_genes(merged)
    
    # Perform exploratory data analysis
    perform_exploratory_analysis(merged)

if __name__ == "__main__":
    main()
