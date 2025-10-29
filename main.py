def read_book(title):
    with open(f"books/{title}.txt") as f:
        book = f.read()
    return book


def word_count(title):
    book = read_book(title)
    word = book.split() 
    print(f"Found {len(word)} total words")


def main():
    title = "frankenstein"
    #title = input("Which Book?\n")
    #read_book(title)
    word_count(title)

main()