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

# Function to read words from a file
def read_words_from_file(filename):
    """
    Read a list of words from a given filename.
    The function opens the file, reads its contents, and returns a list of words.
    """
    with open(filename, 'r') as file:
        return file.read().split()


# Function to write translated words to a file
def write_words_to_file(filename, words):
    """
    Write a list of translated words to a given filename.
    The function joins the list of words into a string and writes it to the file.
    """
    with open(filename, 'w') as file:
        file.write(' '.join(words))

# Function for console-based interaction
def console_interaction():
    """
    Handle console-based interaction with the user.
    The function prompts the user for words to translate until the user types 'exit'.
    """
    while True:
        user_input = input("Enter a word (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Thank you for using the Pig Latin Translator. Goodbye!")
            break
        translated_word = translate_word(user_input)
        print(f"The Pig Latin translation is: {translated_word}")


# Function for file-based interaction
def file_interaction():
    """
    Handle file-based interaction.
    The function reads words from 'input.txt', translates them, and writes the results to 'output.txt'.
    """
    input_filename = "input.txt"
    output_filename = "output.txt"

    words_to_translate = read_words_from_file(input_filename)
    translated_words = translate_sentence(' '.join(words_to_translate))

    write_words_to_file(output_filename, translated_words.split())
    print(f"Translation completed. Check '{output_filename}' for the translated content.")

# Main function to handle the user's choice of interaction
def main():
    """
    Main function to handle the flow of the application based on user input.
    The user can choose between console interaction, file interaction, or exit the application.
    """
    while True:
        choice = input("Enter your choice ('console', 'file', 'exit'): ").lower()
        if choice == 'console':
            console_interaction()
            break
        elif choice == 'file':
            file_interaction()
            break
        elif choice == 'exit':
            print("Exiting the Pig Latin Translator Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 'console', 'file', or 'exit'.")


# Entry point of the application
if __name__ == "__main__":
    main()