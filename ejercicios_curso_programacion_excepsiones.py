"""Escribe un programa que intente dividir dos números.
 Si el segundo número es cero,
captura la excepción ZeroDivisionError
 y muestra un mensaje de error al usuario"""
def dividir_numeros (numero1,numero2):
 try:
  division = numero1 / numero2
  return  division
 except ZeroDivisionError:
    return "Ha ocurrido un error, no se puede dividir por cero"
"""Escribe un programa que intente sumar un número y una cadena.
Si se produce un errorde tipo,
captura la excepción TypeError y
muestra un mensaje de error al usuario."""
def sumar_numeros_y_cadenas (numero, cadena):
  try:
    suma = numero + cadena
    return suma
  except TypeError:
    return "ocurrio un error de tipo, no se puede sumar un numero con una cadena"
"""Escribe un programa que intente acceder a una clave que no existe en un
diccionario. 
Si se produce una excepción KeyError, captura la excepción y muestra."""
diccionario = {"nombre": "Lionel","apellido": "Messi"}
def accediendo_a_claves_de_diccionarios(dict, clave):
 try:
  return(diccionario[clave])
 except KeyError:
  print("Esta clave no esta en el diccionario")
"""escribe un programa que intente abrir un archivo que no existe. Si se produce una excepción
FileNotFoundError, captura la excepción y muestra un mensaje de error al usuario. Sin
embargo, también intenta crear el archivo si no existe."""
def abrir_o_crear(ruta, contenido_por_defecto=""): 
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            contenido = f.read()
        return contenido
    except FileNotFoundError:
        print(f"Error: el archivo '{ruta}' no existe. Se intentará crearlo ahora.")
        with open(ruta, "w", encoding="utf-8") as f:
                f.write(contenido_por_defecto)
        print(f"Archivo '{ruta}' creado correctamente.")
        return contenido_por_defecto
"""Escribe un programa que intente dividir dos números.
 Si el segundo número es cero,
captura la excepción ZeroDivisionError.
 Si el primer número es un número no válido,
captura la excepción ValueError. 
En cualquier caso, muestra un mensaje de error al usuario."""
def dividir_dos_numeros(numero1, numero2):
   try: 
    if not isinstance(numero1, (int, float)):
            raise ValueError("El primer valor no es un número válido")
    if numero2 == 0:
            raise ZeroDivisionError("No se puede dividir por 0")
   except ValueError as e:
        print("Error:", e)
   except ZeroDivisionError as e:
        print("Error:", e)
   else:
     resultado = numero1 / numero2
     return resultado




