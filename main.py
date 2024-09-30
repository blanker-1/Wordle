import random


notletter = []

def load_words(file_name):
    with open(file_name, 'r') as file:
        return [line.strip() for line in file if len(line.strip()) == 5]  # Only include 5-letter words

def get_random_word(word_list):
    return random.choice(word_list)

def display_status(guess, secret_word):
    status = []
    for i, letter in enumerate(guess):
        if letter == secret_word[i]:
            status.append(letter.upper())  # Correct letter in the correct position
        elif letter in secret_word:
            status.append(letter.lower())  # Correct letter in the wrong position
        else:
            status.append('_')  # Incorrect letter
            if letter not in notletter:
                notletter.append(letter)  # Add to notletter only if it's not already there
    return ' '.join(status)

def play_wordle():
    array = load_words('words.txt')
    
    if not array:
        print("No valid words found in words.txt.")
        return
    
    secret_word = get_random_word(array)
    attempts = 6
    attempt = 0

    print("Welcome to Wordle! Try to guess the 5-letter word.")
    print("You have 6 attempts.")

    while attempt < attempts:
        print(f"The letters you dont have are: {', '.join(notletter)}")
        guess = input(f"Attempt {attempt + 1}/{attempts}: ").strip().lower()
        

        if len(guess) != 5 or not guess.isalpha():
            print("Invalid input. Please enter a valid 5-letter word.")
            continue  
          
        if any(letter in notletter for letter in guess):  # Check if any letter in guess is in notletter
            input1 = input("You have already used one of the letters and it was wrong. Are you sure you want to continue? (y/n): ")
            if input1.lower() not in ['y', 'yes']:
              continue
          
        if guess == secret_word:
            print("Congratulations! You've guessed the word!")
            return

        status = display_status(guess, secret_word)
        print("Status: ", status)
        attempt += 1

    print(f"Sorry, you've run out of attempts. The word was: {secret_word}")

if __name__ == "__main__":
    play_wordle()
