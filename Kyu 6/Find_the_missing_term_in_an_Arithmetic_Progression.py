def find_missing(sequence):
    dif_comun = (sequence[-1] - sequence[0]) / len(sequence)
    for char in range(len(sequence) - 1):
        if sequence[char + 1] - sequence[char] != dif_comun:
            return sequence[char] + dif_comun
    
    
    return sequence[0]