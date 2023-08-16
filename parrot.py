# Finished Parrot script, repeats words back with random noises. Also draws ASCII graphical art
import random
import ascii


def print_screen(phrase, length, i_filler, o_filler):  # Print the Parrot!
    print("|)--------------------------------------------------------------------------------------------------(|")
    print("|    ________" + ("_" * length) + "______" + o_filler + " |")
    print("|   /         " + (" " * length) + "     \ " + i_filler + "|")
    print("|  |------| " + ' '.join(phrase) + " |------|" + i_filler + "|")
    print("|   \____       __" + ("_" * length) + "_/" + o_filler + "|")
    print("|        \_    /      _                                                                              |")
    print("|          \_ \_    /` '\                                                                            |")
    print("|            \__\ /| @   l                                                                           |")
    print("|                 \|      \                                                                          |")
    print("|    ,^^^^^^^^^,    `\     '\_                                                                       |")
    print("|    |_________|      \    __ '\                                                                     |")
    print("|    |_________|       l  \  `\ `\__                                                                 |")
    print("|    |         |        \  `\./`    ``\                                                              |")
    print("|    `=========`         \ ____ / \   l                                                              |")
    print("|                           ||  ||  )  /                                                             |")
    print("|==)==)==)==)==)==)==)==)==(((=(((==l /==)==)==)====)==)==)==)==)==)==)==)==)==)==)==)==)==)==)==)===|")
    print("|                                   l /                                                              |")
    print("|                                  / /                                                               |")
    print("|                                 / /                                                                |")
    print("|                                //                                                                  |")
    print("|                               /                                                                    |")
    print("|)--------------------------------------------------------------------------------------------------(|")


def main():  # User Loop
    while True:
        menu = True
        run = False
        while menu:  # Menu and Rules
            ascii.clear()
            ascii.title_box("<( P O L L Y )>|<( P A R R O T )>|-----------------|"
                            "< 1 > - Play|< 2 > - Rules|< 0 > - Exit", '|')
            choice = input("| > ")
            if choice == '1':
                ascii.clear()
                run = True
                menu = False
            elif choice == '2':
                ascii.clear()
                ascii.title_box("<<<( I N F O R M A T I O N )>>>|----------------------------------|"
                                "This was my first project. It is a|"
                                "parrot that repeats your input|"
                                "back at you with numerous squawks.", '|')
                input("| > ")
            elif choice == '0':
                input("| See ya *SQUAWK* later!\n| > ")
                return

        while run:  # Input and Calculations
            # Squawk and Random Greetings
            squawk = "*SQUAWK*"
            greetings = ["I can " + squawk + " repeat whatever you " + squawk + " say!",
                         "Say something " + squawk + " and I will " + squawk + " Try to copy you!",
                         "Type anything " + squawk + " and I'll say it back!"]

            ascii.clear()
            ascii.title_box(random.choice(greetings), '|')  # Pick a random greeting from the list
            phrase = input(str('| > '))
            count = phrase.count(" ")  # Counts the Spaces for squawk assignment
            phrase = phrase.split()  # Splits the phrase into a list to allow for string insertion
            rand = 0  # Initialize random variable
            for index in range(count * 2):  # For each Word/Space, chance to add a squawk
                if rand == 0:
                    phrase.insert(index, squawk)
                    rand = random.choice([2, 4])  # 1 squawk, then another two or three words later, repeating
                else:
                    rand -= 1  # Calls Squawk function
            length = len(' '.join(phrase))  # Calculates length of the phrase by characters
            o_filler = str(' ' * (81 - int(length)))
            i_filler = str(' ' * (80 - int(length)))  # <^ These lines add the spaces before the end border character
            print_screen(phrase, length, i_filler, o_filler)
            cmd = input("|> If you want to leave, enter 'q'." 
                        "\n|> If not, enter any key to play again!\n| > ")
            if cmd == 'q':
                input("|)> Goodbye Friend!")
                return


while __name__ == '__main__':
    main()
