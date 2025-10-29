from stats import word_count
from stats import letter_count



def main():
    title = "frankenstein"
    #title = input("Which Book?\n")
    #read_book(title)
    word_count(title)
    letter_count(title)
    
main()