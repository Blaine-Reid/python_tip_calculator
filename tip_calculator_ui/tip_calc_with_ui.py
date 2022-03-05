# Tip Calculator for determining the bill per person in a party
# of X people, after applying a tip of X%

import tkinter as tk

from tip_calc_ui_functions import *
from tip_calc_ui_widgets import *
from tip_calc_ui_config import *
# Create app class and pass in tk.Tk as parent to give access to methods


class TipCalc(tk.Tk):
    def __init__(self):
        # Call tk.Tk __init__
        super().__init__()

        # Variables
        window_width = 400
        window_height = 400
        window_x = '-50'
        window_y = '+50'

        # create title for application
        self.title('Tip Calculator')
        # sets size and location of application on window
        self.geometry(f'{window_width}x{window_height}{window_x}{window_y}')
        # blocks user from resizing window
        self.resizable(False, False)
        # config
        self.configure(background='sky blue')
        # custom ico
        self.iconbitmap('./assests/calc.ico')

        # Define columns and rows of app
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Variables for display of values
        self.party_size = tk.StringVar()
        self.bill_total = tk.StringVar()
        self.tip_perc = tk.IntVar()
        self.cost_per_person = tk.StringVar()

        # Call createWidgets method
        self.createWidgets()

    def createWidgets(self):
        '''Create Widgets for App'''

        # TITLE
        title = Text(self, title_config, title_position)

        # PARTY SIZE
        party_size = LabelEntry(
            self,
            party_size_label_config,
            party_size_label_position,
            party_size_entry_config,
            party_size_entry_position,
            self.party_size
        )

        # BILL
        bill = LabelEntry(
            self,
            bill_label_config,
            bill_label_position,
            bill_entry_config,
            bill_entry_position,
            self.bill_total
        )

        # TIP PERCENTAGE
        tip = LabelEntry(
            self,
            tip_perc_label_config,
            tip_perc_label_position,
            tip_perc_entry_config,
            tip_perc_entry_position,
            self.tip_perc
        )

        # TOTAL COST PER PERSON
        cost = Text(
            self,
            cost_per_person_config,
            cost_per_person_position,
            self.cost_per_person
        )

        # COMMAND FOR BUTTON
        button_config['command'] = self.calculate

        # CALCULATE BUTTON
        calculate_button = MyButton(
            self,
            button_config,
            button_position)

    def calculate(self):
        '''Calculates the Cost per Person'''

        try:
            bill = float(self.bill_total.get())
            party = int(self.party_size.get())
            tip = 1 + (int(self.tip_perc.get()) / 100)

            bill_per_person = (bill * tip) / party

            self.cost_per_person.set(f'${bill_per_person:.2f} / person')

        except:
            # Show error if invalid values entered
            showinfo(
                title='Error',
                message="A value given is not a number. Please check values and enter only numnbers"
            )
        # return price_per_person


if __name__ == "__main__":
    app = TipCalc()
    app.mainloop()
