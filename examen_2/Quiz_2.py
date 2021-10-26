num = int(input("Ingrese un numero entero:... "))


def saber_primo(num):
    if num % 2 == 1:
        resultado = True
    elif num % 2 == 0:
        resultado = False
    return resultado


if saber_primo(num) is True:
    print("\nEL numero es primo\n")
else:
    print("\nEl numero no es primo\n ")
