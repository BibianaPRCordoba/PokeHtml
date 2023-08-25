#Script padre de PokeHtml
#*PLEASE RUN THIS SCRIPT
#Este script es el que se corre en consola para poner en marcha el sistema de generación de HTML
#Bibiana Pérez Rios Córdoba

import os

def mostrar_menu():
    print("Elige un Pokémon:")
    print("1. Pichu")
    print("2. Charmander")
    print("3. Wartortle")
    print("4. Venusaur")
    
    opcion = input("Ingresa el número de opción: ")
    return opcion

if __name__ == "__main__":
    opciones = {
        "1": "pichu",
        "2": "charmander",
        "3": "wartortle",
        "4": "venusaur"
    }

    opcion_elegida = mostrar_menu()
    pokemon_nombre = opciones.get(opcion_elegida, None)
    
    if pokemon_nombre:
        os.system(f"python pokemonHijo.py {pokemon_nombre}")
        print(f"Archivo {pokemon_nombre}.html generado exitosamente!")
    else:
        print("Opción no válida.")
