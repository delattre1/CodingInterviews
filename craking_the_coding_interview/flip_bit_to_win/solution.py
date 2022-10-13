BITS = 32  # Assuming 32-bits
def longest_sequence(n):
    # If all 1s, this is already the longest sequence.
    # This makes more sense in C. Just writing it here for reference.
    if ~n == 0:
        return BITS

    sequences = get_alternating_sequences(n)
    return find_longest_sequence(sequences)

def get_alternating_sequences(n):
    '''
    Return a list of the sizes of the sequences. The sequence starts off with the
    number of 0s (which might be 0) and then alternates with the counts of each
    value.
    '''
    sequences = []
    searching_for = 0
    counter = 0

    for i in range(BITS):
        if n & 1 != searching_for:
            sequences.append(counter)
            searching_for = n & 1  # Flip 1 to 0 or 0 to 1
            # Alternatively: searching_for ^= 1
            counter = 0
        counter += 1
        n >>= 1
    sequences.append(counter)

    return sequences

def find_longest_sequence(seq):
    '''
    Given the lengths of alternating sequences of 0s and 1s, find the longest one
    we can build.
    '''
    max_seq = 1

    for i in range(0, len(seq), 2):  # Note the step size of 2
        zeros_seq = seq[i]
        ones_seq_right = seq[i-1] if i-1 >= 0 else 0
        ones_seq_left = seq[i+1] if i+1 < len(seq) else 0

        this_seq = 0
        if zeros_seq == 1:  # Can merge
            this_seq = ones_seq_left + 1 + ones_seq_right
        elif zeros_seq > 1:  # Just add a zero to either side
            this_seq = 1 + max(ones_seq_left, ones_seq_right)
        elif zeros_seq == 0:  # No zero, but take either side
            this_seq = max(ones_seq_left, ones_seq_right)
        max_seq = max(this_seq, max_seq)

    return max_seq
