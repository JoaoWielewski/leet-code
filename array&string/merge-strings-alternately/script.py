word1: str = "abc"
word2: str = "pqrzz"

def merge_alternately(word1: str, word2: str) -> str:
    merged_string: str = ""
    index = 0
    if len(word1) <= len(word2):
    
        for letter in word1:
            merged_string += letter
            merged_string += word2[index]
            word2 = word2[1:]
        
        merged_string += word2

    else:
        for letter in word2:
            merged_string += word1[index]
            word1 = word1[1:]
            merged_string += letter


        merged_string += word1

    return merged_string
            


print(merge_alternately(word1, word2))