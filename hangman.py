import random
import ascii


def main():
    """Run Hangman Script"""
    while True:
        ascii.title_box('<<<( H A N G M A N )>>>|'
                        '-----------------------|'
                        '< 1 > - Save Hangman!|'
                        '< 2 > - Information ?|'
                        '< 0 > - Exit to Menu ->')
        choice = input("|-> ")
        if choice == "1":
            words = ["bakery", "cartwheel", "python", "castle", "catapult", "meteor", "skyscraper"]
            right_letters, wrong_letters, word = [], [], []  # Keeps track of right and wrong guesses, and the chosen word.
            choice = random.choice(words)  # Select a random word from the words list
            for char in choice:  # Split each character of the word into a list
                word.append(char)
                right_letters.append("_")  # Add underscore placeholder for each correct letter
            while True:
                ascii.title_box('Wrong Letters: ' + ' '.join(wrong_letters) + '|Right Letters: ' + ''.join(right_letters))
                letter = input("| Guess a letter! -> ")
                if len(wrong_letters) == 10:  # Trigger game loss when too many incorrect characters have been guessed
                    ascii.title_box('You Lose!')
                    input("|-> ")
                    break
                elif len(letter) == 1 and letter.isalpha():  # Check if letter is valid
                    if letter in right_letters or letter in wrong_letters:  # Check if character has already been guessed
                        print("| You have already guessed this letter!")
                        input('|-> ')
                    elif letter in word:  # If the letter is found in the word...
                        x = 0
                        for char in word:
                            if letter == char:
                                right_letters[x] = letter  # Replace the underscore where the character lies
                            x += 1
                        if word == right_letters:  # Trigger Game Win when the word matches with the right letters
                            ascii.title_box('You win! The word was: ' + ''.join(word).upper())
                            input("|-> ")
                            break
                    elif letter not in word:  # If the letter is not in the word, add to list of wrong letters
                        wrong_letters.append(letter)
                else:
                    print("| Not a valid letter!")
                    print('|-> ')
        elif choice == '2':
            ascii.title_box('Still need a larger word bank.')
            input('|-> ')
        elif choice == '0':
            break


while __name__ == '__main__':  # This code will not run if it is imported
    main()
