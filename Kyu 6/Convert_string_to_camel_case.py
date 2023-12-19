def to_camel_case(text):
    end_string = ""
    for i, character in enumerate(text):
        if character == "-" or character == "_":
            continue
        elif i != 0 and (text[i - 1] == "-" or text[i - 1] == "_"):
            end_string += character.upper()
        else:
            end_string += character
    return end_string