import random

#tällä liitetään .txt tiedosto, josta haetaan wordle peliin sanat (ne ovat valmiiksi kirjoitettuja)
with open("wordle.txt") as SanaLista:
    rivit = SanaLista.readlines()
    sanat = [sana.rstrip() for sana in rivit]

#määritellään arvattavan sanan yrityskerrat
yritykset = 6
sana = random.choice(sanat)
print(sana)

while yritykset > 0:
    salattu = list("-----")
    arvaus = input("Arvaa sana: ")

    for maara, kirjain in enumerate(arvaus):
        if sana[maara] == kirjain:
            salattu[maara] = kirjain.upper()
        elif kirjain in sana:
            salattu[maara] = kirjain.lower()

    print("".join(salattu))

    if "".join(salattu).lower() == sana:
        print("Voitit pelin! ")
        break
    else:
        yritykset -= 1
