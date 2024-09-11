import json
import os

# Název souboru, do kterého budeme ukládat data
filename = 'text.json'

# Načteme data ze souboru, pokud existuje
if os.path.exists(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
else:
    data = []  # Pokud soubor neexistuje, inicializujeme prázdný seznam

def zobrazit_data():
    return data

# Získáme vstup od uživatele
zvire = input("Zadej zvíře: ")

# Přidáme zvíře do seznamu dat
data.append(zvire)

# Vypíšeme aktuální stav dat
print("Aktuální data:", zobrazit_data())

# Při ukončení programu uložíme data zpět do souboru
with open(filename, 'w') as f:
    json.dump(data, f, indent=4)
