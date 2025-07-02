#function that takes string and counts words in it
def get_num_words(text):
    return len(text.split())

def get_num_char(text):
    characters = {}
    lowercase_text = text.lower()
    
    for char in lowercase_text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    return characters

def sort_on(chardict):
    #create a new list that will contain multiple dictionaries
    charValues = []

    #for each letter in the supplied dictionary(chardict) add it's letter and letter value to a new dictionary in a list
    for letter in chardict:
        letter_value = chardict[letter]

        formatdict = {
            'char': letter,
            'num': letter_value
            }

        charValues.append(formatdict)

    #use the sort method to sort greatest to least and create a function to set the sorting criteria
    def sortNums(tempdict):
        return tempdict["num"]

    charValues.sort(reverse=True, key=sortNums)

    return charValues
    
    
    

