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
total_days = 0
years = 0
months = 0
days = 0

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
            print(f"\nKulutasite {money_spent:,.2f}€ piletite peale ({(int(money_spent/TICKET_PRICE))} piletit).")
            print(f"Võitsite {(PRIZE):,.2f}€!\n")
            
            # Uurime kaua läks. Korra nädalas loositakse. Alustasime loosimise päeval
            total_days = ((money_spent/TICKET_PRICE)/in_tickets) * 7 - 7
            years = int(total_days // 365)
            months = int((total_days % 365) // 30)
            days = int((total_days % 365) % 30)
            print("Sul kulus jackpoti võitmiseks " + str(years) + " aastat, " + str(months) + " kuud ja " + str(days) + " päeva.\n")
            
            money_spent = 0
        # Kaotasime. Proovime uuesti
        else:
            money_spent += TICKET_PRICE*in_tickets
            #print(f"Kaotasite {int(TICKET_PRICE*in_tickets):,.2f} € (piletihind). Olete kulutanud {money_spent:,.2f}€ piletite peale ({int(money_spent/TICKET_PRICE)} piletit).")

