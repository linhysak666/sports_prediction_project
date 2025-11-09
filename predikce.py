import csv
import random

# Načtení dat
with open('data.csv', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    zápasy = list(reader)

print('--- SPORTOVNÍ PREDIKCE ZÁPASŮ ---\n')

for zápas in zápasy:
    tip = random.choice(['1', 'X', '2'])
    print(f"{zápas['Sport']}: {zápas['Tým_domácí']} vs {zápas['Tým_hosté']} -> Predikce: {tip}")

print('\nPredikce dokončena. Hodně štěstí!')
