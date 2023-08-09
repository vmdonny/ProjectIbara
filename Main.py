import ascii
import hangman
import parrot


def main():
    ascii.title_box("<<<( V A U G H N ' S )>>>|"
                    "<<<( P R O G R A M S )>>>|"
                    "-------------------------|"
                    "< 1 > - Good 'ol Hangman|"
                    "< 2 > - Speaking Parrot|"
                    "< 0 > - Exit Library")

    choice = input("|> ")
    if choice == '1':
        hangman.main()
    elif choice == '2':
        parrot.main()
    elif choice == '0':
        exit()


while __name__ == '__main__':  # This code will not run if it is imported
    main()
