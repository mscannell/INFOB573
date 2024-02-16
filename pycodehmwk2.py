# Part 1
def read_chr1_GL383518v1_alt():
    with open("chr1_GL383518v1_alt.fa", "r") as file:
        sequence = file.read().strip().split('\n')[1:]
        sequence = ''.join(sequence)
        return sequence.upper()  # Convert sequence to uppercase

sequence = read_chr1_GL383518v1_alt()
print("10th letter:", sequence[9])  # 10th letter
print("758th letter:", sequence[757])  # 758th letter

# Part 2
def reverse_complement(sequence):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'a': 't', 'c': 'g', 'g': 'c', 't': 'a'}  # Include lowercase letters
    reversed_sequence = sequence[::-1]
    return ''.join(complement[base] for base in reversed_sequence)

reverse_sequence = reverse_complement(sequence)
print("79th letter of reverse complement:", reverse_sequence[78])  # 79th letter
print("500th to 800th letters of reverse complement:", reverse_sequence[499:799])  # 500th to 800th letters

# Part 3
def count_bases(sequence):
    bases_count = {}
    kilobase = 0
    for i, base in enumerate(sequence):
        if i % 1000 == 0 and i != 0:
            kilobase += 1
        if kilobase not in bases_count:
            bases_count[kilobase] = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        bases_count[kilobase][base] += 1
    return bases_count

nested_dict = count_bases(sequence)

# Part 4
first_1000 = [nested_dict[kb][base] for base in 'ACGT' for kb in range(1)]  # First 1000 bases
print("Part 4a:", first_1000)

lists = []
for kb in nested_dict:
    kb_list = [nested_dict[kb][base] for base in 'ACGT']
    lists.append(kb_list)

sums = [sum(lst) for lst in lists]
print("Part 4d:", sums)

