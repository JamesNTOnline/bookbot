
def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def create_char_dict(text):
    chars = {}
    text = text.lower()
    for c in text:
        if c in chars:
            chars[c] +=1
        else:
            chars[c] = 1
    return chars


def sort_on(dict):
    return dict["count"]


def char_dict_to_sorted_list(char_dict):
    sorted_list = []
    for c in char_dict:
        if c.isalpha():
            sorted_list.append({"char": c, "count": char_dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    print(sorted_list)
    return sorted_list
    



def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = create_char_dict(text)
    sorted_char_list = char_dict_to_sorted_list(char_dict)
    print(f"*** Report for {book_path} ***")
    print(f"Book contains {num_words} words")
    for c in sorted_char_list:
        print(f"The letter '{c["char"]}' occurs {c["count"]} times")
    first = sorted_char_list[0]
    last = sorted_char_list[-1]
    diff = first["count"] - last["count"]
    print(f"The most common letter '{first["char"]}' occurs {diff} more times than the least common letter '{last["char"]}'")
    #do other stuff 
    
     
if __name__ == "__main__":
    main()