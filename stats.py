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

def dict_report(chars):
    newlist = []
    for char in chars:
        num = chars[char]
        if char.isalpha():
            newlist.append({'char': char, 'num': num})
    return sorted(newlist, key=lambda x: x['num'], reverse=True)
