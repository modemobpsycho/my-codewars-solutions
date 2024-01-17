import string


def is_pangram(s):
    return set("".join(char.lower() for char in s if char.isalpha())) - set(" ") == set(string.ascii_lowercase)
