def main():
    filepath = "books/frankenstein.txt"
    file_contents = get_book_text(filepath)
    print(file_contents)


def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

main()
