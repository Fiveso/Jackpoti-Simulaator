# Eurojackpoti võitmise simulaator. TEGU POLE FINANTSNÕUANDEGA!!
# Hasartmäng pole sobiv viis rahaliste probleemide lahendamiseks.
# 18+, panusta vastutustundlikult.

import random

# Konstandid
PRIZE = 10000000
TICKET_PRICE = 2
EURO_ODDS = 95344200

# Muutujad
gamemode = 0

money_spent = 0
raha = 0

total_days = 0
years = 0
months = 0
days = 0

# Tervitav sõnum
print("Tere tulemast Eurojackpoti võitmise simulaatorisse!\n")

# Võiduni/eelarve prompt
eelarve_prompt = input("Kas soovite mängida eelarvega? [y/N] ")

if eelarve_prompt.lower() == "y" or eelarve_prompt.lower == "" or eelarve_prompt.lower == "n":
    if eelarve_prompt.lower() == "y":
        eelarve = float(input("\nKui palju soovite eelarveks määrata? Sisestage summa: "))
        while eelarve < TICKET_PRICE:
            eelarve = float(input("\nKui palju soovite eelarveks määrata? Sisestage summa: "))
            
            if eelarve < TICKET_PRICE:
                print("Eelarve on väiksem kui ühe pileti hind!")
        raha = eelarve
        gamemode = 1
    else:
        gamemode = 0

# Korduv programm
while(True):
    
    # Küsime mitut piletit mängija tahab
    if gamemode == 0:
        in_tickets = int(input("\nMitu piletit soovite igal loosimisel osta? Sisestage täisarv: "))
    else:
        in_tickets = int(input(f"\nMitu piletit soovite igal loosimisel osta? Eelarve: {eelarve:,.2f}€\nSisestage täisarv: "))
        
        while in_tickets*TICKET_PRICE > raha:
            print("Teil pole raha, et nii palju pileteid osta!")
            
            in_tickets = int(input(f"\nMitu piletit soovite igal loosimisel osta? Eelarve: {eelarve:,.2f}€\nSisestage täisarv: "))
    
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
        if gamemode == 1 and raha < TICKET_PRICE*in_tickets:
            print(f"\nKulutasite {money_spent:,.2f}€ piletite peale ({(int(money_spent/TICKET_PRICE))} piletit).")
            print(f"Raha on otsas, jackpot jäi saamata. Jääk: {raha:,.2f}€")
            
            # Uurime kaua läks. Korra nädalas loositakse. Alustasime loosimise päeval
            total_days = ((money_spent/TICKET_PRICE)/in_tickets) * 7 - 7
            years = int(total_days // 365)
            months = int((total_days % 365) // 30)
            days = int((total_days % 365) % 30)
            print(f"Möödus {years} aastat, {months} kuud ja {days} päeva.")
            break
        # Võidame jackpoti
        if roll(in_tickets/EURO_ODDS):
            raha -= TICKET_PRICE*in_tickets
            money_spent += TICKET_PRICE*in_tickets
            jackpot = True
            print(f"\nKulutasite {money_spent:,.2f}€ piletite peale ({(int(money_spent/TICKET_PRICE))} piletit).")
            print(f"Võitsite {(PRIZE):,.2f}€!\n")
            
            # Uurime kaua läks. Korra nädalas loositakse. Alustasime loosimise päeval
            total_days = ((money_spent/TICKET_PRICE)/in_tickets) * 7 - 7
            years = int(total_days // 365)
            months = int((total_days % 365) // 30)
            days = int((total_days % 365) % 30)
            print(f"Möödus {years} aastat, {months} kuud ja {days} päeva.")
            
            money_spent = 0
        # Kaotasime. Proovime uuesti
        else:
            raha -= TICKET_PRICE*in_tickets
            money_spent += TICKET_PRICE*in_tickets
            #print(f"Kaotasite {int(TICKET_PRICE*in_tickets):,.2f} € (piletihind). Olete kulutanud {money_spent:,.2f}€ piletite peale ({int(money_spent/TICKET_PRICE)} piletit).")
