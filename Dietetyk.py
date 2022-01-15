from Osoba import *


class Dietetyk(Osoba):
    def __init__(self, imie: str, nazwisko: str, pesel: str, data_urodzenia: str, id_pracownika: int):
        super().__init__(imie, nazwisko, pesel, data_urodzenia)
        self._id_pracownika = id_pracownika

    def __str__(self) -> str:
        return super().__str__() + f""" osoba jest pracownikiem z id {self._id_pracownika}"""

    @property
    def id_pracownika(self):
        return self._id_pracownika

    @id_pracownika.setter
    def imie(self, id_pracownika):
        id_pracownika = self._id_pracownika
