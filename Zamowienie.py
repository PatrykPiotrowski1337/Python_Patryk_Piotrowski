from Dieta import *
from Dietetyk import *
from Osoba import *
from Pacjent import *


class Zamowienie:
    def __init__(self, nowaDieta: Dieta, nowyDietetyk: Dietetyk, nowyPacjent: Pacjent, data_zamowienia: str):
        self._nowaDieta = nowaDieta
        self._nowyDietetyk = nowyDietetyk
        self._nowyPacjent = nowyPacjent
        self._data_zamowienia = data_zamowienia

    def ObliczCene(self):
        print(self._nowaDieta.cena1 + self._nowaDieta.cena2)

    def ObliczKalorie(self):
        print(self._nowaDieta.ilosc_kalorii1 + self._nowaDieta.ilosc_kalorii2)

    def __str__(self) -> str:
        return f"""Nowe zamowienie składa {self._nowyPacjent},
    został do niego skierowany dietetyk{self._nowyDietetyk},{self._nowaDieta},
     nowa dieta została zamowiona dnia:{self._data_zamowienia}"""

    @property
    def nowaDieta(self):
        return self._nowaDieta

    @nowaDieta.setter
    def nowaDieta(self, nowaDieta: Dieta):
        self._nowaDieta = nowaDieta

    @property
    def nowyDietetyk(self):
        return self._nowyDietetyk

    @nowyDietetyk.setter
    def nowyDietetyk(self, nowyDietetyk: Dietetyk):
        self._nowyDietetyk = nowyDietetyk

    @property
    def nowyPacjent(self):
        return self._nowyPacjent

    @nowyPacjent.setter
    def nowyPacjent(self, nowyPacjent: Pacjent):
        self._nowyPacjent = nowyPacjent

    @property
    def data_zamowienia(self):
        return self._data_zamowienia

    @data_zamowienia.setter
    def data_zamowienia(self, data_zamowienia):
        self._data_zamowienia = data_zamowienia
