import re

def identificar_proposiciones(oracion):
    # Definir los conectores y sus símbolos
    operadores = {
        " y ": "∧", 
        " o ": "∨", 
        "no ": "¬", 
        " pero ": "∧", 
        " además, ": "∧", 
        " Además, ": "∧",
        ", ": "∧"  # Para manejar las comas
    }
    
    # Reemplazar los conectores con sus símbolos
    for conector, simbolo in operadores.items():
        oracion = oracion.replace(conector, simbolo)

    # Dividir en proposiciones simples y en los operadores
    proposiciones_simples = re.split(r'[∧∨]', oracion)
    operadores_encontrados = re.findall(r'[∧∨]', oracion)
    
    # Crear un array para las letras, considerando la negación (¬)
    letras = []
    for i, prop in enumerate(proposiciones_simples):
        prop = prop.strip()  # Limpiar espacios
        if '¬' in prop:  # Si la proposición contiene la negación
            letras.append('¬' + chr(65 + i))  # Agregar ¬ seguido de la letra
        else:
         letras.append(chr(65 + i))  # Solo la letra

    # Reconstruir la oración con letras y operadores
    nueva_oracion = ""
    for i in range(len(letras)):
        nueva_oracion += letras[i]  # Agregar la proposición con su letra
        if i < len(operadores_encontrados):  # Si hay un operador correspondiente
            nueva_oracion += operadores_encontrados[i]  # Agregar el operador
    
    return nueva_oracion, letras

# Ejemplo de uso
oracion = "Hoy es lunes y está lloviendo, o voy al trabajo. Además, hay tráfico en la carretera o no llego a tiempo, pero también puede ser que llego a tiempo y está lloviendo."
frase_con_cambios, letras = identificar_proposiciones(oracion)

print("Frase con cambios:", frase_con_cambios)
print("Frases sustituidas por letras:", letras)