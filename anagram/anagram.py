def find_anagrams(word, candidates):
    return [w for w in candidates if
            sorted(word.lower()) == sorted(w.lower())
            and word.lower() != w.lower()]
