# Finished Parrot script, repeats words back with random noises. Also draws ASCII graphical art
import random
import ascii


def main():
    """Run Parrot Script"""
    while True:
        ascii.title_box('<<<( P A R R O T )>>>|'
                        '------------------------|'
                        '< 1 > - Visit the Parrot|'
                        '< 2 > - Information ?|'
                        '< 0 > - Exit to Menu ->')
        choice = input("|-> ")
        if choice == '1':
            squawk = "*SQUAWK*"  # Make the squawk String
            greet = ["I can " + squawk + " repeat whatever you " + squawk + " say!",
                     "Say something " + squawk + " and I will " + squawk + " try to copy you!",
                     "Type anything " + squawk + " and I'll say them back!"]  # Random Greetings
            ascii.title_box(random.choice(greet))
            phrase = input(str('|> '))
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
            o_filler = str(' ' * (69 - int(length)))
            i_filler = str(' ' * (68 - int(length)))  # <^ These lines add the spaces before the end border character
            print("|)--------------------------------------------------------------------------------------(|")
            print("|    ________" + ("_" * length) + "______" + o_filler + " |")
            print("|   /         " + (" " * length) + "     \ " + i_filler + "|")
            print("|  |------| " + ' '.join(phrase) + " |------|" + i_filler + "|")
            print("|   \____       __" + ("_" * length) + "_/" + o_filler + "|")
            print("|        \_    /      _                                                                  |")
            print("|          \_ \_    /` '\                                                                |")
            print("|            \__\ /| @   l                                                               |")
            print("|                 \|      \                                                              |")
            print("|    ,^^^^^^^^^,    `\     '\_                                                           |")
            print("|    |_________|      \    __ '\                                                         |")
            print("|    |_________|       l  \  `\ `\__                                                     |")
            print("|    |         |        \  `\./`    ``\                                                  |")
            print("|    `=========`         \ ____ / \   l                                                  |")
            print("|                           ||  ||  )  /                                                 |")
            print("|==)==)==)==)==)==)==)==)==(((=(((==l /==)==)==)===)==)==)==)==)==)==)==)==)==)==)==)==)=|")
            print("|                                   l /                                                  |")
            print("|                                  / /                                                   |")
            print("|                                 / /                                                    |")
            print("|                                //                                                      |")
            print("|                               /                                                        |")
            print("|)--------------------------------------------------------------------------------------(|")
            input('|\n| > ')
        elif choice == '2':
            ascii.title_box('Problems: text can go past graphics')
        elif choice == '0':
            break


while __name__ == '__main__':
    main()
