# Functions for the tip calculator

def get_party_size(question, negative_input, error_message) -> int:
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
            party_size = int(input(question))

            # if number is less than 0, restart loop
            if party_size < 0:
                print(negative_input)
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
            print(error_message)


def get_bill_size(question, negative_input, error_message) -> float:
    '''Get the bill size from user, pre-tip'''

    # flag to continue while loop
    bill_input = True

    # Print a decorative title
    print("~~~~~~~~~~~~~~~~ BILL ~~~~~~~~~~~~~~~~ \n")

    while bill_input:
        try:

            # get users bill
            bill_pre_tip = float(input(question))

            # if bill is negative value, rerun loop
            if bill_pre_tip < 0:
                print(negative_input)
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
            print(error_message)


def get_tip_percentage(question, negative_input, error_message) -> float:
    '''Gets the percentage to tip from the user'''

    # flag to continue while loop
    tip = True

    # Print a decorative title
    print("~~~~~~~~~~~~~~~~ TIP PERCENTAGE ~~~~~~~~~~~~~~~~ \n")

    # loop while no errors
    while tip:
        # try and get a float or int value from user
        try:
            tip_percentage = int(input(question))

            # if tip is less than 0, rerun loop
            if tip_percentage < 0:
                print(negative_input)
                continue

            # covert value given to decimal ie 20 = .20
            converted_tip = tip_percentage / 100

            return converted_tip

        except ValueError:
            print(error_message)


def calculate_tip(party: int, tip_percentage: float, bill: float) -> float:
    '''Calculates the bill per person of a party, after applying a tip percentage'''

    # calculate total bill with percentage of tip applied
    bill_w_percentage = bill * (1 + tip_percentage)

    # calculate bill per person
    bill_per_person = bill_w_percentage / party

    # return bill per person
    return bill_per_person


def exit_application(text_to_exit, error_message) -> bool:
    '''Determines if user wants to exit application'''

    while True:    # Ask user if they want to run application again
        run_again = input(text_to_exit)

        # # convert value to lower case for ease
        run_again = run_again.lower()

        # exit application if
        if run_again == 'no' or run_again == 'n':
            return False
        elif run_again == 'yes' or run_again == 'y':
            return True
        else:
            print(error_message)


def print_output(bill_pre_tip, tip_percentage, party_size, bill_per_person):
    '''Prints a neat and clean output'''

    print()
    print("~~~~~~~~~~~~ TIP CALCULATIONS ~~~~~~~~~~~~")
    print("Your bill total was:" + f'${bill_pre_tip:.2f}'.rjust(22))
    print(f'Your tip percentage was:' +
          f'{int(tip_percentage * 100)}%'.rjust(18))
    print(f'Your party size was:' + f'{party_size}'.rjust(22))
    print('------------------------------------------')
    print(f'Bill per person:' + f'${bill_per_person:.2f}'.rjust(26))
    print()

# Testing function for tip calc functions
# assert calculate_tip(get_party_size(), get_tip_percentage(),
#                      get_bill_size()) > 0, "Return was negative"
# assert calculate_tip(1, .20, 10) == 12.00, "Return didn't equal correct value"
