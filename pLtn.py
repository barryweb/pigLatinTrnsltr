print("Welcome to the Pig Latin Translator Application!")
print("Instructions:")
print("1. Type 'console' to enter words directly into the console for translation.")
print("2. Type 'file' to translate words from 'input.txt' and save the results to 'output.txt'.")
print("3. Type 'exit' to quit the application.")


def translate_word(word):
    vowels = "aeiouAEIOU"
    if word[0] in vowels:
        return word + "way"
    else:
        for index, letter in enumerate(word):
            if letter in vowels:
                return word[index:] + word[:index] + "ay"
        return word


def translate_sentence(sentence):
    words = sentence.split()
    translated_words = [translate_word(word) for word in words]
    return ' '.join(translated_words)


def read_words_from_file(filename):
    with open(filename, 'r') as file:
        return file.read().split()



def write_words_to_file(filename, words):
    with open(filename, 'w') as file:
        file.write(' '.join(words))

def console_interaction():
    while True:
        user_input = input("Enter a word (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Thank you for using the Pig Latin Translator. Goodbye!")
            break
        translated_word = translate_word(user_input)
        print(f"The Pig Latin translation is: {translated_word}")



def file_interaction():
    input_filename = "input.txt"
    output_filename = "output.txt"

    words_to_translate = read_words_from_file(input_filename)
    translated_words = translate_sentence(' '.join(words_to_translate))

    write_words_to_file(output_filename, translated_words.split())
    print(f"Translation completed. Check '{output_filename}' for the translated content.")


def main():
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


if __name__ == "__main__":
    main()