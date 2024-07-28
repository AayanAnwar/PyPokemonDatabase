import requests
from tkinter import *

root = Tk()
root.resizable(0,0)
root.geometry("480x480")
root.config(bg="#000")
root.title("Pokemon API")

"""
def get_pkmn(pkmn):
   response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pkmn.lower()}")
   print(f"Response Status: {response.status_code}")
   #print(response.text)
   pokemon = response.json()
   print(f"Pokemon Name: {pokemon['name'].title()}")
   print(f"Height: {pokemon['height']} decimeters")
   print(f"Weight: {pokemon['weight']} hectograms")
   print(f"Species: {pokemon['species']}")
   print(f"Types: {pokemon['types']}")

pkmn = "Ditto"

while pkmn != 'q':
    if pkmn == 'q':
        print("--PROGRAM END--")
    else:
            print("Enter the name of your Pokemon:")
            print("(Input q to quit)")
            pkmn = input()
            get_pkmn(pkmn)
"""

#widgets
title = Label(root,text="Pokemon API",font=("courier",15),fg="#00ff00",bg="#000",anchor=CENTER).grid(row=0,columnspan=2,column=0)
pkmn_field = Entry(root,width=50,bg="#fff").grid(row=1,column=0)
submit_pkmn = Button(root,text="Submit Name",bg="#000",fg="#00ff00",padx=5,width=15).grid(row=1,column=1)

root.mainloop()

