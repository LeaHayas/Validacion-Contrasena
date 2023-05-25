# Validacion de Contraseña con python
Este script tiene como objetivo verificar si una contraseña cumple con ciertos requisitos de seguridad. Se evalúa la longitud de la contraseña, la presencia de letras mayúsculas y minúsculas, números y caracteres especiales.

1) La función ```verificar_contrasena``` recibe la contraseña como parámetro y devuelve una lista de errores.

2) Se inicializa una lista vacía llamada ```errores``` para almacenar los posibles errores encontrados en la contraseña.

3) El primer bloque ```if``` verifica la longitud de la contraseña. Si la longitud es menor que 8 o mayor que 15, se agrega un mensaje de error a la lista ```errores```.

4) El siguiente bloque ```if``` utiliza una comprensión de listas y el método ```isupper()``` para verificar si hay al menos una letra mayúscula en la contraseña. Si no se cumple esta condición, se agrega un mensaje de error a la lista ```errores```.

5) El siguiente bloque ```if``` utiliza una comprensión de listas y el método ```islower()``` para verificar si hay al menos una letra minúscula en la contraseña. Si no se cumple esta condición, se agrega un mensaje de error a la lista ```errores```.

6) El siguiente bloque ```if``` utiliza una comprensión de listas y el método ```isdigit()``` para verificar si hay al menos un número en la contraseña. Si no se cumple esta condición, se agrega un mensaje de error a la lista ```errores```.

El último bloque ```if``` utiliza una comprensión de listas y verifica si hay al menos uno de los caracteres especiales (!, @, #, $, %, &, /) en la contraseña. Si no se cumple esta condición, se agrega un mensaje de error a la lista ```errores```.

Una vez que se han verificado todos los requisitos, se devuelve la lista de ```errores```.

Luego, se solicita al usuario que ingrese una contraseña mediante el uso de la función ```input()``` y se almacena en la variable ```contrasena```.

Se llama a la función ```verificar_contrasena``` pasando como argumento la contraseña ingresada, y el resultado se guarda en la variable ```errores```.

Se verifica si la longitud de la lista de ```errores``` es igual a cero. Si es así, se imprime "Contraseña válida". En caso contrario, se imprime "La contraseña no cumple con los siguientes requisitos:" y se muestra cada mensaje de error de la lista ```errores``` utilizando un bucle ```for```.
