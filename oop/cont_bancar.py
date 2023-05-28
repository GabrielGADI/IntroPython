class ContBancar:
    # constructorul
    def __init__(self, titularCont, iban):
        # atribute, fields, proprietati
        self.titularCont = titularCont
        self.iban = iban
        self.sold = 0
        self.activ = True
        self.pin = 7777
        self.incercari_activare = 0

    # metode
    def interogareSold(self):
        print(f'Titular {self.titularCont}')
        print(f'Iban {self.iban}')
        print(f'Sold {self.sold}')
        print(f'activ {self.activ}')
        print(f'Incercari activare {self.incercari_activare}')
        print(f'-----------------------------------------')

    def activareCont(self, pin_utilizator):
        self.salut()
        if pin_utilizator == self.pin:
            print(f'Card Activat')
            self.ativ = True
        else:
            print(f'**** Pin gresit')
            self.incercari_activare == self.incercari_activare + 1  # o alternativa ==> self.incercari_activare+=1
            # += (se adauga) operator de atribuire care o salveaza dupa
            # -= (se scade) o prescurtare

    def alimentareCont(self, suma_depusa):
        self.salut()
        self.sold += suma_depusa
        print(f'Ati alimentat {suma_depusa}')
        print(f'Aveti in cont {self.sold}')

    def plataCard(self, suma_cheltuita):
        self.salut()
        if suma_cheltuita <= self.sold:
            self.sold -= suma_cheltuita
            print(f'Ati cheltuit {suma_cheltuita}')
            print(f'Aveti in cont {self.sold}')
        else:
            print(f'****Fonduri induficiente')

    # am definit metoda pentru salut, se va apela cu self.salut in loc de  print(f' Buna {self.titularCont}' )
    def salut(self):
        print(f'Buna {self.titularCont}')
