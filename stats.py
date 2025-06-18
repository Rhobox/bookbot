def get_book_word_count(book_text):
    num_words = len(book_text.split())
    return num_words

def get_book_character_count(book_text):
    acc ={}
    for c in book_text:
        current_char = c.lower()

        if current_char in acc:
            acc[current_char] += 1
        else:
            acc[current_char] = 1
    
    return acc

def get_sorted_character_count(book_characters):
    def sort_on(dict):
        return dict["num"]

    sorted_chars = []
    for k,v in book_characters.items():
        sorted_chars.append({"char": k, "num": v})
    
    sorted_chars.sort(reverse=True, key=sort_on)

    return sorted_chars