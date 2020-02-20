# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 11:23:23 2020

@author: s3nt3nz4

Convertisseur https://www.mtggoldfish.com > https://deckbox.org/

Tuto tkinter : https://sebsauvage.net/python/gui/index_fr.html
"""

from pandas import DataFrame, read_csv
from tkinter import filedialog
import tkinter as tk


def conversion(url):
    print("je commence la conversion..." + url)
    gf = DataFrame(read_csv(url))
    gf['Tradelist Count'] = ''
    gf['Card Number'] = ''
    gf['Condition'] = ''
    gf['Language'] = 'French'
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

        button = tk.Button(self, text="Convertir", command=self.onclick)
        button.grid(column=1, row=0)

        self.labelVariable = tk.StringVar()
        label = tk.Label(self, textvariable=self.labelVariable, anchor="w", fg="black", bg="grey")
        label.grid(column=0, row=1, columnspan=3, sticky="EW")
        self.labelVariable.set("Coller ci-dessus l'url MTG Goldfish")

        button_exit = tk.Button(self, text="Terminé", command=self.close_window)
        button_exit.grid(column=2, row=0)

        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, False)

    def onclick(self):
        url = self.entryVariable.get()
        conversion(url)
        self.labelVariable.set("OK !")

    def onpressenter(self, event):
        url = self.entryVariable.get()
        conversion(url)
        self.labelVariable.set("OK !")

    def close_window(self):
        self.destroy()


if __name__ == "__main__":
    app = Magic(None)
    app.title('Magic converter')
    app.mainloop()

"""
# Création de la boite de dialogue | Vu sur https://datatofish.com/entry-box-tkinter/
root = tk.Tk()

boite = tk.Canvas(root, width=600, height=300)
boite.pack()

titre = tk.Label(root, text="Copier coller l'url depuis https://www.mtggoldfish.com/portfolio/export :")
titre.config(font=("helvetica", 14))
boite.create_window(300, 100, window=titre)

entree = tk.Entry(root)
boite.create_window(300, 140, window=entree)


    def input_url():
        url_goldfish = entree.get()

        label1 = tk.Label(root, text=url_goldfish)
        boite.create_window(300, 230, window=label1)
        return url_goldfish

    def close_window():
        root.destroy()


button1 = tk.Button(text='bla bla bla', command=input_url)
boite.create_window(200, 180, window=button1)
button2 = tk.Button(text="OK", command=close_window)
boite.create_window(400, 180, window=button2)
# url = input_url()
# print(url)

root.mainloop()

print("Copier coller l'url depuis https://www.mtggoldfish.com/portfolio/export : ")
url = input()
# url = 'https://mtggoldfish-csv-export.s3.amazonaws.com/eb4ff31f-12d3-4032-b6de-b0c1e54db6a2/my_collection.csv'
print(url)

gf = DataFrame(read_csv(url))
gf['Tradelist Count'] = ''
gf['Card Number'] = ''
gf['Condition'] = ''
gf['Language'] = 'French'
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
db.columns = ['Count', 'Tradelist Count', 'Name', 'Edition', 'Card Number', 'Condition', 'Language', 'Foil', 'Signed',
              'Artist Proof', 'Altered Art', 'Misprint', 'Promo', 'Textless', 'My Price']

db = db[db.Edition != 'MTGA']
db = db.replace({
    "Beanstalk Giant": "Beanstalk Giant // Fertile Footsteps",
    "Foulmire Knight": "Foulmire Knight // Profane Insight",
    "Queen of Ice": "Queen of Ice // Rage of Winter",
    "Rosethorn Acolyte": "Rosethorn Acolyte // Seasonal Ritual",
    "Silverflame Squire": "Silverflame Squire // On Alert"
})

db.to_csv('deckbox.csv', index=False)

# ['Count','Tradelist Count','Name','Edition','Card Number','Condition','Language','Foil','Signed','Artist Proof','Altered Art','Misprint','Promo','Textless','My Price']
# https://mtggoldfish-csv-export.s3.amazonaws.com/1806273e-3b35-4643-9930-24dd4df9090e/my_collection.csv
"""
