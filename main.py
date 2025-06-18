from stats import get_book_word_count, get_book_character_count, get_sorted_character_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    f.close()

    return file_contents

def print_report(filepath, num_words, book_characters):
    sorted_chars = get_sorted_character_count(book_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")
        
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = get_book_word_count(book_text)
    book_characters = get_book_character_count(book_text)

    print_report(file_path, num_words, book_characters)

main()