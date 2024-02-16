# INFOB573

## Spring 2024 Course Material

**Course**: INFOB573  
**Semester**: Spring 2024  
**Programmer**: Matti Scannell  
**Language and Version**: Python 3.10.5  
**Date**: February 15, 2024  

## Description

This repository contains Python scripts to accomplish various tasks related to DNA sequence manipulation and analysis. Below are the details of each part of the assignment:

1. **Reading DNA Sequence**:
   - The Python program reads the complete sequence from the file `chr1_GL383518v1_alt.fa`, which was downloaded in the previous homework's Unix Script.
   - Prints the 10th letter of this sequence.
   - Prints the 758th letter of this sequence.

2. **Creating Reverse Complement**:
   - The Python program creates the reverse complement of the encoded DNA molecule.
   - Prints the 79th letter of this sequence.
   - Prints the 500th through the 800th letters of this sequence.

3. **Nested Dictionary Creation**:
   - The Python program reads the sequence used in Part 1 and creates a nested dictionary that contains the number of times each letter appears in the sequence, as a function of which kilobase of the sequence you are looking at.

4. **Calculating Nucleotide Counts**:
   - The Python program reads the dictionary created in Part 3.
   - Creates a list with 4 elements, containing the number of times each nucleotide (A, C, G, T) is contained in the first 1000 base pairs.
   - Repeats the above step for each kilobase contained in the dictionary.
   - Creates a list containing each individual list from the previous step.
   - Calculates the sum of each list.

## Expected Sum for Each List:

- For the first 1000 base pairs, the expected sum for each nucleotide is 1000.

## Observation:

1. There might be slight variations in the observed sums due to sequencing errors, experimental conditions, or computational inaccuracies.
2. The sums might not always exactly match the expected value due to these factors.

## Output

Results will print in the terminal.

## Dependencies

There are no specific external dependencies for this script.
