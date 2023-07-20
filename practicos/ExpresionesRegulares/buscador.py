import re

def buscar_expresion_regular(archivo, expresion_regular):
    try:
        with open(archivo, 'r', encoding='utf-8') as archivo_texto:
            contenido = archivo_texto.read()
            resultados = re.findall(expresion_regular, contenido)
            return resultados
    except FileNotFoundError:
        print("No se encontró el archivo. Verifica la ruta y nombre del archivo.")
        return []
    except Exception as e:
        print("Ocurrió un error durante la lectura del archivo:", e)
        return []

# Ruta del archivo de texto
ruta_archivo = 'invariantes.txt'

# Expresión regular que deseas buscar en el archivo
expresion_regular = r'(T0)(.*?)'

# Llamada a la función para buscar la expresión regular en el archivo
resultados_encontrados = buscar_expresion_regular(ruta_archivo, expresion_regular)

# Imprimir los resultados
print("Resultados encontrados:")
for resultado in resultados_encontrados:
    print(resultado)

