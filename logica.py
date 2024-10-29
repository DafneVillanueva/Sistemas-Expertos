import re
import itertools
import networkx as nx
import matplotlib.pyplot as plt

# Función para identificar proposiciones y reemplazar conectores por símbolos lógicos
def identificar_proposiciones(oracion):
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
    
    letras = []
    for i, prop in enumerate(proposiciones_simples):
        prop = prop.strip()
        if '¬' in prop:
            letras.append('¬' + chr(65 + i))
        else:   
            letras.append(chr(65 + i))

    nueva_oracion = ""
    for i in range(len(letras)):
        nueva_oracion += letras[i]
        if i < len(operadores_encontrados):
            nueva_oracion += operadores_encontrados[i]
    
    return nueva_oracion, letras

# Función para separar proposiciones
def separar_proposiciones(expresion):
    return re.split(r'\s*[∨∧]\s*|\s*\(\s*|\s*\)\s*', expresion)

# Función para generar combinaciones de verdad
def generar_combinaciones(proposiciones):
    return list(itertools.product([True, False], repeat=len(proposiciones)))

# Función para evaluar una expresión lógica dada una combinación de valores de verdad
def evaluar_expresion(expresion, valores):
    # Crear un diccionario de valores de proposiciones
    entorno = dict(zip([chr(65 + i) for i in range(len(valores))], valores))
    
    # Sustituir letras por sus valores booleanos en la expresión
    for letra, valor in entorno.items():
        expresion = expresion.replace(letra, str(valor))
    
    # Reemplazar operadores lógicos
    exp_eval = expresion.replace('∨', ' or ').replace('∧', ' and ').replace('¬', ' not ')
    
    return eval(exp_eval)

# Función para generar una tabla de verdad para una expresión lógica
def tabla_de_verdad(expresion):
    proposiciones = separar_proposiciones(expresion)
    combinaciones = generar_combinaciones(proposiciones)
    
    print(f"Tabla de verdad para la expresión: {expresion}")
    print(" | ".join(proposiciones) + " | Resultado")
    print("-" * (len(proposiciones) * 10 + 15))
    
    for valores in combinaciones:
        resultado = evaluar_expresion(expresion, valores)
        print(" | ".join([str(int(v)) for v in valores]) + f" | {int(resultado)}")

# Función para crear un grafo visual de la expresión lógica
def crear_grafo(expresion, variables):
    grafo = nx.DiGraph()
    valores_de_verdad = list(itertools.product([False, True], repeat=len(variables)))
    
    for combinacion in valores_de_verdad:
        valores = dict(zip(variables, combinacion))
        resultado = evaluar_expresion(expresion, list(valores.values()))
        camino = ', '.join(f'{var}={valores[var]}' for var in variables)
        
        grafo.add_node(camino)
        grafo.add_edge(camino, f'Resultado: {resultado}')

    return grafo

# Función principal que integra todas las funcionalidades
def main():
    # Solicitar al usuario que ingrese la oración
    oracion = input("Introduce una oración con conectores lógicos (por ejemplo, 'No termino mi proyecto o no tengo tiempo libre'): ")
    expresion, letras = identificar_proposiciones(oracion)
    
    print("Frase con cambios a símbolos lógicos:", expresion)
    print("Proposiciones sustituidas por letras:", letras)
    
    # Generar la tabla de verdad
    tabla_de_verdad(expresion)
    
    # Crear el grafo a partir de la expresión lógica
    variables = [letra.strip('¬') for letra in letras]
    grafo = crear_grafo(expresion, variables)
    
    # Dibujar el grafo
    pos = nx.spring_layout(grafo, k=2.0)
    plt.figure(figsize=(12, 10))
    nx.draw(grafo, pos, with_labels=True, arrows=True, node_size=3000, node_color='lightblue', font_size=10)
    plt.title('Grafo de Proposiciones Simples', fontsize=16)
    plt.axis('off')
    plt.show()

# Ejecutar la función principal
if __name__ == "__main__":
    main()
