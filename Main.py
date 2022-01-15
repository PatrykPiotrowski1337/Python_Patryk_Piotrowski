from Dietetyk import *
from Dieta import *
from Pacjent import *
from Zamowienie import *

dieta1 = Dieta(3, "Co 4 h", 1, 2, 15, 16, 1300, 1900)
dietetyk1 = Dietetyk("Patryk", "Piotrowski", "Malo Wazne", "19.11.2021", 81)
pacjent1 = Pacjent("Adam", "Puchatek", "Nie Posiada", "20.11.2021", 1)
nowezamowienie = Zamowienie(dieta1, dietetyk1, pacjent1, "15.01.2022")

print(nowezamowienie)

