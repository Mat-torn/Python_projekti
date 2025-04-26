import random

# Luetaan sanalista tiedostosta
with open("wordle.txt") as SanaLista:
    rivit = SanaLista.readlines()
    sanat = [sana.rstrip() for sana in rivit]

# Valitaan satunnainen sana
oikea_sana = random.choice(sanat)
yritykset = 6

# Alussa kaikki piilossa
salattu = list("-" * len(oikea_sana))

while yritykset > 0:
    print("".join(salattu))  # Näytetään tämänhetkinen
    arvaus = input("Arvaa sana 5 kirjainta pitkä sana: ")

    if len(arvaus) != len(oikea_sana):
        print(f"Syötä {len(oikea_sana)} kirjainta pitkä sana.")
        continue

    if arvaus.lower() == oikea_sana:
        print("Voitit pelin! Oikea sana oli:", oikea_sana)
        break

    # Käydään kirjain kerrallaan läpi
    uusi_salattu = salattu.copy()
    for i in range(len(oikea_sana)):
        if arvaus[i] == oikea_sana[i]:
            uusi_salattu[i] = oikea_sana[i].upper()

    salattu = uusi_salattu

    yritykset -= 1

    # Lisäksi voidaan kertoa väärän paikan kirjaimista
    väärä_paikka = []
    for kirjain in set(arvaus):
        if kirjain in oikea_sana and kirjain not in [c.lower() for c in salattu]:
            väärä_paikka.append(kirjain.lower())

    if väärä_paikka:
        print("Oikeita kirjaimia väärissä paikoissa:", " ".join(väärä_paikka))

    if yritykset == 0:
        print("Hävisit pelin! Oikea sana oli:", oikea_sana)
