# Eurojackpoti võitmise simulaator. TEGU POLE FINANTSNÕUANDEGA!!
# Hasartmäng pole sobiv viis rahaliste probleemide lahendamiseks.
# 18+, panusta vastutustundlikult.

import random

# Konstandid
PRIZE = 10000000
TICKET_PRICE = 2
EURO_ODDS = 95344200

# Muutujad
money_spent = 0

# Tervitav sõnum
print("Tere tulemast Eurojackpoti võitmise simulaatorisse! Mängime kuni võidate jackpoti.\n")

# Korduv programm
while(True):
    # Küsime mitut piletit mängija tahab
    in_tickets = int(input("Mitu piletit soovite igal loosimisel osta? Sisesta: "))
    
    # Saadame piletiteta mängijad minema
    if in_tickets < 1:
        print("Väga õige otsus!")
        break
    
    # Jackpot pole veel võidetud
    jackpot = False
    
    # Rollimise funktsioon
    def roll(odds):
        return random.random() < odds
    
    # Rollime kuni võidame jackpoti
    while not jackpot:
        # Võidame jackpoti
        if roll(in_tickets/EURO_ODDS):
            money_spent += TICKET_PRICE*in_tickets
            jackpot = True
            print("\nKulutasite {:,.2f}".format(money_spent) + "€ piletite peale (" + str(int(money_spent/TICKET_PRICE)) + " piletit).")
            print("Võitsite {:,.2f}".format(PRIZE) + "€!\n")
            money_spent = 0
        # Kaotasime. Proovime uuesti
        else:
            money_spent += TICKET_PRICE*in_tickets
            #print("Kaotasite {:,.2f}".format(int(TICKET_PRICE*in_tickets)) + "€ (piletihind). Olete kulutanud {:,.2f}".format(money_spent) + "€ piletite peale (" + str(int(money_spent/TICKET_PRICE)) + " piletit).")

