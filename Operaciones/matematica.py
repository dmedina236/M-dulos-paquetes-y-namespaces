#se suman dos numeros 
def suma(a, b):
    return a + b

#se restan dos numeros 
def resta(a, b):
    return a - b

#se dividen dos numeros 
def multiplicacion(a, b):
    return a * b

#se suman dos numeros 
def division(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b