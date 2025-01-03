import math
    
def resolver_equacao_segundo_grau(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Sem resultados reais. Delta Negativo"
            
    raizes = []
    
    positiva = (-b)+math.sqrt(delta)/2*a 
    negativa = (-b)-math.sqrt(delta)/2*a
    raizes.append(positiva)
    raizes.append(negativa)
    
    return raizes
    
a = int(input("Informe um número A: "))
b = int(input("Informe um número B: "))
c = int(input("Informe um número C: "))

resultado = resolver_equacao_segundo_grau(a, b, c)
print("O resultado da Equação foi:", resultado)