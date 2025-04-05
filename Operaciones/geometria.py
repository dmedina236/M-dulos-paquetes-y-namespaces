import math

#devuelve el area usando el radio
def area_circulo(radio):
    return math.pi * radio ** 2

#devuelve el perimetro usando el radio
def perimetro_circulo(radio):
    return 2 * math.pi * radio

#devuelve el area usando la base y altura
def area_rectangulo(base, altura):
    return base * altura

#devuelve el perimetro usando la base y altura
def perimetro_rectangulo(base, altura):
    return 2 * (base + altura)