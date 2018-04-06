def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    if get_length(dna1) > get_length(dna2):
        return True
    else:
        return False
    

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    num_nucleotides = 0

    for char in dna:
        if char in nucleotide:
            num_nucleotides = num_nucleotides + 1

    return num_nucleotides


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    """
    
    if dna2 in dna1:
        return True
    else:
        return False

    
def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if DNA sequence dna only contains 'A', 'T', 'C', and 'G'.
    
    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ATECVD')
    False
    """

    for char in dna:
        if char not in 'ATCG':
            return False

    return True


def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    Return the DNA sequence by inserting dna2 into dna1 at the given index.
    
    >>> insert_sequence('CCGG', 'AT', 2)
    CCATGG
    >>> insert_sequence('AATTG', 'C', 3)
    AATCTG
    """

    dna = dna1[:index] + dna2 + dna1[index:]

    return dna



    


    
        
