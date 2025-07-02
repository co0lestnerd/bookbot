import sys
from stats import (
    get_num_words,
    get_num_char,
    sort_on,
)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    
    #call function to take relative book path and turn it to a string
    output = get_book_text(sys.argv[1])

    #call function from stats to accept string and count the words 
    print(f"----------- Word Count ----------")
    count = get_num_words(output)
    print(f"Found {count} total words")

    #call function from stats to accept string and count the char
    print(f"--------- Character Count -------")
    char_count = get_num_char(output)

    #call function from stats to accept dictionary and sort by numbers descending
    sorted_chars = sort_on(char_count)

    #for each item in list, check if the key is an alphabetic character, and then if so, print it to the console
    for item in sorted_chars:
        storedChar = item["char"]
        storedNum = item["num"]

        if storedChar.isalpha():
            print(f"{storedChar}: {storedNum}")

    print(f"============= END ===============")

#function that takes filepath and converts it to a string
def get_book_text(path_to_file):

    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents


main()