def find_anagrams(word, candidates):
    return [w for w in candidates if sorted(w.lower())==sorted(word.lower()) and w.lower()!=word.lower()]
