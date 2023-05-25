def verificar_contrasena(contrasena):
    errores = []

    if len(contrasena) < 8 or len(contrasena) > 15:
        errores.append("La contraseña debe tener entre 8 y 15 caracteres.")

    if not any(c.isupper() for c in contrasena):
        errores.append("La contraseña debe contener al menos una letra mayúscula.")

    if not any(c.islower() for c in contrasena):
        errores.append("La contraseña debe contener al menos una letra minúscula.")

    if not any(c.isdigit() for c in contrasena):
        errores.append("La contraseña debe contener al menos un número.")

    if not any(c in "!@#$%&/" for c in contrasena):
        errores.append("La contraseña debe contener al menos uno de los siguientes caracteres especiales: !, @, #, $, %, &. /.")

    return errores


contrasena = input("Ingrese una contraseña: ")
errores = verificar_contrasena(contrasena)

if len(errores) == 0:
    print("Contraseña válida.")
else:
    print("La contraseña no cumple con los siguientes requisitos:")
    for error in errores:
        print("-", error)
