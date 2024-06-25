print("Welcome to the Pig Latin Translator Application!")
print("Instructions:")
print("1. Type 'console' to enter words directly into the console for translation.")
print("2. Type 'file' to translate words from 'input.txt' and save the results to 'output.txt'.")
print("3. Type 'exit' to quit the application.")

# Function to translate a single word into Pig Latin
def translate_word(word):
    """
    Translate a single English word into Pig Latin.
    If the word starts with a vowel, add 'way' to the end of the word.
    If the word starts with a consonant, move the consonant cluster to the end and add 'ay'.
    """
    vowels = "aeiouAEIOU"
    if word[0] in vowels:
        return word + "way"
    else:
        for index, letter in enumerate(word):
            if letter in vowels:
                return word[index:] + word[:index] + "ay"
        return word


# Function to translate a sentence into Pig Latin
def translate_sentence(sentence):
    """
    Translate a full sentence into Pig Latin by translating each word individually.
    The function splits the sentence into words, translates each word, and rejoins them.
    """
    words = sentence.split()
    translated_words = [translate_word(word) for word in words]
    return ' '.join(translated_words)

