import os

# Obtiene el path actual donde se encuentra el Main.py, este directorio lo separa y lo mete en una lista

# Valida el sistema operativo para adaptar el path de busqueda
if os.name == 'posix':
    path = os.path.abspath(__file__).split("/")
else:
    path = os.path.abspath(__file__).split("\\")


# Este va ser el nuevo path para buscar las pruebas
NEW_PATH = ""

# Insertar todos los paths menos el último, exceptuando la carpeta main
for i in range(len(path) - 5):
    NEW_PATH += path[i] + '/'


NEW_PATH += "resources/"