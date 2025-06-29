def main():

    #call function to take relative book path and turn it to a string
    output = get_book_text("books/frankenstein.txt")

    #call function to accept string and count the words 
    count = get_num_words(output)
    print(f"{count} words found in the document")

#function that takes filepath and converts it to a string
def get_book_text(path_to_file):

    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents

#function that takes string and counts words in it
def get_num_words(text):
    return len(text.split())

main()