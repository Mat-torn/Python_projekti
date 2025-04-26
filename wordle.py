import random

#tällä liitetään .txt tiedosto, josta haetaan wordle peliin sanat (ne ovat valmiiksi kirjoitettuja)
with open("wordle.txt") as SanaLista:
    rivit = SanaLista.readlines()
    sanat = [sana.rstrip() for sana in rivit]

#määritellään arvattavan sanan yrityskerrat
oikea_sana = random.choice(sanat)
yritykset = 6

# Luodaan aluksi piilotettu sana (eli kaikki viivat)
salattu = list("-" * len(oikea_sana))

while yritykset > 0:
    print("".join(salattu))  # Näytetään vihje käyttäjälle
    arvaus = input("Arvaa sana: ")

    if arvaus.lower() == oikea_sana:
        print("Voitit pelin! Oikea sana oli:", oikea_sana)
        break

    for i in range(min(len(arvaus), len(oikea_sana))):
        if arvaus[i] == oikea_sana[i]:
            salattu[i] = oikea_sana[i].upper()
        elif arvaus[i] in oikea_sana:
            if salattu[i] == "-":  # Ei korvata oikein arvattua kirjainta
                salattu[i] = arvaus[i].lower()

    yritykset -= 1

    if yritykset == 0:
        print("Hävisit pelin! Oikea sana oli:", oikea_sana)
