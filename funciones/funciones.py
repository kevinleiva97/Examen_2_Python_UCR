nombre = input("\nIngrese el nombre del usuario:... ")
ape = input("\nIngrese el apellido del usuario:... ")
cedu = input("\n ingrese la cedula del usuario:... ")


def formato_ced(ced):

    global cedu
    i = False
    while i == False:
        if len(cedu) != 9:
            cedu = input(
                "Favor ingresar nuevamente la cedula:(recordar que debe ser 9 digitos) ... ")
        elif len(cedu) == 9:
            i = True


def formato_user(name, ape1, ced):
    global ape, nombre, cedu
    identificador = nombre + str(len(ape)) + str(cedu[0:3])
    return identificador
