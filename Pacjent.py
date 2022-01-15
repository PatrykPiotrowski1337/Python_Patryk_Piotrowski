from Osoba import *


class Pacjent(Osoba):
    def __init__(self, imie: str, nazwisko: str, pesel: str, data_urodzenia: str, id_pacjenta: int):
        super().__init__(imie, nazwisko, pesel, data_urodzenia)
        self._id_pacjenta = id_pacjenta

    def __str__(self) -> str:
        return super().__str__() + f""" osoba jest pacjentem z id {self._id_pacjenta}"""

    @property
    def id_pacjenta(self):
        return self._id_pacjenta

    @id_pacjenta.setter
    def imie(self, id_pacjenta):
        id_pacjenta = self._id_pacjenta
