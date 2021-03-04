def contains(haystack, needle):

    # Does the haystack contain the needle?
    for item in haystack:
        if item == needle:
            return True

    return False