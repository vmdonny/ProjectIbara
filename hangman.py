import random
import ascii
global menu, play


def main():  # Script Loop
    while True:
        global menu, play
        menu = True
        play = False

        # Add words to the word list!
        words = ["bakery", "cartwheel", "python", "castle", "catapult", "meteor", "skyscraper"]

        # Initialize variables
        right_letters = []  # Keeps track of correctly guessed letters
        wrong_letters = []  # Keeps track of incorrectly guessed letters
        word = []  # Stores selected word

        while menu:  # Menu
            ascii.clear()
            ascii.title_box("<( H A N G M A N )>|-------------------|< 1 > - Play|< 2 > - Rules|< 0 > - Exit", '|')
            choice = input("| > ")

            if choice == '1':
                choice = random.choice(words)  # Select a random word from the words list
                for char in choice:  # Split each character of the word into a list
                    word.append(char)
                    right_letters.append('_')  # Add underscore placeholder for each correct letter
                menu = False
                play = True

            elif choice == '2':  # Show Information
                ascii.clear()
                ascii.title_box("<<<( I N F O R M A T I O N )>>>|-----------------------------------|"
                                "Hangman! You have 10 incorrect|"
                                "guesses. Good luck, save that guy!", '|')
                input("| > ")

            elif choice == '0':  # Exit Game
                input("| Until next crime !\n| > ")
                return

        while play:  # Main Game Loop
            ascii.clear()
            ascii.title_box("Wrong Letters: " + "".join(wrong_letters) + "|Right Letters: " + "".join(right_letters), "|")
            letter = input("| Guess a letter! > ").lower()

            if len(wrong_letters) == 10:  # Trigger game loss when too many incorrect characters have been guessed
                print("| You Lose!")
                input("| > ")
                ascii.clear()
                play = False

            if len(letter) == 1 and letter.isalpha():  # Check if letter is valid
                if letter in right_letters or letter in wrong_letters:  # Check if character has already been guessed
                    print("You have already guessed this letter!")
                    input("| > ")

                elif letter in word:  # If the letter is found in the word...
                    x = 0
                    for char in word:
                        if letter == char:
                            right_letters[x] = letter  # Replace the underscore where the character lies
                        x += 1

                    if word == right_letters:  # Trigger Game Win when the word matches with the right letters
                        print("You win! The word was: " + "".join(word).capitalize())
                        input("| > ")
                        play = False

                elif letter not in word:  # If the letter is not in the word, add to list of wrong letters
                    wrong_letters.append(letter)

            else:  # Catch-all if the character is invalid
                print("Not a valid letter!")
                input("| > ")


while __name__ == '__main__':  # This code will not run if it is imported
    main()
