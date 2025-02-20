s = "  hello world  "

def reverse_words(s: str) -> str:
    words = []
    word = ''

    for letter in s:
        if letter == ' ' and len(word) > 0:
            words.append(word)
            word = ''
        elif letter != ' ':
            word += letter

    if len(word) > 0:
        words.append(word)

    new_string = ''
    for word in reversed(words):
        new_string += word + ' '

    return new_string[:-1]

print(reverse_words(s))
