
# Part 1: Read the sequence from the file
sequence <- readLines("/N/u/mscannel/Quartz/Informatics_573/chr1_GL383518v1_alt.fa")

# Print the 10th letter
print(sequence[10])

# Print the 758th letter
print(sequence[758])

# Part 2: Create reverse complement
reverse_complement <- function(seq) {
  complement <- gsub("A", "t", seq)
  complement <- gsub("T", "a", complement)
  complement <- gsub("C", "g", complement)
  complement <- gsub("G", "c", complement)
  reverse_complement <- toupper(rev(complement))
  return(reverse_complement)
}

rev_comp_sequence <- reverse_complement(sequence)

# Print the 79th letter
print(rev_comp_sequence[79])

# Print 500th through 800th letters
print(rev_comp_sequence[500:800])

# Part 3: Read sequence again
sequence <- readLines("/N/u/mscannel/Quartz/Informatics_573/chr1_GL383518v1_alt.txt")

# Part 4: Create list of nucleotide counts for each kilobase
seq_length <- nchar(sequence)
kb_length <- seq_length / 1000
nucleotide_counts <- list()

for (i in 1:kb_length) {
  start <- (i - 1) * 1000 + 1
  end <- min(i * 1000, seq_length)
  sub_sequence <- substr(sequence, start, end)
  nucleotide_counts[[i]] <- table(strsplit(sub_sequence, "")[[1]])
}

# Part 5: Create data frame with counts of A, C, G, T for first 1000 base pairs
first_kb_counts <- nucleotide_counts[[1]]
first_kb_df <- data.frame(A = first_kb_counts["A"], C = first_kb_counts["C"], G = first_kb_counts["G"], T = first_kb_counts["T"])

# Part 6: Repeat for each kilobase
kb_df_list <- list()
for (i in 1:length(nucleotide_counts)) {
  counts <- nucleotide_counts[[i]]
  df <- data.frame(A = counts["A"], C = counts["C"], G = counts["G"], T = counts["T"])
  kb_df_list[[i]] <- df
}

# Part 7: Calculate sum of each row
row_sums <- sapply(kb_df_list, function(df) sum(df))

# Part 8: Compare expected sum with observed sum
expected_sum <- rep(1000, length(row_sums))
differences <- row_sums - expected_sum

# Part 9: Provide explanation
# Part 9: Explanation
# Part 9: Explanation
# The variable "differences" tracks any variations from the anticipated total sum. If any element in the "differences" list is not 0, 
# it suggests there's a mismatch between what we expected and what we actually observed.
# Potential causes for these differences might involve sequencing inaccuracies, sample impurities, or problems with the counting method.


