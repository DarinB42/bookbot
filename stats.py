def count_words(text):
    return len(text.split())

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char in 'abcdefghijklmnopqrstuvwxyz':
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts

def sort_characters(char_counts):
    sorted_list = [{"char": char, "num": count} for char, count in char_counts.items()]
    sorted_list.sort(key=lambda x: x["num"], reverse = True)
    return sorted_list

