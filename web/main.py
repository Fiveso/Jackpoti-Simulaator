# Eurojackpoti võitmise simulaator. TEGU POLE FINANTSNÕUANDEGA!!
# Hasartmäng pole sobiv viis rahaliste probleemide lahendamiseks.
# 18+, panusta vastutustundlikult.

import random
from browser import document
from browser import timer

# Tervitav sõnum
document["calc"].text = "Tere tulemast Eurojackpoti võitmise simulaatorisse!\nMitu piletit soovite igal loosimisel osta?"
#print("Tere tulemast Eurojackpoti võitmise simulaatorisse!\n")

rolling = False

# Konstandid
PRIZE = 10000000
TICKET_PRICE = 2
EURO_ODDS = 95344200

# Muutujad
rolling = True
gamemode = 1
eelarve = 1000

money_spent = 0
raha = 0

total_days = 0
years = 0
months = 0
days = 0

# Rollimise funktsioon
def roll(odds):
    return random.random() < odds


# Korduv programm
def roll_jackpot():
    gamemode = 0
    eelarve = 1000

    money_spent = 0
    raha = 0

    total_days = 0
    years = 0
    months = 0
    days = 0

    # Jackpot pole veel võidetud
    jackpot = False

    # Küsime mitut piletit mängija tahab
    if gamemode == 0:
        in_tickets = int(document["text"].value)
        #in_tickets = int(input("\nMitu piletit soovite igal loosimisel osta? Sisestage täisarv: "))
    else:
        raha = eelarve
        money_spent = 0
        in_tickets = int(document["text"].value)
        #in_tickets = int(input(f"\nMitu piletit soovite igal loosimisel osta? Eelarve: {eelarve:,.2f}€\nSisestage täisarv: "))

        while in_tickets*TICKET_PRICE > raha:
            #print("Teil pole raha, et nii palju pileteid osta!")

            in_tickets = int(input(f"\nMitu piletit soovite igal loosimisel osta? Eelarve: {eelarve:,.2f}€\nSisestage täisarv: "))

    # Rollime kuni võidame jackpoti
    while not jackpot:

        if gamemode == 1 and raha < TICKET_PRICE*in_tickets:
            rolling = False
            #print(f"\nKulutasite {money_spent:,.2f}€ piletite peale ({(int(money_spent/TICKET_PRICE))} piletit).")
            #print(f"Raha on otsas, jackpot jäi saamata. Jääk: {raha:,.2f}€")

            # Uurime kaua läks. Korra nädalas loositakse. Alustasime loosimise päeval
            total_days = ((money_spent/TICKET_PRICE)/in_tickets) * 7 - 7
            years = int(total_days // 365)
            months = int((total_days % 365) // 30)
            days = int((total_days % 365) % 30)
            #print(f"Möödus {years} aastat, {months} kuud ja {days} päeva.")
            break
        # Võidame jackpoti
        if roll(in_tickets/EURO_ODDS):
            rolling = False
            raha -= TICKET_PRICE*in_tickets
            money_spent += TICKET_PRICE*in_tickets
            jackpot = True
            #print(f"\nKulutasite {money_spent:,.2f}€ piletite peale ({(int(money_spent/TICKET_PRICE))} piletit).")
            #print(f"Võitsite {(PRIZE):,.2f}€!\n")

            # Uurime kaua läks. Korra nädalas loositakse. Alustasime loosimise päeval
            total_days = ((money_spent / TICKET_PRICE) / in_tickets) * 7 - 7
            years = int(total_days // 365)
            months = int((total_days % 365) // 30)
            days = int((total_days % 365) % 30)

            document["calc"].text = f"\nKulutasite {money_spent:,.2f}€ piletite peale ({(int(money_spent / TICKET_PRICE))} piletit).\nVõitsite {(PRIZE):,.2f}€!\nMöödus {years} aastat, {months} kuud ja {days} päeva."

            money_spent = 0
        # Kaotasime. Proovime uuesti
        else:
            raha -= TICKET_PRICE*in_tickets
            money_spent += TICKET_PRICE*in_tickets
            #print(f"Kaotasite {int(TICKET_PRICE*in_tickets):,.2f} € (piletihind). Olete kulutanud {money_spent:,.2f}€ piletite peale ({int(money_spent/TICKET_PRICE)} piletit).")


def start_roll(e):
    # Saadame piletiteta mängijad minema
    in_tickets = int(document["text"].value)
    if in_tickets < 1:
        document["calc"].text = "Väga õige otsus!"
    else:
        document["calc"].text = "Arvutamine..."
        timer.set_timeout(roll_jackpot, 1)


document["calc-btn"].bind("click", start_roll)
