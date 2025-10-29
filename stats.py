
def letter_count(title):
    book = read_book(title)
    lower_book = book.lower
    alphabet = {}
    if alphabet in lower_book:
        alphabet[i] += 1
    else:
        alphabet[i] += 1
    print(alphabet)
    pass

def word_count(title):
    book = read_book(title)
    word = book.split() 
    print(f"Found {len(word)} total words")

def read_book(title):
    with open(f"books/{title}.txt") as f:
        book = f.read()
    return book

letter_count("frankenstein")