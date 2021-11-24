def dwieListy(a: list, b: list) -> list:
    bezTychSamych = list(set(a + b))
    LaczonaLista = [i ** 3 for i in bezTychSamych]
    return LaczonaLista


print(dwieListy([0,1,2], [1,2]))

