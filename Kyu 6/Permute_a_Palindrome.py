def permute_a_palindrome(input):
    frecuencia = {}
    
    for char in input:
        if char in frecuencia:
            frecuencia[char] += 1
        else:
            frecuencia[char] = 1

    impares = 0
    for count in frecuencia.values():
        if count % 2 != 0:
            impares += 1

    return impares <= 1