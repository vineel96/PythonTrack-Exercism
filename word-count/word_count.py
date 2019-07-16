def count_words(sentence):
    import re
    w= re.findall("[a-z]+'*[a-z]|[0-9]", sentence.lower())
    return {word: w.count(word) for word in w if word}