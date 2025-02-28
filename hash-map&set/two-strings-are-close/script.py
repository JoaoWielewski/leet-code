word1 = "cabbba"
word2 = "abbccc"

def close_strings(word1: str, word2: str) -> bool:
    if (len(word1) != len(word2)):
        return False

    letters_dict1 = separate_letters(word1)
    letters_dict2 = separate_letters(word2)

    dict1_values = letters_dict1.values()
    dict2_values = letters_dict2.values()

    dict1_keys_set = set(letters_dict1.keys())
    dict2_keys_set = set(letters_dict2.keys())

    if not dict1_keys_set.issubset(dict2_keys_set) and not dict2_keys_set.issuperset(dict1_keys_set):
        return False

    return sorted(dict1_values) == sorted(dict2_values)


def separate_letters(word):
    letters_dict = {}

    for letter in word:
        if letter in letters_dict:
            letters_dict[letter] = letters_dict.get(letter) + 1
        else:
            letters_dict[letter] = 1

    return letters_dict





print(close_strings(word1, word2))