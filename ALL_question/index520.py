def detectCapitalUse(word):
    """
    :type word: str
    :rtype: bool
    """
    word_list = list(word)
    if len(word_list) == 1:
        return True
    count = 0
    for item in word_list:
        if ord(item) > 90 or ord(item) < 65:
            count = count + 1
    if count == len(word_list) or count == 0 or word.lower().title() == word:
        return True
    return False


# def detectCapitalUse(self, word):
#     """
#     :type word: str
#     :rtype: bool
#     """
#     return word.islower() or word.isupper() or word.istitle()





