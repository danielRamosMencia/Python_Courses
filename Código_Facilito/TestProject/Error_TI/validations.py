def tiny_int(v):
    return v >= 0 and v <= 255

def validation_tiny_int(x):
    try:
        return isinstance(int(x), int)
    except ValueError as error:
        return False