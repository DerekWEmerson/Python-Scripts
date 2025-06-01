text_file = "books/frankenstein.txt"

with open(text_file) as f:
    file_contents = f.read()

def wordcount(text):
    words = text.split()
    wordtotal = len(words)
    return wordtotal

def charcount(text):
    chars = {}
    for character in text.lower():
        if character in chars:
            chars[character] += 1
        else:
            chars[character] = 1
    return chars

def sort_on(char_dict):
    letter, count = next(iter(char_dict.items()))
    return count

def report(chars, sort_on):
    list_of_dicts = [{letter: count} for letter, count in chars.items()]
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

wordtotal = wordcount(file_contents)
chars = charcount(file_contents)
rep = report(chars, sort_on)

print(f"--- Begin report of {text_file} ---")
print(f"{wordtotal} words found in the document.")

for char_dict in rep:
    for letter, count in char_dict.items():
        if letter.isalpha():
            print(f"The '{letter}' character was found {count} times")

print("--- End report ---")
