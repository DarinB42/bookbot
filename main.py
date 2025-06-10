import sys

from stats import count_words, count_characters, sort_characters

def get_book_text(path_to_file):
    try:
        with open(path_to_file,  'r', encoding='utf-8') as f:
            file_contents = f.read()
        return file_contents
    except FileNotFoundError:
        return "Error: File not found."
    except IOError as e:
        return f"IO error: {e}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    print("=========== BOOKBOT ===========")
    print(f"Analyzing book found at {path}...")

    book_text = get_book_text(path)

    if book_text.startswith("Error"):
        print(book_text)
        sys.exit(1)

    num_words = count_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    char_counts = count_characters(book_text)
    sorted_chars = sort_characters(char_counts)

    print("--------- Character Count -------")
    for entry in sorted_chars:
        char = entry["char"]
        num = entry["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()

