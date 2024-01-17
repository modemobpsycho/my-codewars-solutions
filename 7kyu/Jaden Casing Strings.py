def to_jaden_case(string):
    words = string.split()
    jaden = [word.capitalize() for word in words]
    return ' '.join(jaden)
