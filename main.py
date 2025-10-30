from stats import word_count
from stats import pretty_dict



def main():
    title = "frankenstein"
    #title = input("Which Book?\n")
    #read_book(title)
    count = word_count(title)
    bet = pretty_dict(title)
            
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{title}.txt...")
    print("----------- Word Count ----------")
    print(f"Found {len(count)} total words")
    print("--------- Character Count -------")
    for a in bet:
        print(f"{a["char"]}: {a["num"]}")
    print("============= END ===============")
    #print(f"test{bet}")


main()