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