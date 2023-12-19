def alphabet_position(text):
    import string
    stringfinal = ""
    lowerText = string.ascii_lowercase

    text = text.lower()

    for letter in text:
        if letter in lowerText:
            alphabet_posi = lowerText.index(letter) + 1
            stringfinal += str(alphabet_posi) + " "

    return stringfinal[:-1]