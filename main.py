from stats import get_num_words, get_num_characters

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    chars_dict = get_num_characters(text)
    char_list = get_char_list(chars_dict)
    char_list.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print_char_list(char_list)


def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()


def sort_on(items):
    return items["num"]

def get_char_list(chars_dict):
    char_list = []
    for key, value in chars_dict.items():
        temp_dict = {}
        temp_dict["char"] = key
        temp_dict["num"] = value
        char_list.append(temp_dict)
    return char_list

def print_char_list(char_list):
    for i in char_list:
        if i["char"].isalpha() == True:
            print(f"{i["char"]}: {i["num"]}")

main()