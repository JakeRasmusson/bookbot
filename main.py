def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = get_number_words(text)
    characters = count_letters(text)
    sorted_characters_list = characters_sorted_list(characters)
    final_list = characters_is_alpha(sorted_characters_list)

    print(f"-- Begin of Book Report {book_path} ---")
    print(f"{num_words} words found in the document")
    print(    )
    for i in final_list:
        print(f"The '{i['letter']}' character was found {i['number']} times`")

    print("---End report---")


def get_number_words(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["number"]

def get_text(path):
    with open(path) as f:
        return f.read()

def characters_sorted_list(characters):
    sorted_list = []
    for ch in characters:
        sorted_list.append({"letter": ch, "number": characters[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list



def count_letters(text):
    words = text.split()
    text_lower = text.lower()
    characters = {}
    sorted_list = []
    for i in text_lower:
        if i in characters:
            characters[i] += 1
        else:
            characters[i] = 1

    return characters

def characters_is_alpha(sorted_characters_list):
    alpha_characters_list = []
    for items in sorted_characters_list:
        if items["letter"].isalpha() == True:
            alpha_characters_list.append(items)
    return alpha_characters_list




main()