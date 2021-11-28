class Pojazd:
    def __init__(self, marka, nazwa, model, opis, data_produkcji):
        self._marka = marka
        self._nazwa = nazwa
        self._model = model
        self._opis = opis
        self._data_produkcji = data_produkcji

    def __str__(self):
        return f""" Marka samochodu:{self._marka}\n
        nazwa samochodu{self._nazwa}, model to:{self._model}\n
        Krótki opsi:{self._opis}\n
        Data wydania:{self._data_produkcji}"""

    @property
    def marka(self):
        return self._marka

    @marka.setter
    def marka(self, marka):
        self._marka = marka

    @property
    def nazwa(self):
        return self._nazwa

    @nazwa.setter
    def nazwa(self, nazwa):
        self._nazwa = nazwa

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self.model = model

    @property
    def opis(self):
        return self._opis

    @opis.setter
    def opis(self, opis):
        self._opis = opis

    @property
    def data_produkcji(self):
        return self._data_produkcji

    @data_produkcji.setter
    def data_produkcji(self, data_produkcji):
        self._data_produkcji = data_produkcji


class FirmaTransportowa:
    def __init__(self, nazwaFirmy, wlasciciel, pojazd, nip, data_zalozenia, ):
        self._nazwaFirmy = nazwaFirmy
        self._wlascicel = wlasciciel
        self._pojazd = pojazd
        self._nip = nip
        self._data_zalozenia = data_zalozenia

    def __str__(self):
        return f"""Nazwa firmy{self._nazwaFirmy}\n
                wlascicielem firmy jest {self._wlascicel}\n
                firma posiada pojazd transportowy{self._pojazd}\n
                nip firmy to:{self._nip}\n
                została założona:{self._data_zalozenia}"""

    @property
    def nazwafirmy(self):
        return self._nazwaFirmy

    @nazwafirmy.setter
    def nazwafirmy(self, nazwaFirmy):
        self._nazwaFirmy = nazwaFirmy

    @property
    def wlasciciel(self):
        return self._wlascicel

    @wlasciciel.setter
    def wlasciciel(self, wlasciciel):
        self._wlascicel = wlasciciel

    @property
    def pojazd(self):
        return self._pojazd

    @pojazd.setter
    def pojazd(self, pojazd: Pojazd):
        self._pojazd = pojazd

    @property
    def nip(self):
        return self._nip

    @nip.setter
    def nip(self, nip):
        self._nip = nip

    @property
    def data_zalozenia(self):
        return self._data_zalozenia

    @data_zalozenia.setter
    def data_zalozenia(self, data_zalozenia):
        self._data_zalozenia = data_zalozenia


class FirmaSpozywcza(FirmaTransportowa):
    def __init__(self, nazwaFirmy, wlasciciel, towary, nip, data_zalozenia):
        super().__init__(nazwaFirmy, wlasciciel, nip, data_zalozenia, towary)
        self._towary = towary

    @property
    def towary(self):
        return

    @towary.setter
    def towary(self, towary):
        self._towary = towary


class Odcinek:
    def __init__(self, punktA: float, punktB: float, kraj, miasto, zatwierdzenie):
        self._punktA = punktA
        self._punktB = punktB
        self._kraj = kraj
        self._miasto = miasto
        self._zatwierdzenie = zatwierdzenie

    def __str__(self):
        return f"""Dlugosc do punktu:{self._punktA}
                Dlugosc do punktu B:{self._punktB}
                Kraj do którego jedzie transport:{self._kraj}
                Miasto do którego jedzie transport:{self._miasto}
                Czy zatwierdzono:{self._zatwierdzenie}"""

    @property
    def punkta(self):
        return self._punktA

    @punkta.setter
    def punkta(self, punktA):
        self._punktA = punktA

    @property
    def punktb(self):
        return self._punktB

    @punktb.setter
    def punktb(self, punktB):
        self._punktB = punktB

    @property
    def kraj(self):
        return self._kraj

    @kraj.setter
    def kraj(self, kraj):
        self._kraj = kraj

    @property
    def miasto(self):
        return self._miasto

    @miasto.setter
    def miasto(self, miasto):
        self._miasto = miasto

    @property
    def zatwierdzenie(self):
        return self._zatwierdzenie

    @zatwierdzenie.setter
    def zatwierdzenie(self, zatwierdzenie):
        self._zatwierdzenie = zatwierdzenie


class Kurs:
    def __init__(self, pojazd: Pojazd, firmaTransportowa: FirmaTransportowa, firmaSpozywcza: FirmaSpozywcza,
                 trasa: Odcinek, data):
        self._pojazd = pojazd
        self._firmaTransportowa = firmaTransportowa
        self._firmaSpozywcza = firmaSpozywcza
        self._trasa = trasa
        self._data = data

    def __str__(self):
        return f"""Firma:{self._firmaTransportowa} pojedzie do:\n
                    Firmy:{self._firmaTransportowa}\n
                    Pojazdem:{self._pojazd}\n
                    Trasa do pokonania:{self._trasa}
                    Data:{self._data}"""

    @property
    def pojazd(self):
        return self._pojazd

    @pojazd.setter
    def pojazd(self, pojazd: Pojazd):
        self._pojazd = pojazd

    @property
    def firmatransportowa(self):
        return self._firmaTransportowa

    @firmatransportowa.setter
    def firmatransportowa(self, firmaTransportowa: FirmaTransportowa):
        self._firmaTransportowa = firmaTransportowa

    @property
    def firmaspozywcza(self):
        return self._firmaSpozywcza

    @firmaspozywcza.setter
    def firmaspozywcza(self, firmaSpozywcza: FirmaSpozywcza):
        self._firmaSpozywcza = firmaSpozywcza

    @property
    def trasa(self):
        return self._trasa

    @trasa.setter
    def trasa(self, trasa: Odcinek):
        self._trasa = trasa

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data
def oblicz():
    a=gdzie.punkta
    b=gdzie.punktb
    return print(round(a+b,2))
def wyswietl():
    c=firma2.pojazd.marka
    return print(c)



samochod = Pojazd("Skoda", "Fajna", "Fabia", "stary zlom", "1999")
firma1 = FirmaSpozywcza("NiemieckieSmaczki", "Hans", "Mleko", "1337", "11.10.1914")
firma2 = FirmaTransportowa("PolskaSzlachta", "Jarosław", samochod, "1410", "11.11.1918")
gdzie = Odcinek(12, 11, "Deutchland", "Berlin", "zatwierdzenie")
kursik = Kurs(samochod, firma2, firma1, gdzie, "18.11.2021")

print(kursik)

print(oblicz())

print(wyswietl())
