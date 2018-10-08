def is_isogram(string=""):
    """
    input: string
    output: bool True if the string is Isogram, False if not
    """
    string = str(string)
    string = string.replace(" ", "")        # duplicated space and hyphens are ok
    string = string.replace("-", "")
    string = string.lower()
    if len(set(string)) == len(string): return True
    else:                               return False
