# create a function to make complement sequence
def reverse_complement(sequence):
# store the complement methods in a dictionary
    complement_table = {
        "A":"T",
        "T":"A",
        "G":"C",
        "C":"G",
        "a":"t",
        "t":"a",
        "g":"c",
        "c":"g",
    }
# extend complement sequence and return as a string
    sequence_list = list(sequence)
    sequence_list = [complement_table[base] for base in sequence_list]
    string = ''.join(sequence_list)
    return string
# example
seqs=reverse_complement('ACTGactgAACCTTGG')
print(seqs)

