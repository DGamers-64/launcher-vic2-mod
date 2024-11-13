# AUTOR: xLune64

import subprocess
import os
import json

# FUNCIONES IMPORTANTES

def cargar_configuracion():
    with open("config.json", "r") as archivo:
        configuracion = json.load(archivo)
    return configuracion

def wsl_is_installed():
    result = subprocess.run(["wsl", "--version"], capture_output=True, text=True)

    if result.returncode == 0:
        return True
    return False

import os

def convertir_ruta_wsl(ruta_windows):
    
    ruta_windows = ruta_windows.replace("\\", "/")
    
    if ruta_windows[1:3] == ":/":
        unidad = ruta_windows[0].lower()
        ruta_wsl = "/mnt/" + unidad + ruta_windows[2:]
        return ruta_wsl
    else:
        print(f"Error: La ruta proporcionada no tiene un formato válido: {ruta_windows}")
        return None
    
def programa_principal():
    print("LAUNCHER MODDING VICTORIA 2")
    print("---------------------------")
    print("1. Abrir el juego")
    print("2. Borrar caché")
    print("3. Abrir error.log")
    print("4. Abrir game.log")
    if (wsl_is_installed()):
        print("5. Abrir en vivo error.log")
        print("6. Abrir en vivo game.log")

    opcion = int(input("Elige una opción: "))

    try:
        match opcion:
            case 1:
                open_game()
            case 2:
                delete_cache(config, ruta_cache_mod)
            case 3:
                open_error_log(ruta_cache_mod)
            case 4:
                open_game_log(ruta_cache_mod)
            case 5:
                open_live_error_log(ruta_cache_mod)
            case 6:
                open_live_game_log(ruta_cache_mod)
            case _:
                print("Error: Selecciona una respuesta válida")
    except:
        print("¡Ha habido un error!")

# FUNCIONES DE PROGRAMA

def open_game():
    subprocess.run(['start', 'steam://rungameid/42960'], shell=True)
    return True

def delete_cache(config, ruta):
    subprocess.run(["rmdir", "/Q", "/S", ruta], shell=True)
    return True

def open_error_log(ruta):
    subprocess.run(["notepad", ruta + f"logs\\error.log"])
    return True

def open_game_log(ruta):
    subprocess.run(["notepad", ruta + f"logs\\game.log"])
    return True

def open_live_error_log(ruta):
    ruta = convertir_ruta_wsl(ruta)
    subprocess.run(["wsl", "less", "+F", os.path.join(ruta, "logs/error.log")])
    return True

def open_live_game_log(ruta):
    ruta = convertir_ruta_wsl(ruta)
    subprocess.run(["wsl", "less", "+F", os.path.join(ruta, "logs/game.log")])
    return True

# PROGRAMA PRINCIPAL

config = cargar_configuracion()
ruta_cache_mod = f"C:\\Users\\{os.environ['USERNAME']}\\Documents\\Paradox Interactive\\Victoria II\\{config['ABREVIATURA_MOD']}\\"

if(config["INSTALADO"] == "False"):
    print("Primero ejecuta install.py")
else:
    programa_principal()