
def letter_count(title):
    book = read_book(title)
    lower_book = book.lower()
    alphabet = {}
    key = alphabet.keys()
    for key in lower_book:
        if key in alphabet:
            alphabet[key]+=1
        else:
            alphabet[key]= 1
    print(alphabet)
    return alphabet

def word_count(title):
    book = read_book(title)
    word = book.split()
    print(f"Found {len(word)} total words")
    return word

def read_book(title):
    with open(f"books/{title}.txt") as f:
        book = f.read()
    return book