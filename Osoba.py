class Osoba:
    def __init__(self, imie: str, nazwisko: str, pesel: str, data_urodzenia: str):
        self._imie = imie
        self._nazwisko = nazwisko
        self._pesel = pesel
        self._data_urodzenia = data_urodzenia

    def __str__(self) -> str:
        return f"""Osoba o imieniu {self._imie} oraz nazwiskiem {self._nazwisko},
jej numer pesel to:{self._pesel}, urodzona w {self._data_urodzenia}"""

    @property
    def imie(self):
        return self._imie

    @imie.setter
    def imie(self, imie):
        imie = self._imie

    @property
    def naziwsko(self):
        return self._nazwisko

    @naziwsko.setter
    def naziwsko(self, nazwisko):
        nazwisko = self._nazwisko

    @property
    def pesel(self):
        return self._pesel

    @pesel.setter
    def pesel(self, pesel):
        pesel = self._pesel

    @property
    def data_urodzenia(self):
        return self._data_urodzenia

    @data_urodzenia.setter
    def data_urodzenia(self, data_urodzenia):
        data_urodzenia = self._data_urodzenia
