# Word Counter Program

# Function to count words in a given text
def count_words(text):
    # Split the text into words based on spaces
    words = text.split()
    # Return the number of words
    return len(words)

# Main program execution
def main():
    # Prompt the user to input a sentence or paragraph
    user_input = input("Please enter a sentence or paragraph: ")

    # Check if the input is empty
    if not user_input.strip():
        print("Error: You didn't enter any text. Please try again.")
        return

    # Count the number of words using the count_words function
    word_count = count_words(user_input)

    # Display the result to the user
    print(f"Word Count: {word_count} words")

# Entry point of the program
if __name__ == "__main__":
    main()
