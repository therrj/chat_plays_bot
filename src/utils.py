def clamp(val, min_val, max_val):
    """Clamp val between min and max values.

    Args:
        val (int): Integer to clamp value for.
        min_val (int): Minimum value allowed.
        max_val (int): Maximum value allowed

    Returns:
        int
    """
    if val < min_val:
        return min_val
    elif val > max_val:
        return max_val
    else:
        return val


def invert_dictionary(d):
    """Takes a dictionary with a list of values and inverts the dictionary.

    Args:
        d (dict): Dictionary of keys with lists of values to invert.

    Returns:
        A new dictionary where each value is a key, with it's previous
        key as it's only value.
    """
    new_dict = {}
    for k, v in d.items():
        for val in v:
            new_dict[val.lower()] = k.lower()

    return new_dict
