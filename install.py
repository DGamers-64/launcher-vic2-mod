import subprocess
import json

def nombrar_mod():
    nombre = input("Nombre completo del mod: ")
    abreviatura = input("Abreviatura del mod: ")
    instalado = "True"

    configuracion = {"NOMBRE_MOD": nombre, "ABREVIATURA_MOD": abreviatura, "INSTALADO": instalado}

    with open("config.json", "w") as archivo:
        json.dump(configuracion, archivo, indent=4)

nombrar_mod()