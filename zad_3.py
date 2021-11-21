def podajInt(a:int) -> bool:
    if a % 2 ==0:
        return True
    return False
liczba = podajInt(11)
if liczba:
    print("Liczba Parzysta")
else:
    print("Liczba niepatrzysta")

