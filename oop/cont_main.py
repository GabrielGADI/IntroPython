from oop.cont_bancar import ContBancar

cont1 = ContBancar('Luigy V', 'RO009')
cont2 = ContBancar('Vio Gr.', 'RO007')

cont1.activareCont(8898)
cont2.activareCont(9988)
cont2.activareCont(7777)

cont1.alimentareCont(249)
cont2.alimentareCont(300)

cont1.plataCard(200)
cont2.plataCard(400)

# tema
# clasa angajat
# nume, prenume, salariu, vechime
# constructor: nume, prenume, salariu, functie, vechime
# metoda
# de descriere: ce nume, ce prenume, ce salariu, ce functie
# metoda marire salariu in functie de vechime
# daca are vechime sub 5 ani, marim cu 300, daca are peste 5 ani cu 500
# dupa care apelam descrierea


cont2.interogareSold()
cont1.interogareSold()
