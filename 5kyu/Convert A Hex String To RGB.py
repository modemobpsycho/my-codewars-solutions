def hex_string_to_RGB(hex_string):
    hex_string = hex_string.replace("#", "")
    r = int(hex_string[:2], 16)
    g = int(hex_string[2:4], 16)
    b = int(hex_string[4:], 16)
    return {"r": r, "g": g, "b": b}
