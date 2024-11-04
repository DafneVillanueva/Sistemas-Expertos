import re
import pandas as pd
import itertools
import os
def Formula(oracion):    
    operadores = {
        " y ": "∧", 
        " o ": "∨", 
        "∧no ": "∧¬",
        "∨no ": "∨¬",
        "No ": "¬",
        " pero ": "∧", 
        " además, ": "∧", 
        " Además, ": "∧",
    }   
  
    for conector, simbolo in operadores.items():
        oracion = oracion.replace(conector, simbolo)
    frase=Separador(oracion)

    frases_vistas = {}
    contador=1
    def reemplazar_por_variable(match):
        nonlocal contador
        frase = match.group(0)
        if frase in frases_vistas:
            return frases_vistas[frase]
        else:
            resultado = f"X{contador}"
            frases_vistas[frase] = resultado 
            contador += 1
            return resultado
    formula= re.sub(r"[^∧∨¬]+", reemplazar_por_variable, oracion)
    formula=Separador(formula)
    #res_formula=Unir(formula)
    #res_frase=Unir(frase)
    return formula,frase

def Separador(oracion):
    separacion=oracion.replace("∧", "☺∧☺")
    separacion=separacion.replace("∨", "☺∨☺")
    separacion=separacion.replace("¬", "☺¬☺")
    separacion = re.split(r"☺", separacion)
    separacion = [elemento for elemento in separacion if elemento != '']
    return separacion

def Unir(frase):
    union=""
    for i in range(len(frase)):
        union=union+frase[i]
    return union

def Tabla_Atomos(formula,frase):
    res_formula=Unir(formula)
    res_frase=Unir(frase)
    res_frase=re.split(r'[∧∨¬]', res_frase)
    res_frase = [elemento for elemento in res_frase if elemento != '']
    res_formula=re.split(r'[∧∨¬]', res_formula)
    res_formula = [elemento for elemento in res_formula if elemento != '']
    array_var = []
    vistos = set()
    for elemento in res_formula:
        if elemento not in vistos:
            vistos.add(elemento)
            array_var.append(elemento)
    array_frase = []
    vistos2 = set()
    for elemento in res_frase:
        if elemento not in vistos2:
            vistos2.add(elemento)
            array_frase.append(elemento)
    print("Tabla de Atomos")
    print("____________________________")
    for i in range(len(array_frase)):
        print("____________________________\n")
        print(array_var[i]+":"+array_frase[i])
        print("____________________________")
    print("____________________________")
    return 

def Tabla_Booleana(oracion):
    formula=Unir(oracion)
    print(formula)
    # Reemplazar los símbolos lógicos por sus equivalentes en Python
    formula_python = formula.replace("∧", " and ").replace("∨", " or ").replace("¬", " not ")

    # Identificar todas las variables únicas en la fórmula (formato X seguido de un número)
    variables = sorted(set(re.findall(r'X\d+', formula)))

    # Generar todas las combinaciones posibles de valores de verdad para las variables
    valores = [True, False]
    combinaciones = list(itertools.product(valores, repeat=len(variables)))

    # Imprimir la tabla de verdad
    encabezado = "\t".join(variables) + "\tResultado"
    print(encabezado)
    print("-" * (len(encabezado) + 1))
    
    for combinacion in combinaciones:
        # Crear un diccionario para asignar valores a cada variable
        contexto = dict(zip(variables, combinacion))

        # Evaluar la expresión en el contexto de valores de verdad actuales
        try:
            resultado = eval(formula_python, {}, contexto)
        except Exception as e:
            resultado = f"Error: {e}"

        # Imprimir la combinación de valores y el resultado
        valores_str = "\t".join(str(contexto[var]) for var in variables)
        print(f"{valores_str}\t{resultado}")
    return

def Guardar(oracion):
    formula=Unir(oracion)
    if not os.path.exists("Reglas.txt"):
        with open("Reglas.txt", 'w', encoding='utf-8') as archivo:
            print(f"Archivo Reglas.txt creado.")

    with open("Reglas.txt", 'a', encoding='utf-8') as archivo:
        archivo.write(formula + ".\n")
        print("Nueva información agregada exitosamente.")
    return 

def Cargar():
    if os.path.exists("Reglas.txt"):
        with open("Reglas.txt", 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            return contenido
    else:
        print("No se ha generado ningun archivo")
        return 
    
    
def Arbol_binario(oracion):
    
    return nueva_oracion, letras

def Multiples_reglas(oracion):
    
    return nueva_oracion, letras

def Regresion(oracion):
    
    return nueva_oracion, letras

def opciones():
    print('1.-Agregar una regla.')
    print('2.-Cargar reglas.')
    print('3.-Guardar regla.')
    print('5.-Ver Tabla de verdad')
    print('6.-Ver arbol binario')
    print('7.-Salir')
    
def invocacion(respuesta: int):
    menu={
            1:1,
            2:2,
            3:3,
            4:4,
            5:5,
            6:6,
            7:7
        }
    return menu.get(respuesta, "Opción inválida")

def Menu():
    respuesta=0
    cont=0
    print('Hola bienvenid@')
    while respuesta!=7:
        print('Que deseas hacer?')
        opciones()
        respuesta=int(input("\n"))
        menu=invocacion(respuesta)
        if menu ==1:
            #oracion=input("Ingresa la frase \n")
            oracion='No termino mi proyecto o no tengo tiempo libre o no me siento bien o no recibo ayuda o puedo salir de vacaciones y termino mi proyecto'
            formula,frase=Formula(oracion)
            formula=Unir(formula)
            cont=cont+1
            print('El resultado es: ',formula+'\n')
        elif menu==2:
            BD=Cargar()
            
            print('El resultado es: \n',BD)
        elif menu==3:
            if cont >0:
                Guardar(formula)
            else:
                print('Crea una formula antes')
        elif menu==4:
            print('Crea una formula antes')
        elif menu==5:
            print('Crea una formula antes')
        elif menu==6:
            print('Crea una formula antes')
    print('Nos vemos!!!')  
    
Menu()
#print(formula)
#print(frase)
#Tabla_Atomos(formula,frase)
#Tabla_Booleana(formula)
#Guardar(formula)
#BD=Cargar(formula)
#print(BD)
