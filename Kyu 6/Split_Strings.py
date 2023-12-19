def solution(s):
    if len(s) %2 != 0:
        s += "_"
    lista = []
    for caracter in range(0, len(s), 2):
        par = s[caracter:caracter+2]
        lista.append(par)
    return lista