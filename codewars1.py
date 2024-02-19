"""Write a function that takes in a string of 
one or more words, and returns the same string, 
but with all words that have five or more letters 
reversed (Just like the name of this Kata). 
Strings passed in will consist of only letters and spaces. 
Spaces will be included only when more than one word is present."""


def spin_words(sentence):
    # Split the sentence into individual words
    words = sentence.split()

    # Iterate through each word in the list
    for i, word in enumerate(words):
        # If the length of the word is 5 or more, reverse it
        if len(word) >= 5:
            words[i] = word[::-1]  # Reverse the word

    # Join the words back together into a single string
    return " ".join(words)


# Example usage:
sentence = "Hey fellow warriors"
result = spin_words(sentence)
print(result)
