def get_book_text(f):
    with open(f) as book:
        return book.read()

def num_words(book):
    words = book.split()
    return len(words)

def main():
    file = "/home/frozen/workspace/github.com/USFrozen/bookbot/books/frankenstein.txt"
    print(f"{num_words(get_book_text(file))} words found in the document")

main()
