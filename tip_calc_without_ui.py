# Tip Calculator for determining the bill per person in a party
# of X people, after applying a tip of X%

# import functions
from tip_calc_functions_no_ui import *


def tip_calculator():
    '''Tip Calculator that calculates a bill per person based on original bill and added tip percentage divided by the party size'''

    # Variable for questions for functions
    # Change to suit your needs
    party_size_question = 'How many people are in your party?\n(Please input number greater than 0 or input 0 to exit)\n'
    party_size_negative = 'Please input a positive value'
    party_size_error = "Sorry, I need a number of people in your party."

    bill_pre_tip_question = "How much was the bill?\n(Please enter as a positive integer (ie 20 for a $20 bill total) or decimal (ie 20.00 (enter 0 to exit))\n"
    bill_pre_tip_negative = "Please input a positive value for the bill."
    bill_pre_tip_error = "Sorry, I need a number as the value for your bill"

    tip_percentage_question = "How much would you like to tip?\n(Please input a positive integer (ie. 20 for 20%))\n"
    tip_percentage_negative = 'Please input a value of 0 or greater for tip percentage.'
    tip_percentage_error = 'Sorry, I need an integer for the tip'

    exit_application_question = "Would you like to calculate another bill?\n(Input Yes, Y, No, or N (Casing doesn't matter))"
    exit_application_error = "Please enter value requested."

    # Flag to exit while loop
    run_calc = True

    # While flag is true, run application loop
    while run_calc:
        print()

        # get the size of the users party
        party_size = get_party_size(
            party_size_question, party_size_negative, party_size_error)

        # get the bill pre-tip
        bill_pre_tip = get_bill_size(
            bill_pre_tip_question, bill_pre_tip_negative, bill_pre_tip_error)

        # get users tip
        tip_percentage = get_tip_percentage(
            tip_percentage_question, tip_percentage_negative, tip_percentage_error)

        # calculate the bill per person
        bill_per_person = calculate_tip(
            party_size, tip_percentage, bill_pre_tip)

        # print the values and outcome
        print_output(bill_pre_tip, tip_percentage,
                     party_size, bill_per_person)

        # if return value it false, exit application
        run_calc = exit_application(
            exit_application_question, exit_application_error)


# Run function
tip_calculator()
