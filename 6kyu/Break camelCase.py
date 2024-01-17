import re


def solution(s):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', s)
