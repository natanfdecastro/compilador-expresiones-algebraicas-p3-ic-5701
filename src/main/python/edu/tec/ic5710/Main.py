import sys
import os

from LexicalAnalyser import Scanner

# Comando de ejecucion: python3 Main.py <programa.txt>

# Obtiene el path actual donde se encuentra el Main.py, este directorio lo separa y lo mete en una lista
path = os.getcwd().split("\\")

# Este va ser el nuevo path para buscar las pruebas
new_path = ""

# Insertar todos los paths menos el último, exceptuando la carpeta main
for i in range(len(path)-4):
    new_path += path[i] + '/'

# Concatena la carpeta resources al path nuevo, esto para que apunte a una nueva carpeta
new_path += "resources/"

# Editar la ruta según computadora que se ejecuta
file = open(new_path + sys.argv[1],'r')

program = file.read()

file.close()

scanner = Scanner(program)