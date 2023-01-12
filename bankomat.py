class bankomat:
    def __init__(self, card_id: str, pin: int):
        self.__card_id = card_id
        self.__pin = pin
        try:
            self.__stan_konta = self.autoryzacja_transakcji()
        except Exception:
            print("niepoprawny PIN")

    def stan_konta(self):
        return f"Stan konta wynosi: {self.__stan_konta}"


    def wyplata(self, kwota):
        if kwota <= self.__stan_konta:
            self.__stan_konta -= kwota
            print(f"{self.__class__.__name__} wyplacil {kwota}")
        else:
            print("Brak wystarczajacych srodkow na koncie!")

    def wplata(self, kwota):
        self.__stan_konta += kwota
        print(f"{self.__class__.__name__} wplacil {kwota}")

    def autoryzacja_transakcji(self):
        ###################################################################
        # łączenie do banku i tam weryfikacja pinu i sprawdzenie stan konta,
        # na potrzeby zadania pin jest 1111
        # stan konta to 10 000 PLN
        correct_pin = {}
        stan_konta = {}
        correct_pin[self.__card_id] = 1111
        stan_konta[self.__card_id] = 10000
        ###################################################################
        if self.__pin == correct_pin[self.__card_id]:
            return stan_konta[self.__card_id]
        else:
            raise Exception


klient1 = bankomat('123456', 1111)

print(klient1.stan_konta())
klient1.wplata(1000)
print(klient1.stan_konta())
klient1.wyplata(20000)
print(klient1.stan_konta())
