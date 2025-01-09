def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def get_character_count(text):
    words = text.split()
    char_dict = {}
    for word in words:
        for ch in word:
            if ch.isalpha():
                if ch.lower() in char_dict:
                    char_dict[ch.lower()] += 1
                else:
                    char_dict[ch.lower()] = 1
    return char_dict

def aggregate_charcount_console(char_count, word_count, book_path):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    for ch, cnt in char_count.items():
        print(f"The '{ch}' character was found {cnt} times")
    print("--- End report ---")
                

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    word_count = get_word_count(text)
    print(word_count)
    char_count = get_character_count(text)
    print(char_count)
    sorted_char_count = {k:v for k,v in sorted(char_count.items(), key=lambda item: item[1], reverse=True)}
    aggregate_charcount_console(sorted_char_count, word_count, book_path)
main()