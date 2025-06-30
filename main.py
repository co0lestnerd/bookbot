def main():

    #call function to take relative book path and turn it to a string
    output = get_book_text("books/frankenstein.txt")

    #call function to accept string and count the words 
    count = get_num_words(output)
    print(f"{count} words found in the document")

    #call function to accept string and count the char 
    char_count = get_num_char(output)
    print(char_count)

#function that takes filepath and converts it to a string
def get_book_text(path_to_file):

    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents

from stats import get_num_words
from stats import get_num_char

main()