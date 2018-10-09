def is_pangram(sentence=''):
    sentence = str(sentence).lower()
    letters = set('abcdefghijklmnopqrstuwxyz') 
    if letters.issubset(sentence):
        return True
    else:
        return False
