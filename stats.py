def num_words(book):
    words = book.split()
    return len(words)

def character_count(book):
    symbols = list(book.lower())
    chars = {}
    for symbol in symbols:
        try:
            chars[symbol] += 1
        except KeyError:
            chars[symbol] = 1
    return chars
