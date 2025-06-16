from stats import num_words
from stats import character_count

def get_book_text(f):
    with open(f) as book:
        return book.read()

def main():
    file = "/home/frozen/workspace/github.com/USFrozen/bookbot/books/frankenstein.txt"
    print(f"{num_words(get_book_text(file))} words found in the document")
    print(f"{character_count(get_book_text(file))}")

main()
