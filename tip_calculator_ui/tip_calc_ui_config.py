import tkinter as tk
import tkinter.font as font


padx = 10
pady = 10
background = "sky blue"
font_lg = ('Times', 24)
font_sm = ('Times', 16)

# TITLE -----------------------------------
title_config = {
    "text": 'Tip Calculator',
    "background": background,
    'anchor': 'center',
    'font': font_lg
}

title_position = {
    "column": 0,
    "columnspan": 2,
    "row": 0,
    "sticky": tk.EW,
    "padx": padx,
    "pady": pady,
}

# PARTY SIZE--------------------------------
party_size_label_config = {
    "text": "Party Size",
    "background": background,
    'font': font_sm
}

party_size_label_position = {
    "column": 0,
    "row": 1,
    "sticky": tk.EW,
    "padx": padx,
    "pady": pady
}

party_size_entry_position = {
    "column": 1,
    "row": 1,
    "sticky": tk.EW,
    "padx": padx,
    "pady": pady
}

party_size_entry_config = {
    'font': font_sm
}

# BILL SIZE----------------------------------
bill_label_config = {
    "text": "Bill Total",
    "background": background,
    'font': font_sm
}

bill_label_position = {
    "column": 0,
    "row": 2,
    "sticky": tk.EW,
    "padx": padx,
    "pady": pady
}

bill_entry_position = {
    "column": 1,
    "row": 2,
    "sticky": tk.EW,
    "padx": padx,
    "pady": pady
}

bill_entry_config = {
    'font': font_sm
}

# TIP PERCENTAGE ----------------------------
tip_perc_label_config = {
    "text": "Tip Percentage",
    "background": background,
    'font': font_sm
}

tip_perc_label_position = {
    "column": 0,
    "row": 3,
    "sticky": tk.EW,
    "padx": padx,
    "pady": pady
}

tip_perc_entry_config = {
    'font': font_sm,

}
tip_perc_entry_position = {
    "column": 1,
    "row": 3,
    "sticky": tk.EW,
    "padx": padx,
    "pady": pady
}


# TAX PERCENTAGE ----------------------------
tax_perc_label_config = {
    "text": "Tax Percentage",
    "background": background,
    'font': font_sm
}

tax_perc_label_position = {
    "column": 0,
    "row": 4,
    "sticky": tk.EW,
    "padx": padx,
    "pady": pady
}

tax_perc_entry_config = {
    'font': font_sm,

}
tax_perc_entry_position = {
    "column": 1,
    "row": 4,
    "sticky": tk.EW,
    "padx": padx,
    "pady": pady
}

# DISPLAY TOTAL-----------------------------------
cost_per_person_config = {
    "background": background,
    'anchor': 'center',
    'font': font_lg,

}

cost_per_person_position = {
    "column": 0,
    "columnspan": 2,
    "row": 6,
    "sticky": tk.EW,
    "padx": padx,
    "pady": pady
}

# Calculate Button
button_config = {
    'text': 'Calculate',
    'font': font_sm,
    'width': 1

}

button_position = {
    "column": 1,
    "columnspan": 1,
    "row": 5,
    "sticky": tk.EW,
    "padx": padx,
    "pady": pady
}
