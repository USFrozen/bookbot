def get_book_text(f):
    with open(f) as book:
        return book.read()

def main():
    file = "/home/frozen/workspace/github.com/USFrozen/bookbot/books/frankenstein.txt"
    get_book_text(file)
    print(get_book_text(file))

main()
