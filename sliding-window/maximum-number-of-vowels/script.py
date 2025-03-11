s = "leetcode"
k = 3

def max_vowels(s: str, k: int) -> int:
    start_index = 0
    max_vowels = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}

    for i in range(k):
        if s[i] in vowels:
            max_vowels += 1

    start_index += 1
    vowel_counter = max_vowels

    while start_index + k < len(s) + 1:
        
        if s[start_index - 1] in vowels:
            vowel_counter -= 1
            
        if s[start_index + k - 1] in vowels:
            vowel_counter += 1
            
        max_vowels = max(vowel_counter, max_vowels)

        start_index += 1
        

    return max_vowels


print(max_vowels(s, k))