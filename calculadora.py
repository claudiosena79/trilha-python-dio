def somar(a, b):
    return (a + b)

def subtrair(a, b):
    return (a - b)

def multiplicar(a, b):
    return (a * b)

def dividir(a, b):
    return (a / b)



def calcular(a, b, funcao):
    resultado = funcao(a, b)
    print(f'O resultado da operação de {funcao.__name__} entre {a} e {b} é {resultado}')


calcular(a=5, b= 12, funcao= somar)

calcular(5, 12, subtrair)

calcular(a=5, b= 12, funcao= multiplicar)

calcular(5, 12, dividir)
