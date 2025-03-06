def get_word_count(text):
    """Calculate the number of words in the given text."""
    return len(text.strip().split()) if text.strip() else 0

def get_character_count(text):
    """Calculate the number of characters in the given text."""
    return len(text)

def main():
    print("\n=== Word Counter ===\n")
    
    while True:
        # Get user input
        print("Enter your text below (or press Ctrl+C to exit):")
        try:
            text = input("\n> ")
            
            # Calculate counts
            word_count = get_word_count(text)
            char_count = get_character_count(text)
            
            # Display results
            print("\nResults:")
            print(f"Words: {word_count}")
            print(f"Characters: {char_count}")
            print("\n" + "-" * 30 + "\n")
            
        except KeyboardInterrupt:
            print("\n\nThank you for using Word Counter!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
            print("Please try again.\n")

if __name__ == "__main__":
    main()