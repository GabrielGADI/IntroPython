# problema; masina merge atat timp cat inca   are benzina
litri_benzina = 10
while litri_benzina > 0:

    # acceleram
    print('Vruum! Vruum!')
    # scadem benzina
    litri_benzina = litri_benzina - 1
    # aprindem beculetul cand avem <= 3 litri
    if litri_benzina <= 3:
        print('Se aprinde beculetul rosu!!')
print('Stop! Nu mai este benzina')

# tema: barul este deschis pana la ora 3
bar_deschis = 3
while bar_deschis > 0:
    print(f'Barul este deschis. Bine ati venit!')
    bar_deschis = bar_deschis - 1
    if bar_deschis <= 2:
        print(f'Intr-o ora inchidem')
print(f'Am inchis mai poftiti pe la noi si alta data!')
