
def count_words(text):
    words = text.split()
    
    return len(words)


def main():

    user_input = input("Please enter a sentence or paragraph: ")

    
    if not user_input.strip():
        print("Error: You didn't enter any text. Please try again.")
        return

    
    word_count = count_words(user_input)

    
    print(f"Word Count: {word_count} words")


if __name__ == "__main__":
    main()
