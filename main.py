import sys
from stats import num_words
from stats import character_count
from stats import dict_report

def get_book_text(f):
    with open(f) as book:
        return book.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    file = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}")
    print("----------- Word Count ----------")
    print(f"Found {num_words(get_book_text(file))} total words")
    print("--------- Character Count -------")
    temp1 = dict_report(character_count(get_book_text(file)))
    for item in temp1:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    return sys.exit(0)


main()
