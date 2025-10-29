from stats import word_count

def read_book(title):
    with open(f"books/{title}.txt") as f:
        book = f.read()
    return book

def main():
    title = "frankenstein"
    #title = input("Which Book?\n")
    #read_book(title)
    word_count(title)

main()