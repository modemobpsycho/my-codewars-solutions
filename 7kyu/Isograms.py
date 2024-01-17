
def is_isogram(string):
    return len(string.lower()) == len(set(string.lower()))


print(is_isogram("isogram"))