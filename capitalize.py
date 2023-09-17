def capitalize_word(word):
    return "" if word=="" else word[0].upper() + word[1:].lower()

def capitalize(words):
    return " ".join([capitalize_word(word) for word in words.split(" ")])