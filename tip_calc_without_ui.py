# Tip Calculator for determining the bill per person in a party
# of X people, after applying a tip of X%

# import functions
from tip_calc_functions import *

run_calc = True

# While flag is true, run application loop
while run_calc:
    print()

    # get the size of the users party
    party_size = get_party_size()

    # get the bill pre-tip
    bill_pre_tip = get_bill_size()

    # get users tip
    tip_percentage = get_tip_percentage()

    # calculate the bill per person
    bill_per_person = calculate_tip(party_size, tip_percentage, bill_pre_tip)

    # print the values and outcome

    print()
    print("~~~~~~~~~~~~ TIP CALCULATIONS ~~~~~~~~~~~~")
    print("Your bill total was:" + f'${bill_pre_tip:.2f}'.rjust(22))
    print(f'Your tip percentage was:' +
          f'{int(tip_percentage * 100)}%'.rjust(18))
    print(f'Your party size was:' + f'{party_size}'.rjust(22))
    print('------------------------------------------')
    print(f'Bill per person:' + f'${bill_per_person:.2f}'.rjust(26))
    print()

    # if return value it false, exit application
    run_calc = exit_application()
