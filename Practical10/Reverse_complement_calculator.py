def reverse_complement(sequence):
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
    sequence_list = list(sequence)
    sequence_list = [complement_table[base] for base in sequence_list]
    string = ''.join(sequence_list)
    return string
seqs=reverse_complement('ACTGactgAACCTTGG')
print(seqs)

