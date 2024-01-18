def filter_lucky(lst):
    return list(filter(lambda l: str(l).find("7") >= 0, lst))
