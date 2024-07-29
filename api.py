import requests
from tkinter import *

root = Tk()
#root.resizable(0,0)
root.geometry("1000x480")
root.config(bg="#000")
root.title("Pokemon API")

#default values before searching Pokemon
pkmn = "Ditto"


def get_pkmn():
    pkmn = pkmn_field.get()
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pkmn.lower()}")
    pokemon = response.json()
    species_url = pokemon['species']['url']
    species_response = requests.get(species_url)
    species = species_response.json()
    name_label.config(text=f"Pokemon Name: {pokemon['name'].title()}")
    height_label.config(text=f"Height: {pokemon['height']} decimeters")
    weight_label.config(text=f"Weight: {pokemon['weight']} hectograms")
    types = [type_info['type']['name']
             for type_info in pokemon['types']]
    types_label.config(text=f"Types: {', '.join(types)}")
    response_stat_label.config(text=f"Response Status: {response.status_code}")

#widgets
title = Label(root, text="Pokemon API", font=("courier", 20), fg="#00ff00", bg="#000", anchor=CENTER)
title.grid(row=0, columnspan=3, column=0)

space0 = Label(root, text="   ", bg="#000")
space0.grid(row=1, column=0)

pkmn_field = Entry(root, width=50, bg="#fff")
pkmn_field.grid(row=1, column=0, columnspan=2)

space1 = Label(root, text="   ", bg="#000")
space1.grid(row=1, column=2)

submit_pkmn = Button(root, text="Submit Name", font=("courier", 10), bg="#000", fg="#00ff00", padx=10, width=15, command=get_pkmn)
submit_pkmn.grid(row=1, column=3)

name_label = Label(root, text="Name: ", bg="#000", fg="#00ff00", font=("courier", 13), justify="left")
name_label.grid(row=2, column=0)

height_label = Label(root, text="Height: ", bg="#000", fg="#00ff00", font=("courier", 13), justify="left")
height_label.grid(row=3, column=0)

weight_label = Label(root, text="Weight: ", bg="#000", fg="#00ff00", font=("courier", 13), justify="left")
weight_label.grid(row=4, column=0)

types_label = Label(root, text="Type(s): ", bg="#000", fg="#00ff00", font=("courier", 13), justify="left")
types_label.grid(row=6, column=0)

response_stat_label = Label(root, text="RESPONSE STATUS: ", bg="#000", fg="#00ff00", font=("courier", 13), justify="left")
response_stat_label.grid(row=7, column=0)

root.mainloop()

