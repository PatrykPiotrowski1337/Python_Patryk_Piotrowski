def checkIfList(a: list, b: int) -> bool:
    if b in a:
        return True
    return False

print(checkIfList([1,2,3],13))