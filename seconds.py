# Finished Calculator | Calculates how many seconds/days user has been alive
import datetime
import ascii


def main():  # Main Function
    while True:
        menu = True
        run = False
        while menu:  # Menu and Rules
            ascii.clear()
            ascii.title_box("<( L I F E )>|<( C A L C U L A T O R )>|-------------------------|"
                            "< 1 > - Run|< 2 > - Rules|< 0 > - Exit", '|')
            choice = input("| > ")
            if choice == '1':
                ascii.clear()
                run = True
                menu = False
            elif choice == '2':
                ascii.clear()
                ascii.title_box("<<<( I N F O R M A T I O N )>>>|-----------------------------------|"
                                "This is my math project. It is a|"
                                "calculator that determines how many|"
                                "seconds you have been alive.", '|')
                input("| > ")
            elif choice == '0':
                input("| Later old-timer!\n| > ")
                return

        while run:  # Program
            # Get the current date
            now = datetime.datetime.now()
            year_now = now.year
            month_now = now.month
            day_now = now.day

            # Map the birthday as a tuple of integers
            (month_born, day_born, year_born) = map(int, input("| When is your birthday? (mm/dd/yyyy)\n| > ").split('/'))
            ascii.clear()

            # Calculations
            years = int(year_now) - int(year_born)
            if int(month_now) < int(month_born):  # If the birth month has not been reached, subtract a year
                years -= 1
                months = 12 - int(month_born) + int(month_now)
            else:
                months = int(month_now) - int(month_born)
            if int(day_now) < int(day_born):  # If the birthday has not been reached, subtract a month
                months -= 1
                days = 30 - int(day_born) + int(day_now)
            else:
                days = int(day_now) - int(day_born)
            totals = int(years * 31536000) + int(months * 2592000) + int(days * 86400)

            # Print the Info Box
            ascii.title_box("Current Date: " + str(month_now) + "/" + str(day_now) + "/" + str(year_now)
                            + "|Your Birthday: " + str(month_born) + "/" + str(day_born) + "/" + str(year_born)
                            + "|You have been alive for about " + str("{:,}".format(totals)) + " seconds!"
                            + "|Over " + str("{:,}".format(int(totals / 86400))) + " days!", '|')
            input("| > ")
            run = False


while __name__ == "__main__":
    main()
