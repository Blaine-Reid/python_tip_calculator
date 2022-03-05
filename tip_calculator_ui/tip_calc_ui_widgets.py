import tkinter as tk
from tkinter import ttk

from django import conf


class Text(tk.Tk):
    def __init__(self, parent, config, position, display=None):
        title = ttk.Label(parent, textvariable=display)
        title.configure(config)
        title.grid(position)


class LabelEntry(tk.Tk):
    def __init__(self, parent, label_config, label_posit, entry_config, entry_posit, entry_var):

       # Label
        label = ttk.Label(parent)
        label.config(label_config)
        label.grid(label_posit)

        # Entry

        entry = ttk.Entry(
            parent,
            textvariable=entry_var,

        )
        entry.config(entry_config)
        entry.grid(entry_posit)


class MyButton(tk.Tk):
    def __init__(self, parent, config, position):
        button = tk.Button(parent)
        button.config(config)

        button.grid(position)
