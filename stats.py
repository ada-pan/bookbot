def get_num_words(text):
    num_words = len(text.split())
    return num_words

def get_num_characters(text):
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] = char_dict[char] + 1
        else:
            char_dict[char] = 1
    return char_dict