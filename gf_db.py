# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 11:23:23 2020

@author: s3nt3nz4

Convert https://www.mtggoldfish.com > https://deckbox.org/

Tuto tkinter : https://sebsauvage.net/python/gui/index_fr.html

Exemple d'url : https://mtggoldfish-csv-export.s3.amazonaws.com/eb4ff31f-12d3-4032-b6de-b0c1e54db6a2/my_collection.csv
"""

from pandas import DataFrame, read_csv
from tkinter import filedialog
import tkinter as tk


def conversion(url, lang_select):
    # print("je commence la conversion..." + url)
    lib_lang = 'Error'
    if lang_select == 1:
        lib_lang = 'English'
    elif lang_select == 2:
        lib_lang = 'French'
    gf = DataFrame(read_csv(url))
    gf['Tradelist Count'] = ''
    gf['Card Number'] = ''
    gf['Condition'] = ''
    gf['Language'] = lib_lang
    gf['Foil'] = ''
    gf['Signed'] = ''
    gf['Artist Proof'] = ''
    gf['Altered Art'] = ''
    gf['Misprint'] = ''
    gf['Promo'] = ''
    gf['Textless'] = ''
    gf['My Price'] = ''

    cols = ['Quantity', 'Tradelist Count', 'Card', 'Set ID', 'Card Number', 'Condition', 'Language', 'Foil', 'Signed',
            'Artist Proof', 'Altered Art', 'Misprint', 'Promo', 'Textless', 'My Price']
    db = gf[cols]
    db.columns = ['Count', 'Tradelist Count', 'Name', 'Edition', 'Card Number', 'Condition', 'Language', 'Foil',
                  'Signed',
                  'Artist Proof', 'Altered Art', 'Misprint', 'Promo', 'Textless', 'My Price']

    db = db[db.Edition != 'MTGA']
    db = db.replace({
        "Beanstalk Giant": "Beanstalk Giant // Fertile Footsteps",
        "Foulmire Knight": "Foulmire Knight // Profane Insight",
        "Queen of Ice": "Queen of Ice // Rage of Winter",
        "Rosethorn Acolyte": "Rosethorn Acolyte // Seasonal Ritual",
        "Silverflame Squire": "Silverflame Squire // On Alert"
    })

    exportcsv(db)


def exportcsv(deckbox):
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv', initialfile='deckbox')
    deckbox.to_csv(export_file_path, index=None, header=True)


class Magic(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.entryVariable = tk.StringVar()
        self.entry = tk.Entry(self, width=40, textvariable=self.entryVariable)
        self.entry.grid(column=0, row=0, sticky='EW')
        self.entry.bind("<Return>", self.onpressenter)

        button = tk.Button(self, text="Convert", command=self.onclick)
        button.grid(column=1, row=0)

        self.labelVariable = tk.StringVar()
        label = tk.Label(self, textvariable=self.labelVariable, anchor="w", fg="black", bg="grey")
        label.grid(column=0, row=1, columnspan=3, sticky="EW")
        self.labelVariable.set("Paste the url MTG Goldfish above")

        button_exit = tk.Button(self, text="Exit", command=self.close_window)
        button_exit.grid(column=2, row=0)

        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, False)

        self.langue = tk.IntVar()
        r1 = tk.Radiobutton(self, text="English", variable=self.langue, value=1, command=self.sel)
        r1.grid(column=0, row=2)

        r2 = tk.Radiobutton(self, text="French", variable=self.langue, value=2, command=self.sel)
        r2.grid(column=1, row=2)
        r2.select()

    def sel(self):
        return self.langue.get()

    def onclick(self):
        url = self.entryVariable.get()
        try:
            conversion(url, self.sel())
            self.labelVariable.set("OK !")
        except:
            self.labelVariable.set("Error : check the url (should look like : "
                                   "https://mtggoldfish-csv-export.s3.amazonaws.com/......./my_collection.csv).")

    def onpressenter(self, event):
        url = self.entryVariable.get()
        try:
            conversion(url, self.sel())
            self.labelVariable.set("OK !")
        except:
            self.labelVariable.set("Error : check the url (should look like : "
                                   "https://mtggoldfish-csv-export.s3.amazonaws.com/......./my_collection.csv).")

    def close_window(self):
        self.destroy()


if __name__ == "__main__":
    app = Magic(None)
    app.title('Magic converter')
    app.mainloop()
