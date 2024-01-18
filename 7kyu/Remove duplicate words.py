def remove_duplicate_words(s):
    words = s.split()
    unique = []
    for word in words:
        if word not in unique:
            unique.append(word)
    return " ".join(unique)
