from stats import word_count
from stats import pretty_dict
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        title = sys.argv[1]
        count = word_count(title)
        bet = pretty_dict(title)
        #title = input("Which Book?\n")    
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {title}.txt...")
        print("----------- Word Count ----------")
        print(f"Found {len(count)} total words")
        print("--------- Character Count -------")
        for a in bet:
            print(f"{a["char"]}: {a["num"]}")
        print("============= END ===============")
        #print(f"test{bet}")


main()