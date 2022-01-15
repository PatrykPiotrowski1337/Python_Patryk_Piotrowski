class Dieta:
    def __init__(self, ilosc_posilkow: int, jak_czesto: str, posilek_miesny: int, posilek_wazywny: int, cena1: float,
                 cena2: float, ilosc_kalorii1: float, ilosc_kalorii2: float):
        self._ilosc_posilkow = ilosc_posilkow
        self._jak_czesto = jak_czesto
        self._posilek_miesny = posilek_miesny
        self._posilek_wazywny = posilek_wazywny
        self._cena1 = cena1
        self._cena2 = cena2
        self._ilosc_kalorii1 = ilosc_kalorii1
        self._ilosc_kalorii2 = ilosc_kalorii2

    def __str__(self) -> str:
        return f""" Dieta powinna składać się z {self._ilosc_posilkow},
        w tym posilkow miesnych {self._posilek_miesny} sztuk, oraz posilkow wazywnych {self._posilek_wazywny},
        które powinno się jeść srednio {self._ilosc_posilkow} """

    @property
    def ilosc_posilkow(self):
        return self._ilosc_posilkow

    @ilosc_posilkow.setter
    def ilosc_posilkow(self, ilosc_posilkow):
        ilosc_posilkow = self._ilosc_posilkow

    @property
    def jak_czesto(self):
        return self._jak_czesto

    @jak_czesto.setter
    def jak_czesto(self, jak_czesto):
        jak_czesto = self._jak_czesto

    @property
    def posilek_miesny(self):
        return self._posilek_miesny

    @posilek_miesny.setter
    def pesel(self, posilek_miesny):
        posilek_miesny = self._posilek_miesny

    @property
    def posilek_wazywny(self):
        return self._posilek_wazywny

    @posilek_wazywny.setter
    def data_urodzenia(self, posilek_wazywny):
        posilek_wazywny = self._posilek_wazywny

    @property
    def cena1(self):
        return self._cena1

    @cena1.setter
    def cena1(self, cena1):
        self._cena1 = cena1

    @property
    def cena2(self):
        return self._cena2

    @cena2.setter
    def cena2(self, cena2):
        self._cena2 = cena2

    @property
    def ilosc_kalorii1(self):
        return self._ilosc_kalorii1

    @ilosc_kalorii1.setter
    def ilosc_kalorii1(self, ilosc_kalorii1):
        self._ilosc_kalorii1 = ilosc_kalorii1

    @property
    def ilosc_kalorii2(self):
        return self._ilosc_kalorii2

    @ilosc_kalorii2.setter
    def ilosc_kalorii2(self, ilosc_kalorii2):
        self._ilosc_kalorii2 = ilosc_kalorii2
