import ascii
import hangman
import parrot
import seconds


def main():
    ascii.clear()
    ascii.title_box("<<<( PROJECT )>>>|<<<( IBARA )>>>|------------------|< 1 > - Hangman|< 2 > - Parrot|"
                    "< 3 > - Life Calc.|< 0 > - Exit", '|')
    choice = input("| > ")
    ascii.clear()
    if choice == '1':
        hangman.main()
    elif choice == '2':
        parrot.main()
    elif choice == '3':
        seconds.main()
    elif choice == '0':
        exit()


while __name__ == '__main__':  # This code will not run if it is imported
    main()
