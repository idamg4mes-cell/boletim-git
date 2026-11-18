# Autor: Idam Fischer

def falta(n):
    """Devolve quantos pontos faltam para chegar a 60.
    Se a media ja e 60 ou mais, devolve 0.
    Ex.: falta(50) -> 10
    """
    if n >= 60 :
        return 0
    elif n < 60 :
     resultado = 60 - n
    # complete aqui: troque o return "?" pelo if
     return resultado
