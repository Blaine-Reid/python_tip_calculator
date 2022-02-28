# Functions for the tip calculator

def get_party_size() -> int:
    '''Gets a users party size'''

    # flag to continue while loop
    party_size = True

    # Print a decorative title
    print("~~~~~~~~~~~~~~~~ PARTY ~~~~~~~~~~~~~~~~ \n")

    # While there isn't a party size given
    while party_size:
        # try and get an interger input from user
        try:
            # ask user for people in party
            party_size = int(
                input('How many people are in your party?\n(Please input number greater than 0 or input 0 to exit)\n'))

            # if number is less than 0, restart loop
            if party_size < 0:
                print('Please input a positive value')
                continue

            # if the user enters 0, they want to exit
            if party_size == 0:
                exit()

            # print a spacer
            print()
            # return integer for party size
            return party_size

        # catch exception ValueError when user enters non-integer
        except ValueError:

            # print instructions
            print(
                "Sorry, I need a number of people in your party.")


def get_bill_size() -> float:
    '''Get the bill size from user, pre-tip'''

    # flag to continue while loop
    bill_input = True

    # Print a decorative title
    print("~~~~~~~~~~~~~~~~ BILL ~~~~~~~~~~~~~~~~ \n")

    while bill_input:
        try:

            # get users bill
            bill_pre_tip = float(input(
                "How much was the bill?\n(Please enter as a positive integer (ie 20 for a $20 bill total) or decimal (ie 20.00 (enter 0 to exit))\n"))

            # if bill is negative value, rerun loop
            if bill_pre_tip < 0:
                print("Please input a positive value for the bill.")
                continue

            # if bill is 0, then exit application
            if bill_pre_tip == 0:
                exit()

            # print a spacer
            print()
            # return the bill
            return bill_pre_tip
        # catch error of user inputing non type convertable value
        except ValueError:
            print(
                "Sorry, I need a number as the value for your bill")


def get_tip_percentage() -> float:
    '''Gets the percentage to tip from the user'''

    # flag to continue while loop
    tip = True

    # Print a decorative title
    print("~~~~~~~~~~~~~~~~ TIP PERCENTAGE ~~~~~~~~~~~~~~~~ \n")

    # loop while no errors
    while tip:
        # try and get a float or int value from user
        try:
            tip_percentage = int(input(
                "How much would you like to tip?\n(Please input a positive integer (ie. 20 for 20%))\n"))

            # if tip is less than 0, rerun loop
            if tip_percentage < 0:
                print('Please input a positive value for tip percentage.')
                continue

            # covert value given to decimal ie 20 = .20
            converted_tip = tip_percentage / 100

            return converted_tip

        except ValueError:
            print('Sorry, I need an integer for the tip')


def calculate_tip(party: int, tip_percentage: float, bill: float) -> float:
    '''Calculates the bill per person of a party, after applying a tip percentage'''

    # calculate total bill with percentage of tip applied
    bill_w_percentage = bill * (1 + tip_percentage)

    # calculate bill per person
    bill_per_person = bill_w_percentage / party

    # return bill per person
    return bill_per_person


def exit_application():

    while True:    # Ask user if they want to run application again
        run_again = input(
            "Would you like to calculate another bill?\n(Input Yes, Y, No, or N (Casing doesn't matter))")
        # convert value to lower case for ease
        run_again.lower()

        # exit application if
        if run_again == 'no' or run_again == 'n':
            return False
        elif run_again == 'yes' or run_again == 'y':
            return True
        else:
            print("Please type either Yes, Y, No, or N \n(Casing doesn't matter)")


# Testing function for tip calc functions
# assert calculate_tip(get_party_size(), get_tip_percentage(),
#                      get_bill_size()) > 0, "Return was negative"
# assert calculate_tip(1, .20, 10) == 12.00, "Return didn't equal correct value"
