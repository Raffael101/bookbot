def sort_go(letter):
    return letter["num"]

def pretty_dict(title):
    char_list = []
    soup = letter_count(title)
    b = 0 
    for a in soup:
        if a.isalpha():
            char_list.append({"char": a,"num": soup[a]})
        else:
            continue
    char_list.sort(reverse=True, key=sort_go)
    return char_list



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
    return alphabet

def word_count(title):
    book = read_book(title)
    word = book.split()
    return word

def read_book(title):
    with open(title) as f:
        book = f.read()
    return book
