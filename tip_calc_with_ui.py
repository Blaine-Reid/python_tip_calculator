# Tip Calculator for determining the bill per person in a party
# of X people, after applying a tip of X%

import tkinter as tk

# Variables
window_width = 600
window_height = 400
window_x = '+50'
window_y = '+50'

# creates main widnow
root = tk.Tk()
# create title for application
root.title('Tip Calculator')
# sets size and location of application on window
root.geometry(f'{window_width}x{window_height}{window_x}{window_y}')
# blocks user from resizing window
root.resizable(False, False)

# create a text widgets
title_text = tk.Label(root, text='Tip Calculator')
party_size_text = tk.Label(root, text='Party Size')
bill_text = tk.Label(root, text='Bill Total')
tip_perc_text = tk.Label(root, text='Tip Percentage')

# add text to window
title_text.pack()
party_size_text.pack()
bill_text.pack()
tip_perc_text.pack()


# loads window
root.mainloop()
